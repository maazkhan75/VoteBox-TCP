# 🗳️ VoteBox_TCP

**VoteBox_TCP** is a Python-based voting system built using TCP client-server architecture with file handling for storing data. This project ensures secure management of candidate details, voter information, and vote casting, all while leveraging efficient file storage and communication over TCP.

### Key Features 💡
- **Client-Server Architecture** 🌐: Robust TCP connection between the voting clients and server.
- **File Handling** 🗂️: Organized file storage for candidate, voter, and vote data.
- **Simple Setup** ⚙️: Easy to deploy and run, with clear separation of server and client operations.

### Ideal For 🎯
- **Network Programming** 🖧: A practical example of client-server communication using TCP.
- **File-based Data Management** 📁: Demonstrates how to store and retrieve data from files efficiently.

### Requirements 🛠️
- Python 3.x 🐍
- Socket Programming Knowledge 🌐
- Basic File Handling Skills 🗂️

### Project Structure 🏗️
- `server.py` 🖥️: Handles connections from multiple clients and processes votes.
- `client.py` 💻: Allows users to cast votes.
- `Candidates_List.txt` 📜: Stores candidate data.
- `Voters_List.txt` 📜: Stores voter registration details.
- `Vote_Casting.txt` 📝: Records cast votes.

### How to Run 🚀

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/maazkhan75/VoteBox_TCP.git
   ```
2. **Run the Server**
  ```bash
  python server.py
  ```
3. **Run the Client/s**
   
  ```bash
  python client.py
  ```
