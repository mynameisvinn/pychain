"""
defines block object.
"""

from hashlib import sha1

class Block(object):
    """
    the fundamental unit of the blockchain is a block. each block represents
    a "transaction".
    """
    def __init__(self, index, prev_hash, data, curr_hash):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.curr_hash = curr_hash  # current hash implicitly includes data

    def update_hash(self, correct_hash):
        """
        A miner takes the (a) previous hash and (b) current data as input.
        it will try to  find a hash/seal such that, when appended to (a) + (b),
        it will yield a hash that satisfies the proof of work.
        """
        self.curr_hash = correct_hash

    def show(self):
        print ">>> block index:", self.index
        print ">>> previous hash:", self.prev_hash
        print ">>> current hash:", self.curr_hash
        print ">>> transaction:", self.data

    @staticmethod
    def _hashhash(message):
        return sha1(message).hexdigest()

    @staticmethod
    def _proof_of_work(hash_output):
        """
        in practice, a hash/seal must begin with three zeros in order to be
        considered valid. in this example, a valid hash/seal (or proof of work)
        will have "c" as its 0th element.

        parameter:
        ----------
        hash_output : str
            representing hex digest
        """
        return hash_output[0] is "c"

    def fetch_transaction(self):
        """
        return transaction record.
        """
        return "transaction " + str(self.index) + " : " + self.data
