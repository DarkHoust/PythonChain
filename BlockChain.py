import hashlib
import json
import time
import secrets

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []

    def createGenesisBlock(self):
        genesisBlock = Block(0, [], time.time(), "0")
        self.chain.append(genesisBlock)

    def addTransaction(self, sender, recipient, amount, privateKey):
        transaction = Transaction(sender, recipient, amount)
        signature = self.signTransaction(transaction, privateKey)
        self.transactions.append({
            'transaction': transaction.toDict(),
            'signature': signature
        })

    def signTransaction(self, transaction, privateKey):
        message = json.dumps(transaction.toDict(), sort_keys=True)
        hashValue = hashlib.sha256(message.encode()).hexdigest()
        signature = self.generateSignature(privateKey, hashValue)
        return signature

    def generateSignature(self, privateKey, messageHash):
        # In a real-world scenario, you would use a secure digital signature algorithm.
        # This example uses a simple HMAC-based approach, which is not suitable for production.
        key = secrets.token_bytes(32)  # This should be replaced with the private key
        return hashlib.sha256(key + messageHash.encode()).hexdigest()

    def mineBlock(self):
        if not self.transactions:
            print("No transactions to mine.")
            return

        lastBlock = self.chain[-1]

        newBlock = Block(
            index=lastBlock.index + 1,
            transactions=self.transactions,
            timestamp=time.time(),
            previousHash=lastBlock.calculateHash()
        )

        newBlock.nonce = self.proofOfWork(newBlock)

        self.chain.append(newBlock)
        self.transactions = []
        print("Block mined successfully.")

    def proofOfWork(self, block):
        block.nonce = 0
        computedHash = block.calculateHash()
        while not computedHash.startswith('0000'):
            block.nonce += 1
            computedHash = block.calculateHash()
        return block.nonce

    def displayBlockchain(self):
        for block in self.chain:
            print(f"Block #{block.index}, Hash: {block.calculateHash()}")
            for transaction in block.transactions:
                print(f"  Transaction: {transaction['transaction']}")
                print(f"  Signature: {transaction['signature']}")
            print("\n")

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def toDict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }

class Block:
    def __init__(self, index, transactions, timestamp, previousHash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.nonce = nonce

    def calculateHash(self):
        blockString = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(blockString.encode()).hexdigest()

# CLI menu (unchanged)
def mainMenu():
    blockchain = Blockchain()
    blockchain.createGenesisBlock()

    while True:
        print("\nBlockchain Menu:")
        print("1. Add Transaction")
        print("2. Mine Block")
        print("3. View Blockchain")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            sender = input("Enter sender address: ")
            recipient = input("Enter recipient address: ")
            amount = float(input("Enter transaction amount: "))
            privateKey = input("Enter sender's private key: ")
            blockchain.addTransaction(sender, recipient, amount, privateKey)
            print("Transaction added successfully.")

        elif choice == '2':
            blockchain.mineBlock()

        elif choice == '3':
            blockchain.displayBlockchain()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    mainMenu()
