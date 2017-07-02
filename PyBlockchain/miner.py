"""miner object"""

from .baseblock import BaseBlock

class Miner(BaseBlock):
    """minor object."""
    def __init__(self):
        pass

    @staticmethod
    def update_hash(new_block, correct_hash):
        """
        a miner updates the Block object with the correct hash.

        parameters
        ----------
        new_block : Block object
            miner will update this Block's hash
        correct_hash : str
            correct_hash for a specific Block. when reconstructed with the
            Block's data, it would demonstrate proof of work.
        """
        new_block.update_hash(correct_hash)
