from time import time
import json
import hashlib
from urllib.parse import urlparse

import requests


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], time())
        genesis_block.prev = 'none'
        genesis_block.hash = genesis_block.calculate_hash()
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if len(self.chain) > 0:
            block.prev = self.get_last_block().hash
        else:
            block.prev = 'none'
        self.chain.append(block)

    def new_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return self.get_last_block().index + 1

    # proof of work algorithm
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()  # last_proof - hash of last block
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'

    def mine_block(self):
        last_block = self.get_last_block()
        last_proof = last_block.hash
        proof = self.proof_of_work(last_proof)

        block = Block(len(self.chain), self.current_transactions, time())
        block.prev = last_block.hash
        block.hash = block.calculate_hash()

        self.current_transactions = []
        self.add_block(block)
        return block

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    # consensus algorithm
    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['prev'] != last_block['hash']:
                return False

            if not self.valid_proof(last_block['hash'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None
        max_length = len(self.chain)

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False


class Block(object):
    def __init__(self, index, transactions, time):
        self.index = index  # block number
        self.transactions = transactions  # transaction data
        self.time = time  # time of transaction
        self.prev = ''  # hash of prev block
        self.hash = self.calculate_hash()  # hash of block

    def calculate_hash(self):
        hash_transactions = ''.join(transaction.hash for transaction in self.transactions)
        hash_string = str(self.time) + hash_transactions + self.prev + str(self.index)
        hash_encoded = json.dumps(hash_string, sort_keys=True).encode()
        return hashlib.sha256(hash_encoded).hexdigest()

    def __repr__(self):
        transactions_repr = [repr(transaction) for transaction in self.transactions]
        return f"Block(index={self.index}, transactions={transactions_repr}, time={self.time}, prev={self.prev}, hash={self.hash})"


class Transaction(object):
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.time = time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_string = self.sender + self.receiver + str(self.amount) + str(self.time)
        hash_encoded = json.dumps(hash_string, sort_keys=True).encode()
        return hashlib.sha256(hash_encoded).hexdigest()

    def __repr__(self):
        return f"Transaction(sender={self.sender}, receiver={self.receiver}, amount={self.amount}, time={self.time}, hash={self.hash})"
