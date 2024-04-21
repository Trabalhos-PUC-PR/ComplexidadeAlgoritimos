import gerador as gd
from patience_sort import patience_sort

_time = 0.0


def iniciar_cronometro():
    global _time
    _time = gd.agora()


def encerrar_cronometro():
    global _time
    return gd.dif_time(gd.agora(), _time)


def medir_tempo_ordenacao(ordenador, tamanho: int = 10, arr=None):
    if arr is None:
        arr = [
            gd.gerar_dados_random(tamanho),
            gd.gerar_dados_crescente(tamanho),
            gd.gerar_dados_decrescente(tamanho)
        ]
    temps = []
    for a in arr:
        iniciar_cronometro()
        ordenador(a)
        temps.append(encerrar_cronometro())

    return temps
