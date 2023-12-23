# PythonChain
Overview
This project is a basic blockchain implementation in Python. It includes the core features of a blockchain, such as adding transactions, mining blocks, and proof-of-work.

Features
Create Blockchain: Initialize and create the genesis block for the blockchain.
Add Transaction: Add transactions to the list of unconfirmed transactions.
Mine Block: Generate a new block by mining the unconfirmed transactions.
Proof-of-Work: Implement a simple proof-of-work mechanism to secure the blockchain.
Display Blockchain: View the details of the blockchain, including block index, hash, and transactions.
How to Use
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/blockchain-python.git
cd blockchain-python
Run the Blockchain App:
bash
Copy code
python blockchain.py
Follow the Menu Options:
Use option 1 to add transactions.
Mine blocks using option 2.
View the blockchain with option 3.
Exit the application with option 4.
Requirements
Python 3.x
Example Usage
python
Copy code
# Import the Blockchain class
from blockchain import Blockchain

# Create a blockchain instance
blockchain = Blockchain()

# Create the genesis block
blockchain.createGenesisBlock()

# Add transactions
blockchain.addTransaction("Alice", "Bob", 10.0, "private_key_alice")
blockchain.addTransaction("Bob", "Charlie", 5.0, "private_key_bob")

# Mine a block
blockchain.mineBlock()

# Display the blockchain
blockchain.displayBlockchain()
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
