"""
defines block object.
"""

class Block(object):
    """
    a blockchain is composed of blocks. each block is represented by a 
    block header. 

    each block header is represented as a block hash, which is calculated by
    the (a) previous block header, (b) a merkle root hash, and (c) a nonce.
    """
    def __init__(self, data):
        self.index = 0
        self.prev_hash = "0"
        self.data = data
        self.block_hash = "0"
        self.nonce = 0

    def show(self):
        print ">>> block hash:", self.block_hash
        print ">>> block index:", self.index
        print ">>> previous block hash:", self.prev_hash
        print ">>> root hash:", self.data
        print ">>> nonce: ", self.nonce

    def fetch_transaction(self):
        """return transaction record.
        """
        return "transaction " + str(self.index) + " : " + self.data
