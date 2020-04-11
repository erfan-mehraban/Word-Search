"""
Author: Li-Pro 2020

Refer to build/requirements.txt for build informations.

An example interactive program that searches for words.
"""

import sys
import string

import diclib # The main library

class Format:
	VIEWABLES = string.digits + string.ascii_letters + string.punctuation + ' \n'
	
	def strViewable(s):
		""" Format to readable. Prevent '\\r'. """
		sum = ''
		for x in s:
			if not x in Format.VIEWABLES:
				if x == '\r': x = ' '
				else: x = ' '
			sum += x
		
		return sum
	
	def setLineWidth(s, wlim):
		""" To be easier to read. """
		sum = ''
		for ox in s.split('\n'):
			cnt = 0
			for x in ox.split(' '):
				if len(x)<=0:
					continue
				
				if cnt+len(x) >= wlim:
					sum += '\n'
					cnt = 0
				
				sum += x+' '
				cnt += len(x)+1
			
			sum += '\n'
		
		return sum
	
	def formatted(result, bWithExample, wlim):
		""" An format example. """
		if not len(result.defs):
			return 'Word not found.\n\n'
		
		rep = ''
		for i in range(len(result.defs)):
			rep += str(i+1)+'. \n---\n'
			for defx in result.defs[i]:
				rep += defx + '\n'
			
			if bWithExample:
				rep += '\nExamples: \n'
				for egx in result.examples[i]:
					rep += egx + '\n'
			
			rep += '\n'
		
		return Format.setLineWidth(Format.strViewable(rep), wlim)

def main():
	""" A search program example. """
	print("----- Search Panel -----")
	print("Usage:")
	print(" Type a word to search.")
	print()
	print("Options:")
	print(" -oed : Urban Dictionary (Update Required)")
	print(" -urb : Urban Dictionary")
	print(" -camb: Cambridge Dictionary")
	print()
	print(" -eg  : show th examples")
	print(" -wXX : set line width to XX")
	print("------------------------")
	print()
	
	while True:
		try: line = input("Search: ")
		except (EOFError): break
		
		if len(line) <= 0:
			print()
			continue
		
		seq = line.split(' ')
		word, dic, bWithExample, wlim = [], 'urb', False, 90  # word & options
		for sOpt in seq:
			if len(sOpt)>1 and sOpt[0]=='-':
				opt = sOpt[1:]
				if opt in diclib.dic_list:
					dic = opt
				elif opt=='eg': 
					bWithExample = True
				elif opt[0]=='w' and len(opt[1:])>0:
					if all((x in string.digits) for x in opt[1:]):
						wlim = int(opt[1:])
			elif len(sOpt)>0:
				word.append(sOpt)
		
		result = diclib.searchWord(' '.join(word), dic, bWithExample)
		print(Format.formatted(result, bWithExample, wlim), end='')

if __name__=="__main__":
	main() # Run the example