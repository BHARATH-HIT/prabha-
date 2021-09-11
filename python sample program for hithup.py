import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):    #constructor
        self.chain = []
        self.pending_transactions = []

        self.new_block(pervious_hash = "Previous hash",proof=100)

    
    #FUNCTION TO CREATE NEW BLOCKS
    def new_block(self,proof,pervious_hash=None):
        #Dictionary
        block = {
        'index': len(self.chain)+1,
        'timestramp': time(),
        'transactions': self.pending_transactions,
        'proof': proof,
        'pervious_hash':pervious_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions = []
        self.chain.append(block)
        ##just for checking purpose
        #for i in self.chain:
            #print(i)

    #function to return the last block
    @property
    def last_block(self):
        return self.chain[-1]

    #To create new transaction
    def new_transaction(self,sender,recipiant,amount):
        transaction={
            'sender':sender,
            'recipiant':recipiant,
            'amount':amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index']+1

    #Hashing the blocks
    def hash(self,block):

        #json converts the the dictionary to vaild json string
        string_object=json.dumps(block,sort_keys=True)
        block_string=string_object.encode()
        raw_hash=hashlib.sha256(block_string)
        #to convert the hashed data to hexadecimal string
        hex_hash=raw_hash.hexdigest()
        return hex_hash

blockchain = Blockchain()
t1 = blockchain.new_transaction("ravi","theja","2.5BTC")
t2= blockchain.new_transaction("vijay","guna",'5BTC')
blockchain.new_block(12345) #12345 is the confirmation
t3 = blockchain.new_transaction("shri","sahana",'3BTC')
t4 = blockchain.new_transaction("sahana","shri","10BTC")
blockchain.new_block(3488)
#printing the created blockchain
for i in blockchain.chain:
    print(i)
