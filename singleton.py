# singleton.py

class Cache():
	__create_key = object()
	def __init__(self, create_key):
		assert(create_key == Cache.__create_key), \
            "OnlyCreatable objects must be created using Cache.create"
		self.current = 0
	
	@staticmethod
	def instance(self):
		return Cache(Cache.__create_key)

	def addCache(self, data):
		self.current += 1
		file_action = FileAction('{}.txt'.format(self.current))
		file_action.write(data)

	def getCache(self):
		file_action = FileAction('{}.txt'.format(self.current))
		return file_action.read()


class FileAction():
	def  __init__(self, filename):
		self.filename = filename

	def write(self, data):
		with open(self.filename, 'w') as filedata:
			filedata.write(str(data))

	def read(self):
		with open(self.filename) as filedata:
			return filedata.read()

if __name__ == "__main__":
	cache = Cache.instance(0)
	print(cache.addCache(5555))
	print(cache.addCache(666))
	print(cache.getCache())