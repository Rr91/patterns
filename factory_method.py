# factory_method.py
from abc import ABC, abstractmethod


class Farmer(ABC):
	@abstractmethod
	def getPetForThisOperation(self):
		pass

	def worked(self):
		product = self.getPetForThisOperation()
		return product.getProduct()



class Milked(Farmer):
	def getPetForThisOperation(self):
		return Cow()

class Egged(Farmer):
	def getPetForThisOperation(self):
		return Chiken()


class Pets(ABC):
	@abstractmethod
	def getProduct(self):
		pass 


class Cow(Pets):

	def getProduct(self):
		return self.getMilk()

	def getMilk(self):
		return "Cow give milk";


class Chiken(Pets):

	def getProduct(self):
		return self.getEgg()

	def getEgg(self):
		return "Chiken give egg"


if __name__ == "__main__":
	worker1 = Milked()
	print(worker1.worked())
	worker2 = Egged()
	print(worker2.worked())