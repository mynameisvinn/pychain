import unittest
from PyBlockchain import Blockchain

class Test_Blockchain(unittest.TestCase):
    """test module for learner
    """
    def setUp(self):
        """
        create an instance of learner to be tested
        """
        genesis_block = "A"
        self.blockchain = Blockchain(genesis_block)

    def test_get_length(self):
        """test
        """
        self.assertEqual(self.blockchain.get_length(), 1)

if __name__ == "__main__":
    unittest.main()