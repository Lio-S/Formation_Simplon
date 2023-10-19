from components.my_module import add, mul, test
from components.data_sc import csv_clean
import numpy as np
from pathlib import Path

print(add(3,5))
print(mul(5,5))

print(np.arange(5))


print(test('test'))
filepath = Path('data/titanic.csv')
csv_clean(filepath)