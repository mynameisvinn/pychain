"""
miner object
"""
from block import Block

class Miner(object):
    """
    minor object.
    """
    def __init__(self):
        pass

    @staticmethod
    def update_hash(new_block, correct_hash):
        """
        helper function. a miner should update the block with the correct seal, not the
        block itself.
        """
        print ">>> updating hash for block", new_block.index
        new_block.update_hash(correct_hash)


    @staticmethod
    def calc_hash_seal(some_block):
        """
        cryptographic hash function are difficult to reverse, thus the input
        value of a hash function cant be determined from its output value.

        in the case of blockchain, a hash is the "seal" that finalizes the addition
        of a block to the entire ledger.

        we do not want this seal function to be easy to compute. if it was, then a bad actor could
        theoretically alter past blocks and reseal it.

        to make this sealing/hashing function difficult, a seal must satisfy the following
        condition. a seal, when "mixed" with the block's id number, must result in an output that
        has three zeros. since this is a NP hard problem (very difficult to find a seal that
        satisfies that output, but easy to verify), this is an acceptable "proof of work".

        in order to generate an acceptable seal ("proof of work"), a miner will randomly mutate
        until it satisfies conditions.

        parameters:
        -----------
        some_block : Block object
        data : some new record

        returns:
        --------
        seal: str
            representing hash of new block.
        """
        initial_input = some_block.prev_hash + some_block.data
        initial_hash = Block._hashhash(initial_input)
        seal = ""
        while not Block._proof_of_work(initial_hash):
            initial_input += "1"  # append 1 to the hash until it satisfies hash conditions
            seal += "1"
            initial_hash = Block._hashhash(initial_input)
        return seal
