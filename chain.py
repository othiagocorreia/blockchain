from block import Block

t1 = "Thiago transferiu: 15 Bitcoin(s) para Thiago"

class Chain:
    def __init__(self):
        self.chain = []
        self.allTransactions = []
        self.genesisBlock()

    def genesisBlock(self):
        transactions = t1
        previousHash = 0
        self.chain.append(Block(transactions, previousHash))
    
    def addBlock(self, transactions):
        previousHash = self.chain[len(self.chain)-1].hash
        newBlock = Block(transactions, previousHash)
        self.chain.append(newBlock)

    def showBlocks(self):
        for i in range(len(self.chain)):
            currentBlock = self.chain[i]
            print("\nInformações do Bloco {}".format(i), "\n")
            currentBlock.showBlock()
    
Blockchain = Chain()