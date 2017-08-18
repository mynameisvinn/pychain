"""
defines block object.
"""

class Block(object):
    """
    the atomic unit of the blockchain is a block. each block is represented
    by a block header. 

    a block header is represented as a block hash, which is calculated by
    the (a) previous block header, (b) a merkle root hash, and (c) a nonce.
    """
    def __init__(self, index, prev_hash, data, curr_hash):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.curr_hash = curr_hash

    def update_hash(self, correct_hash):
        """
        A miner takes the (a) previous hash and (b) current data as input.
        it will try to  find a hash/seal such that, when appended to (a) + (b),
        it will yield a hash that satisfies the proof of work.
        """
        self.curr_hash = correct_hash

    def show(self):
        """helper function for QA. should be deleted.
        """
        print ">>> block index:", self.index
        print ">>> previous hash:", self.prev_hash
        print ">>> current hash:", self.curr_hash
        print ">>> transaction:", self.data

    def fetch_transaction(self):
        """return transaction record.
        """
        return "transaction " + str(self.index) + " : " + self.data
