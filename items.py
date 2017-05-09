from location import *

class item(object):

	name = "defaultItem"
	traversable = True
	weight = 0

	def __init__(self):
		None

	def getTraversable(self):
		return self.traversable

	def setTraversable(self, boolean):
		self.traversable = boolean

class sword(item):

	name = "sword"
	weight = 10
	damage = 2

	def __init__(self):
		None

class armor(item):

	name = "armor"
	weight = 12
	armor = 2

	def __init__(self):
		None

