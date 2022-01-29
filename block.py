import datetime as dt
import hashlib

class Block():
    def __init__(self, transactions, prevHash):
        self.transactions = transactions
        self.timestamps = dt.datetime.now()
        self.prevHash = prevHash
        self.nonce = 0
        self.hash = self.generateHash()

    def generateHash(self):
        blockHash = ''
        diff = 4
        while not blockHash.startswith('0'*diff):
            blockData = str(self.transactions) + str(self.timestamps) + str(self.prevHash) + str(self.nonce)
            blockHash = hashlib.sha256(blockData.encode()).hexdigest()
            self.nonce += 1
        return blockHash

    def showBlock(self):
        print("Transações: ", self.transactions)
        print("Hora e Data: ", self.timestamps)
        print("Hash do bloco: ", self.hash)
        print("Hash Anterior: ", self.prevHash)
        print("Nonce necessário: ", self.nonce)