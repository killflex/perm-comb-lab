import numpy as np
from itertools import permutations

data = np.array(["MASSACHUSETTS"])
nomor = 0

perm = set(permutations(data))

# Output Way No. 1
jumlahpermutasi = len(perm)
print(jumlahpermutasi)