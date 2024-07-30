import socket

# Function to display the board
def display_board(board):
    for i in range(0, 9, 3):
        print(f"| ({board[i]}) | ({board[i+1]}) | ({board[i+2]}) |")

# Function to check for a win
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[cell] == player for cell in condition) for condition in win_conditions)

# Function to check if the board is full
def check_full(board):
    return all(cell in ['X', 'O'] for cell in board)

# Set up the client
HOST = '127.0.0.1'
PORT = 65433

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

board = [str(i+1) for i in range(9)]
current_player = 'X' # Client starts with 'X'

while True:
    display_board(board)
    
    if current_player == 'X':
        # Client's turn
        move = int(input("Client (X), enter your move (1-9): ")) - 1
        if board[move] not in ['X', 'O']:
            board[move] = 'X'
            client_socket.sendall(str(move).encode())
            if check_win(board, 'X'):
                display_board(board)
                print("Client (X) wins!")
                break
            if check_full(board):
                display_board(board)
                print("It's a tie!")
                break
            current_player = 'O'
        else:
            print("Invalid move. Try again.")
    else:
        # Waiting for server's move
        print("Waiting for server's move...")
        data = client_socket.recv(1024).decode()
        if not data:
            print("Connection closed by server.")
            break
        move = int(data)
        board[move] = 'O'
        if check_win(board, 'O'):
            display_board(board)
            print("Server (O) wins!")
            break
        if check_full(board):
            display_board(board)
            print("It's a tie!")
            break
        current_player = 'X'

client_socket.close()
