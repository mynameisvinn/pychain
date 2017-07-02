import unittest
from PyBlockchain import Blockchain, Block, BaseBlock, Node

class Test_Blockchain(unittest.TestCase):
    """test module for learner
    """
    def setUp(self):
        """set up a blockchain with a single genesis block.
        """
        index = 0
        prev_hash = "hello"
        data = " World"
        curr_hash = "placeholder"

        self.genesis_block = Block(index, prev_hash, data, curr_hash)
        self.blockchain = Blockchain(self.genesis_block)


    def test_get_length(self):
        self.assertEqual(self.blockchain.get_length(), 1)

    def test_calc_hash_seal(self):
        """sha1("hello World11") will satisfy proof of work.
        """
        self.assertEqual(BaseBlock.calc_hash_seal(self.genesis_block), "11")

    def test_check_hash_validity(self):


if __name__ == "__main__":
    unittest.main()