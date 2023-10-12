class Student:
	def __init__(self, student: dict):
		self.__id__ = student['ID']
		self.__student__ = student['studentName']
	
	def getStudentName(self):
		print(self.__student__)

	def getStudentID(self):
		print(self.__id__)

class Librarian:
	def __init__(self, librarian: dict):
		self.__id__ = librarian['ID']
		self.__name__ = librarian['name']
		self.__password__ = librarian['password']

	def getName(self):
		return self.__name__
	
	def getPassword(self):
		return self.__password__

class Books:
	def __init__(self, book: dict):
		self.__id__ = book['ID']
		self.__name__ = book['title']
		self.__author__ = book['author']
		self.__publisher__ = book['publisher']
		self.__date__ = book['date']
		self.__isBorrowed__ = book['isBorrowed']
	
	def  getBookName(self):
		return self.__name__
	
	def canBorrow(self):
		return self.__isBorrowed__
	
	def doBorrow(self):
		self.__isBorrowed__ = not _i