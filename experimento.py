#!/usr/bin/python3

import sys
from typing import List 
sys.setrecursionlimit(10_000_000)

from analisador import medir_tempo_ordenacao
from bogo_sort import bogo_sort
from merge_sort_interativo import Merge_Sort_interativo_wapper
from merge_sort_recursivo import merge_sort__recursivo_wapper
from merge_sort_recursivo_random import merge_sort_recursivo_random_wapper
from patience_sort import patience_sort
from quick_sort_random import quick_sort_recursivo_random_wapper
from quick_sort_recursivo import quick_sort_recursivo_wapper
from select_sort_recursivo import select_sort_recursivo_wapper
from select_sort_recursivo_random import select_sort_recursivo_random_wapper
from sellSort_base_line import shellSort_Wapper

def get_sorts_altos(tamanho_alto):
    return [
        (quick_sort_recursivo_random_wapper, "Quick sort recursivo randomizado", tamanho_alto),
        (Merge_Sort_interativo_wapper, "Merge sort interativo", tamanho_alto),
        (merge_sort__recursivo_wapper, "Merge sort recursivo", tamanho_alto),
        (merge_sort_recursivo_random_wapper, "Merge sort recursivo randomizado", tamanho_alto),
        (shellSort_Wapper, "Shell Sort [Baseline]", tamanho_alto),
    ]

def get_sorts_medios(tamanho_medio):
    return [
        (quick_sort_recursivo_wapper, "Quick sort recursivo", tamanho_medio),
        (select_sort_recursivo_wapper, "Select sort recursivo", tamanho_medio),
        (select_sort_recursivo_random_wapper, "Select sort recursivo randomizado", tamanho_medio),
        (patience_sort, "Patience Sort", tamanho_medio)
    ]

def get_sort_bogo(tamanho):
    return [
        (bogo_sort, "Bogo Sort", tamanho),
    ]

def get_deltas(ordenadores):
    tempos = []
    for o in ordenadores:
        tempos.append(medir_tempo_ordenacao(o[0], tamanho=o[2]))
        print(f'{tempos[-1]} - {o[1]}')
    return tempos

sorts = []
tempos = []

fr = open("results_random.csv", "w")
fc = open("results_crescente.csv", "w")
fd = open("results_decrescente.csv", "w")

iteracoes = 5
multiplier = 1_000

for i in range(1, iteracoes+1, 1):
    listasListaSort = []
    sorts = []
    print(f'Rodando para {i*multiplier}')

    listasListaSort.append(get_sorts_altos(multiplier * i))
    listasListaSort.append(get_sorts_medios(multiplier * i))
    listasListaSort.append(get_sort_bogo(multiplier * i))

    for lista in listasListaSort:
        for sorter in lista:
            sorts.append(sorter)

    tempos.append(get_deltas(sorts))


fr.write("tamanho,")
fc.write("tamanho,")
fd.write("tamanho,")
for sorter in sorts:
    if sorts.index(sorter) == len(sorts)-1:
        fr.write(sorter[1])
        fc.write(sorter[1])
        fd.write(sorter[1])
    else:
        fr.write(sorter[1]+",")
        fc.write(sorter[1]+",")
        fd.write(sorter[1]+",")

fr.write("\n")
fc.write("\n")
fd.write("\n")

count = 0
i_count = 1
for tempo_tamanhos in tempos:
    fr.write(f"{i_count*multiplier},")
    fc.write(f"{i_count*multiplier},")
    fd.write(f"{i_count*multiplier},")
    for tempo_tipos in tempo_tamanhos:
        if(count == len(sorts)-1):
            fr.write(str(tempo_tipos[0]))
            fr.write(f"\n")
            fc.write(str(tempo_tipos[1]))
            fc.write(f"\n")
            fd.write(str(tempo_tipos[2]))
            fd.write(f"\n")
            count = 0
        else:
            fr.write(str(tempo_tipos[0])+",")
            fc.write(str(tempo_tipos[1])+",")
            fd.write(str(tempo_tipos[2])+",")
        count+=1
    i_count+=1
    count = 0
