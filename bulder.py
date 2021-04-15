# bulder.py
from abc import ABC, abstractmethod, abstractproperty
class ABuilder(ABC):
	@abstractproperty
	def getObj(self):
		pass

	@abstractmethod
	def printObj(self):
		pass


class BuilderCar(ABuilder):
	@property
	def getObj(self):
		self.getCar()

	def getCar(self):
		self.car = Car()

	def printObj(self):
		self.car.printMyself()

	def addBolid(self):
		self.car.add('Bolid')

	def addEngine(self):
		self.car.add('Engine')


class BuilderComputer(ABuilder):
	@property
	def getObj(self):
		self.getComputer()

	def getComputer(self):
		self.computer = Computer()

	def printObj(self):
		self.computer.printMyself()


	def addMouserbord(self):
		self.computer.add('Mouserbord')

	def addProcessor(self):
		self.computer.add('Processor')

	def addMemory(self):
		self.computer.add('Memory')
	
	def addPowerblock(self):
		self.computer.add('Powerblock')
		
	def addBody(self):
		self.computer.add('Body')
		
	def addFan(self):
		self.computer.add('Fan')


		
class Car():
	def __init__(self):
		self.details = []

	def add(self, detail):
		self.details.append(detail)

	def printMyself(self):
		res = ', '.join(self.details)
		print("Your present - This Car consists of {}".format(res))



class Computer():
	def __init__(self):
		self.accessories = []

	def add(self, accessor):
		self.accessories.append(accessor)

	def printMyself(self):
		res = ', '.join(self.accessories)
		print("Your present - This Computer consists of {}".format(res))


class Assembler:
	range_balance = { 'min':500, 'avg':1500,  'max': 10000 }
	
	def runBuild(self, client_balance):
		client_balance = int(client_balance)
		self.result_set = []

		if client_balance >= self.range_balance['min'] and client_balance < self.range_balance['avg']:
			self.result_set.append(self.assembling_min_computer())
		
		elif client_balance >= self.range_balance['avg'] and client_balance < self.range_balance['max']:
			self.result_set.append(self.assembling_big_computer())

		elif client_balance >= self.range_balance['max']:
			self.result_set.append(self.assembling_car())
			# self.result_set.append(self.assembling_big_computer())

		else:
			raise Exception('nothing to offer!')
		
		for item in self.result_set:
			item.printObj()


	def assembling_car(self):
		bulder = BuilderCar()
		bulder.getCar();
		bulder.addBolid();
		bulder.addEngine();
		return bulder

	def assembling_min_computer(self):
		bulder = BuilderComputer()
		bulder.getComputer();
		bulder.addMouserbord();
		bulder.addProcessor();
		bulder.addMemory();
		bulder.addPowerblock();
		return bulder
		
	def assembling_big_computer(self):
		bulder = BuilderComputer()
		bulder.getComputer();
		bulder.addMouserbord();
		bulder.addProcessor();
		bulder.addMemory();
		bulder.addPowerblock();
		bulder.addBody();
		bulder.addFan();
		bulder.addFan();
		return bulder
		

if __name__ == "__main__":

	shop = Assembler() 
	shop.runBuild(input('Your balance - '))
