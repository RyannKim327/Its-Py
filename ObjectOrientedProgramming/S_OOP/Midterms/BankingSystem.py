class BackAccount:
	def __init__(self, accountHolder: str, balance: int = 0):
		self._accountHolder = accountHolder
		self._balance = balance
	
	def getBalance(self):
		return self._balance
	
	def deposit(self, amount: int):
		self._balance += amount

# Start
if __name__ == "__main__":

	# Create 2 bank accounts
	acct1 = BackAccount("John Doe", 1000)
	acct2 = BackAccount("John Smith")

	print(f"{}")