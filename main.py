from BlockchainClass import *
from flask import Flask, jsonify
from json import *


blockchain = Blockchain()

app = Flask("My first Blockchain App")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

#Routes
@app.route('/mine_new_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    data = "New transaction added"

    new_block = blockchain.create_block(proof, previous_hash, data)
    
    response = jsonify({'index': new_block['index'],
                        'timestamp': new_block['timestamp'],
                        'previous_hash': new_block['previous_hash'],
                        'proof': new_block['proof'],
                        'data': new_block['data']
                        })
    return response, 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = jsonify({'status': "success",
                        'chain': blockchain.chain,
                        'length': len(blockchain.chain)})
    return response, 200


@app.route('/check_chain', methods=['GET'])
def check_valid_chain():
    isValid = blockchain.is_chain_valid(blockchain.chain)

    if isValid is True:
        statusCode = "Blockchain is valid"
    else:
         statusCode = "Blockchain is invalid"

    response = jsonify({
        'status': "success",
        'Chain Status': statusCode
    })

    return response, 200


app.run(host='127.0.0.1', port = 5001)
print("server running")