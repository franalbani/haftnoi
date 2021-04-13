#!/usr/bin/env python3
from itertools import combinations, product
from collections import defaultdict
from fractions import Fraction as F

barra = F(10, 1)

discos = [  F(5, 4),
            F(5, 2),
            F(5, 1),
            F(5, 1),
            F(5, 1),
            F(5, 1),
            F(10, 1)] # sólo los de un lado

pesos = [55, 30, 50, 35, 30]

candidatos = defaultdict(set)

for i, peso in enumerate(pesos):
    x = (peso - barra)/2
    for k in range(1, len(discos) + 1):
        for c in set(combinations(discos, k)):
            if sum(c) == x:
                candidatos[i].add(c)
                # print(f'{x}: {[str(x) for x in c]}')

for i, cs in candidatos.items():
    peso = pesos[i]
    print(f'{peso} ({float(peso - barra)/2}):')
    for c in cs:
        print(f'\t{[str(x) for x in c]}')
        # print(f'\t{c}')

# problema: acá se necesita diferenciar discos de mismo peso
for seq in product(*[candidatos[i] for i in range(len(pesos))]):
    z = []
    for a, b in zip(seq, seq[1:]):
        z.append(len(set(b) ^ set(a)))
    print(z)
