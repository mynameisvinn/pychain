def show(Block):
    print ">>> block hash:", Block.block_hash
    print ">>> block index:", Block.index
    print ">>> previous block hash:", Block.prev_hash
    print ">>> root hash:", Block.root_hash
    print ">>> nonce: ", Block.nonce
    print ">>> transactions", Block.ls_transactions