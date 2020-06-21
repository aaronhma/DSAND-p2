from hashlib import *
from time import time as curr_time


class Block:
    def __init__(self, data, previous_hash=None):
        self.timestamp = curr_time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.sep = "====================================================================="

    def calc_hash(self, data):
        sha = sha256()
        sha.update(data.encode("UTF-8"))

        return sha.hexdigest()

    def get_info(self):
        return self.data, self.previous_hash, self.hash, self.timestamp

    def print_info(self, print_prev_hash=True):
        if print_prev_hash:
            blockData, blockPrevHash, blockHash, blockTime = self.get_info()
            print(self.sep)
            print("The data of the block: {}".format(blockData))
            print("Previous block hash: {}".format(blockPrevHash))
            print("Current block hash: {}".format(blockHash))
            print("Block created at: {}".format(blockTime))
            print(self.sep)
        else:
            blockData, _, blockHash, blockTime = self.get_info()
            print(self.sep)
            print("The data of the block: {}".format(blockData))
            print("Current block hash: {}".format(blockHash))
            print("Block created at: {}".format(blockTime))
            print(self.sep)


class Blockchain:
    def __init__(self):
        self.data = None
        self.size_ = 0

    def add(self, data):
        if self.data == None:
            self.data = Block(data)
        else:
            self.data = Block(data, self.data)

        self.size_ += 1

    def print_data(self):
        self.data.print_info()

    def size(self):
        return self.size_


if __name__ == "__main__":
    print("[RUNNING] Running student tests.")
    blockchain = Blockchain()
    print(f"Blockchain size: {blockchain.size()}")
    test = ["udacity", "data structures", "algorithms",
            "grader", "tester", "python", "complete"]

    for i in test:
        blockchain.add(i)
        blockchain.print_data()
        print(f"Blockchain size: {blockchain.size()}")
    print("[PASS] Passed student tests!")
