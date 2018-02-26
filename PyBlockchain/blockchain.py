"""
blockchain object.
"""
class Blockchain(object):
    """blockchain object.
    """
    def __init__(self, genesis_block):
        """
        in this example, blockchain will be a python list consisting 
        of Block objects. 
        """
        self.blockchain = [genesis_block]

    def get_length(self):
        return len(self.blockchain)

    def get_block(self, idx):
        return self.blockchain[idx]

    def add_block(self, block):
        self.blockchain.append(block)
