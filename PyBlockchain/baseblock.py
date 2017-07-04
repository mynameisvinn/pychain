"""Base classes for all objects."""

from hashlib import sha1

class BaseBlock(object):
    """base block"""

    @staticmethod
    def calc_hash_seal(new_block):
        """
        cryptographic hash function are difficult to reverse, thus the input
        value of a hash function cant be determined from its output value.

        in the case of blockchain, a hash is the "seal" that finalizes the
        addition of a block to the entire ledger.

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
        new_block : Block object
            refers to a block that has not yet been added to the blockchain. we
            will generate an acceptable hash.

        returns
        -------
        seal: str
            representing hash of new block. satisfies proof of work.
        """
        initial_input = new_block.prev_hash + new_block.data
        initial_hash = BaseBlock.hash_block(initial_input)
        seal = ""
        while not BaseBlock.proof_of_work(initial_hash):
            initial_input += "1"  # append 1 until it satisfies hash conditions
            seal += "1"
            initial_hash = BaseBlock.hash_block(initial_input)
        return seal

    @staticmethod
    def hash_block(message):
        """use sha1, which returns a 160 bit hash. in practice this is sha256.
        """
        return sha1(message).hexdigest()

    @staticmethod
    def proof_of_work(hash_output):
        """
        in practice, a hash/seal must begin with three zeros in order to be
        considered valid. 

        in this example, a valid hash/seal (or proof of work) will have "c" as 
        its 0th element.

        parameter
        ---------
        hash_output : str
            representing hex digest

        returns
        -------
        boolean, whether hash_output is acceptable or not.
        """
        return hash_output[0] is "c"
