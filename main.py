from chain import Blockchain

sender = str(input("Qual o seu nome?"))
amount = str(input("Quantos Bitcoins você quer transferir?"))
recipient = str(input("Para quem você quer transferir?"))

transaction = sender + " transferiu: " + amount + " Bitcoin(s) para " + recipient 


Blockchain.addBlock(transaction)
Blockchain.showBlocks()