import json
import hashlib
import os
from datetime import datetime


def writeBlock(name, birthday, amount, previousHash):
	blockchainDir = os.curdir + '/blockchain/'
	dateTime = datetime.today().timestamp()
	data = {'name':name,
			'birthday':birthday,
			'amount':amount,
            'date':dateTime,
            'hash':previousHash}
	with open(blockchainDir + str(dateTime), 'w') as block:
                json.dump(data, block, indent=4, ensure_ascii = False)
	
def readHashFromBlock(file):
	blockchainDir = os.curdir + '/blockchain/'
	blockHash = json.load(open(blockchainDir + file))['hash']
	return blockHash
	
def getHash(file):
	blockchainDir = os.curdir + '/blockchain/'
	block = open(blockchainDir + file, 'rb').read()
	blockHash = hashlib.md5(block).hexdigest()
	return blockHash
	
def createBlock(name, birthday, amount):
	blockchainDir = os.curdir + '/blockchain/'
	files = os.listdir(blockchainDir)
	if len(files) == 0 :
		writeBlock(blockchainDir)
	else :
		listOfBloks = sorted([float(i) for i in files])
		previousHash = getHash(str(listOfBloks[-1]))
		writeBlock(name, birthday, amount, previousHash)		

def compareBlocks(previousHash, blockHash):
	if previousHash == blockHash :
		return True
	else :
		return False
		
def checkBlockChain():
	blockchainDir = os.curdir + '/blockchain/'
	files = os.listdir(blockchainDir)
	listOfBloks = sorted([float(i) for i in files])
	sizeOfChain = len(listOfBloks)
	for block in listOfBloks[1:sizeOfChain]:
		indexOfBlock = listOfBloks.index(block)
		previousHash = getHash(str(listOfBloks[indexOfBlock - 1]))
		blockHash = readHashFromBlock(str(block))
		result = compareBlocks(previousHash, blockHash)
		if result :
			print("Block " + str(block) + " - OK")
		else :
			print("Block " + str(block) + " - ERROR")
		
		
		
def main():
	name = 'ivan'
	birthday = '22.03.89'
	amount = 65
	createBlock(name, birthday, amount)
	checkBlockChain()

if __name__ == '__main__' :
	main()

