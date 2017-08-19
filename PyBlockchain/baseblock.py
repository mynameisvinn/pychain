"""Base classes for all objects."""

from hashlib import sha1

class BaseBlock(object):
    """base block"""

    @staticmethod
    def calculate_hash_block(unverified_block):
        """
        a nonce "seals" a block to the blockchain.

        we do not want this seal function to be easy to compute. if it was,
        then a bad actor could theoretically alter past blocks and reseal it.

        to make this sealing/hashing function difficult, a seal must satisfy
        the following condition. a seal, when "mixed" with the block's data,
        must result in an output that has three zeros. since this is a NP hard
        problem (difficult to find a seal that satisfies that output, but easy
        to verify), this is an acceptable "proof of work".

        in order to generate an acceptable seal ("proof of work"), a miner
        may examine 1000000s of random combindations until a hash is considered
        acceptable.

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
        msg = unverified_block.prev_hash + unverified_block.data + str(unverified_block.nonce)
        hash_block = BaseBlock.hash_block(msg)
        
        # increment nonce by 1 until hash block satisfies proof of work condition
        while not BaseBlock.proof_of_work(hash_block):
            unverified_block.nonce += 1
            msg = unverified_block.prev_hash + unverified_block.data + str(unverified_block.nonce)
            hash_block = BaseBlock.hash_block(msg)
        return hash_block

    @staticmethod
    def hash_block(message):
        """use sha1, which returns a 160 bit hash. in practice this is sha256.
        """
        return sha1(message).hexdigest()

    @staticmethod
    def proof_of_work(hash_block):
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
