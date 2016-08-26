#!/usr/bin/python2
# coding:utf-8

# by ins3c7
# 26 Ago 2016

# Log Parser

import os, re
dic = []
for lg in os.listdir('.'):
	with open(lg, 'r') as f:
		lines = f.readlines()
	for line in lines:
		try:
			line = line.split('\t')[1]
			if line.lower().find('approved')!=-1:
				num = re.findall('\d+', line)
				for n in num:
					if len(n) == 16:
						if len(num[num.index(n)+1]) == 2:
							result = num[num.index(n)], num[num.index(n)+1]+''+num[num.index(n)+2][:2], num[num.index(n)+3]
						else:
							result = num[num.index(n)], num[num.index(n)+1], num[num.index(n)+2]
						if result not in dic:
							dic.append(result)
		except Exception, e:
			pass
			# print str(e)

for result in dic:
	print '[APPROVED]',' '.join(result)
