## Ejercicio 5.12: Comprar

import random
import numpy as np

#%%
def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album


#%%
def album_incompleto(A):
    A.sort()
    if A[0] == 0:
        return True
    else:
        return False


#%%
def comprar_figu(figus_total):
    figurita = random.randint(1, figus_total)
    return figurita


figus_total = 670
