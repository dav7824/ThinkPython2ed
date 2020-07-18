#!/usr/bin/env python2
'''
Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict.
Solution: https://github.com/AllenDowney/ThinkPython2/blob/bb8e9ce836564a7d4e354ad8948177a69441c0fb/code/invert_dict.py
'''

def invert_dict(d):
	inv_d = {}
	for key in d:
		val = d[key]
		inv_d.setdefault(val, []).append(key)
		#print inv_d[val]
	return inv_d


if __name__ == '__main__':
	d_ori = {'apple':'A', 'banana':'B', 'lemon':'L', 'air':'A'}
	d_inv = invert_dict(d_ori)
	print d_inv
