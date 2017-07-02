# pyblockchain
bare bones blockchain implemented in python.

this project hopes to educate through simple to read python code. the attached notebook simulates a typical blockchain process:

1. **transaction** is recorded by a **node**
2. a **miner** calculates an acceptable **hash**, thus demonstrating **proof of work**
3. transaction is added to **blockchain**

of course, the devil is in the details, and to truly understand blockchains, id suggest digging through step 2 (see `miner.py`). blockchain, as a concept, clicked for me when i understood why demonstrating proof-of-work was important.

## todo
- [ ] how do nodes broadcast updated ledgers?
- [ ] more unit tests, especially for proof of work