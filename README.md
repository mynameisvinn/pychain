# pyblockchain
bare bones blockchain implemented in python.

this project hopes to educate through simple to read python code. the attached notebook simulates a typical blockchain process:

1. **transaction** is recorded by a **node**
2. a **miner** calculates an acceptable **hash**, thus demonstrating **proof of work**
3. transaction is added to **blockchain**

of course, the devil is in the details, and to truly understand blockchains, id suggest digging through step 2 (see `miner.py`). blockchain, as a concept, clicked for me when i understood why demonstrating proof-of-work was important.

# faqs
## decentralized database or journal?
a blockchain is the journal of a decentralized database, not the database itself. as on the blockchain, only the history of updates are kept. in order to recover the database, you will have to scan through the entire chain and perform each update one by one.

## who maintains the blockchain?
no one. there's no central machine or authority keeping track of things. instead, the blockchain is stored across thousands of machines on the internet (in various states), and the system works with nobody in charge. amazing.

## why is proof of work/mining so important?
once every 10 min, a block is given a "seal". this seal is a hash that satisfies a specific set of conditions and is purposely designed to be difficult to generate. by making it computationally expensive to mine a block, it becomes nearly impossible for any single machine/node/entity to rewrite a blockchain.

Proof of work (PoW) is a clever application of hash functions. It works by calculating the hash of a message, along with many different nonces, until you find a resulting digest that meets a rare criteria. Since each hash is equally unlikely to meet that criteria, specifying a hard-to-meet criteria (perhaps a hash that starts with several leading 0s) is a way to prove that someone spent their CPU cycles. Also, a correct solution will be trivial to verify.

The main property of proof-of-work is that it requires a tremendous amount of computation to create, yet very little computation to validate. Each block in the Bitcoin blockchain requires proof-of-work and all the computing power in the world dedicated to doing this takes roughly 10 minutes to find. This means that to create an alternate version of the blockchain would cost the same amount of computing power.

## how do nodes broadcast updated ledgers?
whenever a new block is added, a node will broadcast this update to its 8+ neighbors. this is why the blockchain is viewed as an eventually consistent, append-only, database/ledger of all transactions.

# todo
[ ] implement merkle tree for transactions (http://www.righto.com/2017/07/bitcoin-mining-on-vintage-xerox-alto.html)

# reference
* [blockchain](https://hackernoon.com/wtf-is-the-blockchain-1da89ba19348)