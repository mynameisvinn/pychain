from hashlib import sha256

class Block(object):
    """
    a blockchain is composed of blocks. each block is represented by a 
    block header. 

    each block header is represented with a block hash. 

    a block hash is determined by the (a) previous block header, (b) a root 
    hash, and (c) a nonce.
    """
    def __init__(self, ls_transactions):
        self.index = 0
        self.prev_hash = "0"
        self.ls_transactions = ls_transactions
        self.block_hash = "0"
        self.nonce = 0

    def show(self):
        print ">>> block hash:", self.block_hash
        print ">>> block index:", self.index
        print ">>> previous block hash:", self.prev_hash
        print ">>> root hash:", self.root_hash
        print ">>> nonce: ", self.nonce
        print ">>> transactions", self.ls_transactions

    @property
    def root_hash(self):
        a, b, c, d = map(lambda x: sha256(x).hexdigest(), self.ls_transactions)
        e = sha256(a + b).hexdigest()
        f = sha256(c + d).hexdigest()
        return sha256(e + f).hexdigest()