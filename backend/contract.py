from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
import json
from dotenv import load_dotenv
import os
load_dotenv()

w3 = Web3(Web3.HTTPProvider(
    # "https://eth-mainnet.g.alchemy.com/v2/nxxqffUPPvmfEVObac4QfFJi4pCDfzY9"))
    "https://eth-goerli.g.alchemy.com/v2/2_B3b5LLxt-f1PH-dSUPCQ0YdIlgSZRR"))
	
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


abi = json.loads("""[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "temp",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "humidity",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "hindex",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "pid",
				"type": "uint256"
			}
		],
		"name": "AddData",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "price",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "reqtemp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "manufacturing",
				"type": "string"
			}
		],
		"name": "AddProduct",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "temp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "humidity",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "heatindex",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "wid",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "pid",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "total_quantity",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "flag",
				"type": "bool"
			}
		],
		"name": "AddStatus",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "Data_list",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "temp",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "humidity",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "hindex",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "pid",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "data",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "temp",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "humidity",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "hindex",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "pid",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "getProductData",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "temp",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "humidity",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "hindex",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "pid",
						"type": "uint256"
					}
				],
				"internalType": "struct Supplychain.Data[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			}
		],
		"name": "getProductStatus",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "location",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "temp",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "humidity",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "heatindex",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "w_id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "p_id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "total_quantity",
						"type": "uint256"
					},
					{
						"internalType": "bool",
						"name": "flag",
						"type": "bool"
					}
				],
				"internalType": "struct Supplychain.Status[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getProducts",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "price",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "reqtemp",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "manufacturing",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					}
				],
				"internalType": "struct Supplychain.Product[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getWorkerssList",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "id",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					}
				],
				"internalType": "struct Supplychain.Worker[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "productStatus",
		"outputs": [
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "temp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "humidity",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "heatindex",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "w_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "p_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "total_quantity",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "flag",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "product_Status",
		"outputs": [
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "temp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "humidity",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "heatindex",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "w_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "p_id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "total_quantity",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "flag",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "products",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "price",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "reqtemp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "manufacturing",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "products_list",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "price",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "reqtemp",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "manufacturing",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			}
		],
		"name": "setWorker",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "workers",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "workers_list",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]""")

#key = os.getenv("RINKEBY_KEY")
key = "0b3cd7854ea5df6acf543fa40acd816570de2166178c695d3c14e51f4ea8e853"
print(key)# private key account
account = w3.toChecksumAddress(
    '0xEd19Cf6e48eF333d742dc5E4A051789b0995158e')  # account


address = w3.toChecksumAddress('0x297873aa7ca257e7a9487153ca77fdc7f3f7e0cc')
    #'0xFa56954976bA7d616945c09A7e360499e7038d98')  # contrat address
deployed_contract = w3.eth.contract(address=address, abi=abi)

print(deployed_contract.functions.getWorkerssList().call())


def setWorker(name):
  transaction = deployed_contract.functions.setWorker(name).buildTransaction({'from': account})
  transaction.update({'nonce': w3.eth.get_transaction_count(account)})
  signed_tx = w3.eth.account.sign_transaction(transaction, key)
  txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
  txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
  print(txn_receipt)
  return "worker added"


def AddProduct(name, price, description, reqtemp,manufacturing):
  transaction = deployed_contract.functions.AddProduct(name, price, description, reqtemp,manufacturing).buildTransaction({'from': account})
  transaction.update({'nonce': w3.eth.get_transaction_count(account)})
  signed_tx = w3.eth.account.sign_transaction(transaction, key)
  txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
  txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
  print(txn_receipt)
  return "product added"


def AddStatus(location, temp,humidity,heatindex, wid, pid,total_quantity,flag):
  transaction = deployed_contract.functions.AddStatus(location, temp, humidity, heatindex, wid, pid, total_quantity,flag).buildTransaction({'from': account})
  transaction.update({'nonce': w3.eth.get_transaction_count(account)})
  signed_tx = w3.eth.account.sign_transaction(transaction, key)
  txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
  txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
  print(txn_receipt)
  return "status added"

def AddData( temp,humidity,heatindex, pid):
  transaction = deployed_contract.functions.AddData(temp, humidity, heatindex, pid).buildTransaction({'from': account})
  transaction.update({'nonce': w3.eth.get_transaction_count(account)})
  signed_tx = w3.eth.account.sign_transaction(transaction, key)
  txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
  txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
  print(txn_receipt)
  return "sensor data added"

def  getProductsList():
    
    return deployed_contract.functions.getProductsList().call()

def getWorkersList():
   return deployed_contract.functions.getWorkerssList().call()

def getProductStatus(pid):
   return deployed_contract.functions.getProductStatus(pid).call()

def getProductData(pid):
    return deployed_contract.functions.getProductData(pid).call()

def getProducts():
    return deployed_contract.functions.getProducts().call()
    


    