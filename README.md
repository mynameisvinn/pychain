# pyblockchain
bare bones blockchain implemented in python.

this project hopes to educate through simple to read python code. the attached notebook simulates a typical blockchain process:

1. **transaction** is recorded by a **node**
2. a **miner** calculates an acceptable **hash**, thus demonstrating **proof of work**
3. transaction is added to **blockchain**

of course, the devil is in the details, and to truly understand blockchains, id suggest digging through step 2 (see `miner.py`). blockchain, as a concept, clicked for me when i understood why demonstrating proof-of-work was important.

# faqs
## who maintains the blockchain?
there's no central machine or authority keeping track of things. instead, the blockchain is stored across thousands of machines on the internet (in various states), and the system works with nobody in charge. amazing.

## why is mining so important?
once every 10 min, a block is given a "seal". this seal is a hash that satisfies a specific set of conditions and is purposely designed to be difficult to generate. by making it computationally expensive to mine a block, it becomes nearly impossible for any single machine/node/entity to rewrite a blockchain.

## how do nodes broadcast updated ledgers?
whenever a new block is added, a node will broadcast this update to its 8+ neighbors. this is why the blockchain is viewed as an eventually consistent, append-only, database/ledger of all transactions.

# todo
[ ] implement merkle tree for transactions (http://www.righto.com/2017/07/bitcoin-mining-on-vintage-xerox-alto.html)