from hashlib import sha256

def h(msg):
    return sha256(msg).hexdigest()  # in bitcoin's merkle trees, SHA256 is applied twice (known as double-SHA256)

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

    @property
    def root_hash(self):
        q = self.ls_transactions

        # if number of transactions is odd, duplicate last transaction
        n_transactions = len(q)
        if n_transactions % 2 == 1:
            q.append(q[n_transactions - 1])

        while len(q) > 1:
            a, b = q.pop(0), q.pop(0)
            c = h(a + b)
            q.append(c)
            print q
        return q[0]