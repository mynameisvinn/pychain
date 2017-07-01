class BaseBlock(object):
    def __init__(self):
        pass

    def get_prev_block(self, blockchain):
        """
        returns most recent block object in blockchain. called by generate_new_block().
        """
        return blockchain[len(blockchain) - 1]