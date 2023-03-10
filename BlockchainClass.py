import hashlib
import json
import datetime

class Blockchain :
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash= "0", data="new transaction")
       
              
    def create_block(self, proof, previous_hash, data):
        new_block = {
                        'index': len(self.chain) + 1,
                        'timestamp': datetime.datetime.now(),
                        'proof': proof,
                        'previous_hash': previous_hash,
                        'data': data
                    }

        self.chain.append(new_block)
        return new_block

    
    def get_previous_block(self):
        return self.chain[-1]
    
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True, default=str).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            proof = block['proof']
            previous_proof = previous_block['previous_hash']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:4] != "0000":
                return False
            
            previous_block = block
            block_index += 1
            
        return True 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        