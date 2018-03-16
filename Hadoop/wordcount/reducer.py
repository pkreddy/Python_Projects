#!/usr/bin/env python

import sys

if __name__ == '__main__':
	curkey = None
	total = 0
	for line in sys.stdin:
		key, val = line.split("\t")
		val = int(val)
		if key == curkey:
			total += val
		else:
			if curkey is not None:
				sys.stdout.write("{0}\t{1}\n" .format(curkey, total))

			curkey = key
			total = val
