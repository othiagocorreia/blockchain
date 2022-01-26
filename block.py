import datetime as dt
import hashlib

class Block():
    def __init__(self, transactions, prevHash):
        self.transactions = transactions
        self.timestamps = dt.datetime.now()
        self.prevHash = prevHash
        #nonce
        self.hash = self.generateHash()

    def generateHash(self):
        blockData = str(self.transactions) + str(self.timestamps) + str(self.prevHash)
        blockHash = hashlib.sha256(blockData.encode()).hexdigest()
        return blockHash

    def showBlock(self):
        print("Transações: ", self.transactions)
        print("Hora e Data: ", self.timestamps)
        print("Hash do bloco: ", self.hash)
        print("Hash Anterior: ", self.prevHash)