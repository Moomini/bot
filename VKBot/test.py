import numpy as np
from random import randint
def rand_id():
    random_user_id=np.int64(randint(10000,1000000000000))
    return random_user_id
print(rand_id())

