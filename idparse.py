#!/usr/bin/python2
# coding:utf-8

# by ins3c7
# 26 Ago 2016

# Log Parser

import os, re
dic=[];dicbr=[]
for direc in [os.path.join('../', nome) for nome in os.listdir('../')]:
	for lg in os.listdir(direc):
		with open(direc+'/'+lg, 'r') as f:
			lines = f.readlines()
		for line in lines:
			br = False
			try:
				line = line.split('\t')[1]
				if line.lower().find('approved')!=-1:
					if line.lower().find('brazil')!=-1 or line.lower().find('brasil')!=-1:
						br = True
					num = re.findall('\d+', line)
					for n in num:
						if len(n) == 16:
							if len(num[num.index(n)+1]) == 2:
								result = num[num.index(n)], num[num.index(n)+1]+''+num[num.index(n)+2][:2], num[num.index(n)+3]
							else:
								result = num[num.index(n)], num[num.index(n)+1], num[num.index(n)+2]
							if result not in dic:
								if br:
									dicbr.append(result)
								else:
									dic.append(result)
			except Exception, e:
				# print str(e)
				pass

for result in dic:
	print '[APPROVED]',' '.join(result)

for result in dicbr:
	print '[APPROVED]',' '.join(result), '[BR]'

print '\nTOTAL:', str(len(dic)+len(dicbr)), 'results.', str(len(dicbr)), 'BR.\n'
