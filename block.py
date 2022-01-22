import datetime as dt
import hashlib

sender = str(input("Qual o seu nome?"))
amount = str(input("Quantos Bitcoins você quer transferir?"))
recipient = str(input("Para quem você quer transferir?"))

transaction = sender + " transferiu: " + amount + " Bitcoin(s) para " + recipient

class block:
    def __init__(self, transactions):
        self.timestamps = dt.datetime.now() #Quando foi criado o bloco
        self.transactions = transactions
        #prevHash
        self.hash = self.generateHash()
        #index
        #nonce

    def generateHash(self):
        blockData = str(self.transactions) + str(self.timestamps)
        hashBlock = hashlib.sha256(blockData.encode()).hexdigest() 
        return hashBlock
        

block1 = block(transaction)

print(block1.transactions, block1.timestamps, block1.hash)