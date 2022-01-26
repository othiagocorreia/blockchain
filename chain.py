from block import block

sender = str(input("Qual o seu nome?"))
amount = str(input("Quantos Bitcoins você quer transferir?"))
recipient = str(input("Para quem você quer transferir?"))

transaction = sender + " transferiu:" + amount + " Bitcoin(s) para " + recipient 

class chain:
    def __init__(self):
        self.chain = []
        self.allTransactions = []
        self.genesisBlock()

    def genesisBlock(self):
        transactions = []
        previousHash = 0
        self.chain.append(block(transactions, previousHash))

    def addBlock(self, transactions):
        previousBlockHash = self.chain[len(self.chain)-1].hash
        newBlock = block(transactions, previousBlockHash)
        self.chain.append(newBlock) 
    
    def printBlocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {}".format(i))
            current_block.showBlock()
    
Blockchain = chain()    
Blockchain.addBlock(transaction)
Blockchain.printBlocks()