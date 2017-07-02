"""tests"""
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
        new_data = "dummy"

        self.genesis_block = Block(index, prev_hash, data, curr_hash)
        self.blockchain = Blockchain(self.genesis_block)
        self.my_node = Node(self.blockchain)
        self.new_block = self.my_node.generate_new_block(new_data)

    def test_get_length(self):
        self.assertEqual(self.blockchain.get_length(), 1)

    def test_calc_hash_seal(self):
        """sha1("hello World11") will satisfy proof of work.
        """
        self.assertEqual(BaseBlock.calc_hash_seal(self.genesis_block), "11")

    def test_check_hash_validity(self):
        """new blocks are always rejected until a miner can calculate the
        correct sealing hash.
        """
        self.assertEqual(self.my_node.check_block(self.new_block), False)


if __name__ == "__main__":
    unittest.main()
