from os import system, name
from blockchain import Blockchain

# Create a new blockchain instance
blockchain = Blockchain()

# Define the menu options
menu_options = {
    '1': {
        'description': 'Add a new transaction',
        'function': lambda: add_transaction()
    },
    '2': {
        'description': 'Create a new block',
        'function': lambda: create_block()
    },
    '3': {
        'description': 'Print the blockchain',
        'function': lambda: print_blockchain()
    },
    '4': {
        'description': 'Quit',
        'function': lambda: quit()
    }
}

# Define the menu functions
def add_transaction():
    sender = input("Sender: ")
    recipient = input("Recipient: ")
    amount = input("Detail: ")
    blockchain.new_transaction(sender, recipient, amount)
    print("Transaction added successfully!")
    if len(blockchain.pending_transactions) == 1:
        print("Pending transaction: 1")
    else:
        print("Pending transactions: " + str(len(blockchain.pending_transactions)))
    input("Press Enter to continue...")
    clear()

def create_block():
    proof = int(input("Enter proof number: "))
    blockchain.new_block(proof)
    print("Block created successfully!")
    print("Total blocks created: " + str(len(blockchain.chain)))
    input("Press Enter to continue...")
    clear()

def print_blockchain():
    blockchain.print_blockchain()
    input("Press Enter to continue...")
    clear()

def clear():
    # Windows use 'cls' and Unix-based systems like Linux and macOS use 'clear' to clear the terminal
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Define the main loop
while True:
    clear()
    # Print the menu options
    print("Simple Blockchain")
    print("-------------------------")
    
    for key, value in menu_options.items():
        print(key + ': ' + value['description'])

    # Print number of pending transactions and number of blocks created
    if len(blockchain.pending_transactions) == 1:
        print("Pending transaction: 1")
    else:
        print("Pending transactions: " + str(len(blockchain.pending_transactions)))
        
    print("Total blocks created: " + str(len(blockchain.chain)))
    
    print("-------------------------")

    # Prompt the user to choose an option
    choice = input("Enter your choice: ")

    # Execute the chosen function
    if choice in menu_options:
        menu_options[choice]['function']()
    else:
        print("Invalid choice. Please try again.")
