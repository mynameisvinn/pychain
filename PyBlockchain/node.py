"""
define nodes, which create blocks.
"""
from .block import Block
from .baseblock import BaseBlock

###############################################################################
class Node(BaseBlock):
    """node class"""
    def __init__(self, blockchain):
        self.blockchain_copy = blockchain

    def update_blockchain(self, new_block):
        """
        a node can add a new block to a block as long it is validated.
        """
        if self.check_block(new_block):
            print ">>> successfully updated blockchain..."
            self.blockchain_copy.add_block(new_block)
            return True
        else:
            print ">>> update failed"
            return False

    def get_prev_block(self):
        """returns most recent block object in blockchain.
        """
        idx = self.blockchain_copy.get_length() - 1
        return self.blockchain_copy.get_block(idx)

    def generate_new_block(self, new_data):
        """
        given a new record and an existing blockchain, this function will create
        a new block.

        an existing blockchain is required because block formation depends on
        most recent block.

        a block chain chain can be traced all the way back to the very first
        block created. as such, the blockchain contains an un-editable record of
         all the transactions made.

        parameters
        ----------
        new_data : str
            representing data, transaction, record, etc.

        returns
        -------
        a new Block object.
        """
        prev_block = self.get_prev_block()
        new_index = prev_block.index + 1
        prev_hash = prev_block.curr_hash
        new_hash = "-- placeholder hash --"
        return Block(new_index, prev_hash, new_data, new_hash)


    def check_block(self, new_block):
        """
        a block must satisfy the following conditions before it is added to
        blockchain:

        (1) index must be in order;
        (2) hash sequence must be in order;
        (3) hash/seal must be valid, given previous block's hash and current
        block's data

        parameters:
        -----------
        new_block : Block object
            block to be added to blockchain.

        returns:
        --------
        boolean
        """
        prev_block = self.get_prev_block()
        index_check = Node._check_index(new_block, prev_block)
        hash_seq_check = Node._check_hash_sequence(new_block, prev_block)
        hash_valid_check = self._check_hash_validity(new_block)

        print ">>> checking index...", index_check
        print ">>> checking hash sequence...", hash_seq_check
        print ">>> checking hash validity...", hash_valid_check

        return index_check & hash_seq_check & hash_valid_check

    @staticmethod
    def _check_index(new_block, prev_block):
        return new_block.index == prev_block.index + 1

    @staticmethod
    def _check_hash_sequence(new_block, prev_block):
        return new_block.prev_hash == prev_block.curr_hash

    def _check_hash_validity(self, new_block):
        return self.calc_hash_seal(new_block) == new_block.curr_hash
