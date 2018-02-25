"""Base classes for all objects."""

from hashlib import sha256

class BaseBlock(object):
    """base block"""

    @staticmethod
    def calculate_hash_block(unverified_block):
        """calculate hash for a new block. 

        a block cannot be added to the chain until an acceptable hash (aka nonce)
        has been identified. in that sense, a nonce "seals" a block to the 
        blockchain.

        a miner will keep guessing nonces until resulting block hash is valid. if
        the hash function is well designed (sha256), there is no better strategy
        than incrementing nonces by one and then checking block hash validy.

        parameters
        ----------
        unverified_block : Block object
            refers to a block that has not yet been added to the blockchain. we
            will generate an acceptable block hash for new block.

        returns
        -------
        block_hash: hash
            representing hash of new block, satisfying proof of work conditions.
        """

        msg = unverified_block.prev_hash + unverified_block.root_hash + str(unverified_block.nonce)
        block_hash = BaseBlock.generate_block_hash(msg)
        
        # keep guessing nonce until resulting block hash is valid
        while not BaseBlock.is_proof_of_work(block_hash):
            unverified_block.nonce += 1  # increment until block hash is satisfactory
            msg = unverified_block.prev_hash + unverified_block.root_hash + str(unverified_block.nonce)
            block_hash = BaseBlock.generate_block_hash(msg)
        return block_hash

    @staticmethod
    def generate_block_hash(message):
        return sha256(message.encode('utf-8')).hexdigest()

    @staticmethod
    def is_proof_of_work(hash_block):
        """Verify validity of block hash.

        in this toy example, a valid block hash starts with 0. this 
        condition is known as "proof of work.". it is the miner's job 
        to guess nonce's (eg simply incrementing nonce by 1) until 
        the resulting block hash is valid.

        parameter
        ---------
        hash_block : str
            representing hex digest

        returns
        -------
        boolean, whether hash_output is acceptable or not.
        """
        return hash_block[0] is "0"
