"""Base classes for all objects."""

from hashlib import sha256

class BaseBlock(object):
    """base block"""

    @staticmethod
    def calculate_hash_block(unverified_block):
        """
        a nonce "seals" a block to the blockchain. 

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
        
        while not BaseBlock.is_proof_of_work(block_hash):
            unverified_block.nonce += 1  # increment until block hash is satisfactory
            msg = unverified_block.prev_hash + unverified_block.root_hash + str(unverified_block.nonce)
            block_hash = BaseBlock.generate_block_hash(msg)
        return block_hash

    @staticmethod
    def generate_block_hash(message):
        return sha256(message).hexdigest()

    @staticmethod
    def is_proof_of_work(hash_block):
        """
        in this toy example, a valid block hash will start with 0. this condition
        is known as "proof of work."

        parameter
        ---------
        hash_block : str
            representing hex digest

        returns
        -------
        boolean, whether hash_output is acceptable or not.
        """
        return hash_block[0] is "0"
