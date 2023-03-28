import pandas as pd
import numpy as np
from pydataset import data

fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", 
"honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

my_fruits = pd.Series(fruits)
print(type(my_fruits))

