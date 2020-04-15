import sys
import numpy as np

def get_alphabet(sequence):
    alphabet = []
    for letter in sequence:
        if letter not in alphabet:
            alphabet.append(letter)
        alphabet.sort()
    return ''.join(alphabet)

def get_matrix(sequence, alphabet):
    n = len(alphabet)
    transition_matrix = np.zeros((n, n))
    l = len(sequence)
    for i in range(l - 1):
        p1 = alphabet.find(sequence[i])
        p2 = alphabet.find(sequence[i + 1])
        if p1 > -1 and p2 > -1:
            transition_matrix[p1][p2] += 1
    for i in range(n):
        transition_matrix[i, :] = transition_matrix[i, :]/np.sum(transition_matrix[i, :])
    return transition_matrix


def get_prob(sequence, tm, alphabet):
    p = 1.0
    l = len(seq)
    for i in range(l -1):
        p1 = alphabet.find(sequence[i])
        p2 = alphabet.find(sequence[i + 1])
        if p1 > -1 and p2 >-1:
            p = p * tm[p1][p2]
    return p


alpha = get_alphabet('ACHYASUHDHFJKNFADJKGNFJKAÒGNAFKJGNFKDGÒNF')
print(get_matrix('ACHYASUHDHFJKNFADJKGNFJKAÒGNAFKJGNFKDGÒNF', alpha))