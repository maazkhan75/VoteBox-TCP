import socket
import threading    # for multi-threading

def validate_voter_from_file(file_path, voter_str):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if voter_str in line: 
                    return True
        return False
    except FileNotFoundError:
        print("File Not Found!")
    except Exception as e:
        print(f"Error : {e}")

def validatePollFromFile(file_path, poll):
    with open(file_path, 'r') as file:
        for line in file:
            if poll == line.split('/')[-1].strip():
                return True
    return False

def EnsureOneVoteByPerson(file_path, voter_str):
    with open(file_path, 'r') as file:
        for line in file:
            if voter_str == line.split('@')[0]:
                return False
    return True

def DisplayCandidatesFromFile(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def caste_vote_in_file(file_path, casting_str):
    with open(file_path, 'a') as file:
        file.write(casting_str + '\n')

def handle_client(connection):
    try:
        voter_str = connection.recv(2000).decode()
        print(f"Client sent = {voter_str}")

        if validate_voter_from_file('Voters_List.txt', voter_str):
            print(f"The voter '{voter_str}' is valid (confirmed from file).")
            welcome_msg = f"WELCOME voter: {voter_str} \nSending you list of candidates..."
            connection.sendall(welcome_msg.encode())

            candidate_data = DisplayCandidatesFromFile('Candidates_List.txt')
            connection.sendall(candidate_data.encode())

            chosen_poll = connection.recv(2000).decode()
            print(f"Client chose = {chosen_poll}")

            if validatePollFromFile('Candidates_List.txt', chosen_poll):
                print(f"The poll '{chosen_poll}' is valid (confirmed from file).")
                connection.sendall("Poll verified!".encode()) 

                casting_info = f"{voter_str}@{chosen_poll}"

                if EnsureOneVoteByPerson('Vote_Casting.txt', voter_str):
                    caste_vote_in_file('Vote_Casting.txt', casting_info)
                    print("Vote casted successfully!")
                    vote_status_msg = "Vote casted successfully!"
                    connection.sendall(vote_status_msg.encode())
                else:
                    print("Voter already has casted vote for some poll symbol!")
                    vote_status_msg = "Voter already has casted vote for some poll symbol!"
                    connection.sendall(vote_status_msg.encode())
            else:
                print(f"The poll '{chosen_poll}' is invalid (confirmed from file).")
                connection.sendall("Poll not verified!".encode()) 
        else:
            print(f"The voter '{voter_str}' is invalid (confirmed from file).")
            connection.sendall("Voter not verified!".encode())
    finally:
        connection.close()

def main():
    server_ip = '127.0.0.1'
    server_port = 7000
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((server_ip, server_port))
    print("Socket created and bound!")

    tcp_socket.listen(5)
    # The backlog is set to 5 here, which means that the server can queue up to 5 incoming connection requests if it is currently busy processing other connection requests.
    # If more than 5 clients attempt to connect simultaneously, any additional connection requests will be rejected until a slot in the queue becomes available.
    
    while True:
        connection, client_address = tcp_socket.accept()
        print(f"Connection from {client_address} has been established.")
        
        # Create a new thread for each client connection (for multi-threading)
        client_thread = threading.Thread(target=handle_client, args=(connection,))
        client_thread.start()

if __name__ == "__main__":
    main()
