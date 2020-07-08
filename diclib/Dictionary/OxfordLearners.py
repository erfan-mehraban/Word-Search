""" Dictionary: Oxford Learner's Dictionary """
from .. import dicTypes

def OEDParser(soup, bWithExample):
	""" The parser of Oxford Learner's Dictionary. """
	rep = dicTypes.Result(bWithExample)
	
	# Top part
	if soup.find('div', class_='top-g')!=None:
		for txt in soup.find('div', class_='top-g').find_all('span', class_='xr-gs'):
			rep.defs.append([txt.get_text()])
			
			if bWithExample:
				rep.examples.append([])
	
	# Middle part
	defs = soup.find_all(class_=['sn-g'])
	for i in range(len(defs)):
		defx = []
		for txt in defs[i].find_all('span', class_=['prefix', 'def', 'label-g', 'ndv', 'xr-gs', 'suffix'], recursive=False):
			if len(txt.get_text()):
				defx.append(txt.get_text())
		
		if not len(defx):
			continue
		
		rep.defs.append(defx)
		
		if bWithExample:
			examples = []
			for exm in defs[i].find_all('span', class_='x'):
				examples.append(exm.get_text())
			
			rep.examples.append(examples)
	
	return rep

DIC_OBJ = dicTypes.Dictionary('https://www.oxfordlearnersdictionaries.com/definition/english/%s', OEDParser)