import datetime as dt
import hashlib

class block:
    def __init__(self, transactions, prevHash):
        self.timestamps = dt.datetime.now() #Quando foi criado o bloco
        self.transactions = transactions
        self.prevHash = prevHash
        self.hash = self.generateHash()
        #index
        #nonce

    def generateHash(self):
        blockData = str(self.transactions) + str(self.timestamps) + str(self.prevHash)
        hashBlock = hashlib.sha256(blockData.encode()).hexdigest() 
        return hashBlock

    def showBlock(self):
        print("Informações do bloco")
        print("Data de criação: ", str(self.timestamps))
        print("Transações: ", str(self.transactions))
        print("Hash atual: ", str(self.hash))
        print("Hash Anterior: ", str(self.prevHash), "\n")
