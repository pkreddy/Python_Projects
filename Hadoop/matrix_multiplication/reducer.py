#!/usr/bin/env python

import fileinput

Mlist = {}
Nlist = {}

for line in fileinput.input():
    line = line.strip()
    key, data = line.split()
    l, j, val = data.split(',')
    j = int(j)
    val = float(val)

    if l == 'A':
        if key in Mlist.keys():
            Mlist[key].append((j, val))
        else:
            Mlist[key] = [(j, val)]
    else:
        if key in Nlist.keys():
            Nlist[key].append((j, val))
        else:
            Nlist[key] = [(j, val)]


for key, arr in Mlist.items():
    s = 0
    for i, val in enumerate(arr):
        s += val[1] * Nlist[key][i][1]
    print("%s %s" % (key, s))