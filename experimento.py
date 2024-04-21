from analisador import medir_tempo_ordenacao
from bogo_sort import bogo_sort
from gerador import gerar_dados_crescente
from gerador import gerar_dados_decrescente
from gerador import gerar_dados_random
from merge_sort_interativo import Merge_Sort_interativo_wapper
from merge_sort_recursivo import merge_sort__recursivo_wapper
from merge_sort_recursivo_random import merge_sort_recursivo_random_wapper
from patience_sort import patience_sort
from quick_sort_random import quick_sort_recursivo_random_wapper
from quick_sort_recursivo import quick_sort_recursivo_wapper
from select_sort_recursivo import select_sort_recursivo_wapper
from select_sort_recursivo_random import select_sort_recursivo_random_wapper
from sellSort_base_line import shellSort_Wapper


def gerar_resultados(tam):
    arr = [
        gerar_dados_random(tam),
        gerar_dados_crescente(tam),
        gerar_dados_decrescente(tam)
    ]
    ordenadores = [
        (quick_sort_recursivo_wapper, "Quick sort recursivo"),
        (quick_sort_recursivo_random_wapper, "Quick sort recursivo randomizado"),
        (Merge_Sort_interativo_wapper, "Merge sort interativo"),
        (merge_sort__recursivo_wapper, "Merge sort recursivo"),
        (merge_sort_recursivo_random_wapper, "Merge sort recursivo randomizado"),
        (select_sort_recursivo_wapper, "Select sort recursivo"),
        (select_sort_recursivo_random_wapper, "Select sort recursivo randomizado"),
        (shellSort_Wapper, "Sell Sort [Baseline]"),
        (bogo_sort, "Bogo Sort"),
        (patience_sort, "Patience Sort")
    ]
    tempos = []
    for o in ordenadores:
        print(f"Chegou no {o[1]}")
        tempos.append(medir_tempo_ordenacao(o[0], arr=arr))
        print(f'{o[1]}: {tempos[-1]}')


gerar_resultados(10)
