# -*- coding: utf-8 -*-
n = input()
n = int(n)
a = []
temp = input()
a = temp.split()
for i in range(n) :
	a[i] = int(a[i])
#print(a)

def qsort(l, r) :
	i = l
	j = r
	mid = a[(l + r) >> 1]
	while i <= j :
		while a[i] < mid : 
			i += 1
		while a[j] > mid :
			j -= 1
		if i <= j :
			t = a[i]
			a[i] = a[j]
			a[j] = t
			i += 1
			j -= 1
	if l < j :
		qsort(l, j)
	if i < r :
		qsort(i, r)

qsort(0, n - 1)
print(a)
