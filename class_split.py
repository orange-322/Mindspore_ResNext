import pandas as pd

df = pd.read_table('classes.txt', delimiter=' ',
                   names=['id', 'name']).to_numpy()
str = "["
for i in range(200):
    str += f"'{df[i][1]}', "

str += "]"
print(str)
