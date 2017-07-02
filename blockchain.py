"""
blockchain object.
"""
class Blockchain(object):
    def __init__(self, genesis_block):
        self.blockchain = [genesis_block]
        
    def get_length(self):
        return len(self.blockchain)
    
    def get_block(self, idx):
        return self.blockchain[idx]
    
    def add_block(self, block):
        self.blockchain.append(block)