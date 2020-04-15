#!/usr/bin/python3
import sys
import numpy as np
from Bio.SVDSuperimposer import SVDSuperimposer

def get_atom(path, chain='A', atom='CA'):
    coords = []
    file = open(path)
    for line in file:
        if (line.startswith('ATOM') and
                line[21] == chain and
                line[13:15] == atom and
                (line[16] == 'A' or line[16] == ' ')):
            print(line)
            x_coord = float(line[30:38])
            y_coord = float(line[38:46])
            z_coord = float(line[46:54])
            coords.append([x_coord, y_coord, z_coord])
    return coords

def get_rmsd(coord1, coord2):
    if len(coord1) != len(coord2):
        print(sys.stderr, 'ERROR: The set of coordinates have different size.')
        sys.exit(1)
    svd = SVDSuperimposer()
    svd.set(np.array(coord1), np.array(coord2))
    svd.run()
    rmsd = svd.get_rms()
    rot, tran = svd.get_rotran()
    print('R', rot)
    print('T', tran)
    return rmsd

P1 = get_atom('3o20.pdb')
P2 = get_atom('3zcf.pdb')
print(len(P1), len(P2))
print(get_rmsd(P1, P2))
