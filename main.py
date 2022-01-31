from chain import Blockchain

blocos = int(input("Quantos blocos você quer criar?"))

i = 0
while(i<blocos):
    sender = str(input("Qual o seu nome?"))
    amount = str(input("Quantos Bitcoins você quer transferir?"))
    recipient = str(input("Para quem você quer transferir?\n"))
    
    transaction = sender + " transferiu: " + amount + " Bitcoin(s) para " + recipient

    Blockchain.addBlock(transaction)
    i += 1

Blockchain.showBlocks()
