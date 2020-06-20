import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
	    sha = hashlib.sha256()
	    hash_str = "We are going to encode this string of data!".encode('utf-8')
	    sha.update(hash_str)
	    return sha.hexdigest()


class BlockChain:

	head=None

	def __init__(self, block=None):
		self.data=block
		self.prev_trans=None



	def addBlock(self, transaction):
		try:
			if(self.head==None):
				self.head=BlockChain(Block(datetime.now(), transaction, 0))
			else:
				head_cpy=self.head
				self.head=BlockChain(Block(datetime.now(), transaction, head_cpy.data.hash))
				self.head.prev_trans=head_cpy
			return True
		except:
			return False


	# printing chain
	def printChain(self):
		trans_list=[]
		head_cpy=self.head

		while(head_cpy!=None):
			trans_list.append({
				"timestamp":head_cpy.data.timestamp,
				"data":head_cpy.data.data,
			})
			head_cpy=head_cpy.prev_trans
		trans_list=trans_list[::-1] # from starting trans to current

		return trans_list


	def get_curr_transaction(self):
		if(self.head==None):
			return None
		else:
			return self.head.data.data

	def check_validity_of_chain(self):
		try:
			if(self.head==None):
				return True # assuming empty chain as true
			head_cpy=self.head
			while(head_cpy.prev_trans!=None):
				if(head_cpy.data.previous_hash!=head_cpy.prev_trans.data.hash):
					return False
				head_cpy=head_cpy.prev_trans

			if(head_cpy.data.previous_hash==0):
				return True
			return False
		except:
			return False



# For Printing purposes
if __name__ == '__main__':
	start_trans=BlockChain()
	

	print("Pass" if True == start_trans.check_validity_of_chain() else "Fail")
	print("Pass" if None == start_trans.get_curr_transaction() else "Fail")
	print("Pass" if True == start_trans.addBlock(5) else "Fail")
	print("Pass" if True == start_trans.addBlock(25) else "Fail")
	print("Pass" if True == start_trans.addBlock(200) else "Fail")
	print("Pass" if True == start_trans.addBlock(15) else "Fail")
	print("Pass" if 15 == start_trans.get_curr_transaction() else "Fail")
	print("Pass" if True == start_trans.addBlock(10) else "Fail")
	print("Pass" if True == start_trans.addBlock(12) else "Fail")
	print("Pass" if 12 == start_trans.get_curr_transaction() else "Fail")


	
	print("\nBlock Chain Looks Like : \n")
	for trans in start_trans.printChain():
		print("     	    _____________________________________")
		print("	   | Date - {}	 |".format(trans['timestamp']))
		print("	   | Amount - {}		         ".format(trans['data']))
		print("	   |		       			 |")
		print(" 	    -------------------------------------")