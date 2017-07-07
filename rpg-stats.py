			

def load_classes_names(path = 'classes/'):
	import os
	import json
	result = []
	for filename in os.listdir(path):
		if not ('.json' in filename): continue
		_class = {}
		with open(path + filename, 'r') as file:
			_class = json.load(file)
		name = list(_class)[0]
		result.append(name)
	return result

def load_class(name, path = 'classes/'):
	import os
	import json
	with open(path + name.lower() + '.json', 'r') as file:
		_class = json.load(file)
	return _class[name]


def name(rpg):
	import requests
	import random
	from bs4 import BeautifulSoup
	url = 'https://www.fantasynamegen.com/human/short/'
	html = requests.get(url).content.decode('utf-8')
	soup = BeautifulSoup(html, 'html.parser')
	names = []
	for tag in soup.find_all('li'):
		if (tag.string != None): names.append(tag.string)
	return random.choice(names)
	
def gender(rpg):
	import random
	return random.choice(['Male', 'Female'])

def class_(rpg):
	import random
	return random.choice(load_classes_names())
	
def alignment(rpg):
	import random
	return random.choice(['Good', 'Neutral', 'Chaotic'])
	
def attributes(rpg):
	import random
	class_attributes = load_class(rpg._sheet['class'])['attributes']
	attributes = {}
	for key in class_attributes.keys():
		array = [int(s) for s in class_attributes[key].split(':')]
		value = random.choice(list(range(array[0], array[1]+1)))
		attributes[key] = value
	return attributes
	
def stats(rpg):
	import random
	class_stats = load_class(rpg._sheet['class'])['stats']
	stats = {}
	for key in class_stats.keys():
		array = [int(s) for s in class_stats[key].split(':')]
		value = random.choice(list(range(array[0], array[1]+1)))
		stats[key] = value
	return stats	
	
def inventory(rpg):
	import random
	class_inv = load_class(rpg._sheet['class'])['inventory']
	inventory = {}
	for key in class_inv.keys():
		if (':' in class_inv[key]):
			array = [int(s) for s in class_inv[key].split(':')]
			value = random.choice(list(range(array[0], array[1]+1)))
		else:
			value = class_inv[key].split(',')
		inventory[key] = value
	return inventory
	
class RPGSheet(object):

	def __init__(self, sheet):
		self._sheet = sheet
		self._generate()

	def _generate(self):
		for key in self._sheet.keys():
			if (callable(self._sheet[key])):
				self._sheet[key] = self._sheet[key](self)
				
	def _print(self):
		from pprint import pprint
		pprint(self._sheet)
	
"""

__main__

"""

my_sheet = {
	 'name': name
	,'gender' : gender
	,'class' : class_
	,'alignment' : alignment
	,'attributes' : attributes
	,'stats' : stats
	,'inventory' : inventory
	,'personality' : {
		'traits' : '',
		'ideals' : '',
		'bonds' : '',
		'flaws' : ''
	}
}
	
obj = RPGSheet(my_sheet)
obj._print()
