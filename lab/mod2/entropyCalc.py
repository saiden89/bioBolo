#!/usr/bin/python3
import sys
import numpy as np

def getAlignment(file):
    ali = {}
    f = open(file)
    for line in f:
        if not line.startswith('sp'):
            continue
        else:
            l = line.split()
            ID = l[0]
            sequence = l[1]
            ali[ID]=ali.get(ID, '') + sequence
    return ali


def getProfile(ali):
    profile = []
    n = len(ali.values()[0])


if __name__ == "__main__":
    file = sys.argv[1]
    ali = getAlignment(file)
    print(ali)

