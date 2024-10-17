import socket

def main():
    server_ip = '127.0.0.1'
    server_port = 7000
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((server_ip, server_port))
    print("socket created and connected to server")

    client_message = input("enter your Name & CNIC in the format (name/cnic): ")
    tcp_socket.sendall(client_message.encode())

    server_message = tcp_socket.recv(2000)
    server_message = server_message.decode()       
    
    if server_message != "Voter not verified!":

        print(f"{server_message}")

        candidates_str = tcp_socket.recv(2000)
        print(f"server sended:\n{candidates_str.decode()}")

        selected_poll = input("input poll symbol : ")
        tcp_socket.sendall(selected_poll.encode())


        poll_verification_msg = tcp_socket.recv(2000)
        poll_verification_msg = poll_verification_msg.decode()

        if poll_verification_msg == "Poll verified!":
            print("Poll verified by server!")
            vote_status_message = tcp_socket.recv(2000)
            print(f"vote status: {vote_status_message.decode()}")
        else:
            print("Poll not verified by server!")

    else:
        print("You are not verified by server!")

    tcp_socket.close()

if __name__ == "__main__":
    main()