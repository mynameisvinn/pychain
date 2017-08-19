from .baseblock import BaseBlock

class Miner(BaseBlock):
    def __init__(self):
        pass

    def update_block_hash(self, unverified_block, valid_hash_block):
        """
        parameters
        ----------
        unverified_block : Block object
            unverified block, whose hash block will be updated by miner.
        valid_hash_block : str
            a hash that demonstrates proof of work.
        """
        unverified_block.block_hash = valid_hash_block
