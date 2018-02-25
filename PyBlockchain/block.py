from hashlib import sha256

def calculate_hash(concatenated_message):
    """calculate hash.
    """
    return sha256(concatenated_message.encode('utf-8')).hexdigest()


class Block(object):
    """
    a blockchain is composed of blocks. each block is represented by a 
    block header. 

    each block headher is then represented with a block hash. a block 
    hash is composed of the hash of the (a) previous block hash, (b) a
     root hash, and (c) a nonce (to be calculated by a miner).
    """
    def __init__(self, ls_transactions):
        self.index = 0
        self.prev_hash = "0"
        self.ls_transactions = ls_transactions
        self.block_hash = "0"  # calculated by miner
        self.nonce = 0

    @property
    def root_hash(self):
        """calculate root hash, as part of a merkle tree.

        each Block has a list of entries. every two entries are 
        concatenated together and hashed. each hash is then concatenated
        with another hash, and recursively hashed until there is a single
        root hash.
        """
        self._balance_tree()  # trees must have even n_entries for root hash

        q = self.ls_transactions.copy()

        # recursively calculate hashes until there is a single entry
        while len(q) > 1:
            a = q.pop(0)
            b = q.pop(0)
            c = calculate_hash(a + b)
            q.append(c)
        return q[0]

    def _balance_tree(self):
        """
        make sure trees have an even number of entries. if number of 
        entries is odd, duplicate last entry.
        """
        n_entries = len(self.ls_transactions)
        if n_entries % 2 == 1:
            self.ls_transactions.append(self.ls_transactions[n_entries - 1])