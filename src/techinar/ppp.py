import pandas as pd
import math
#pizzas
pizza_file_path='data/pizzas.csv'
pizza_data=pd.read_csv(pizza_file_path)
pizza_data["Area"]=[((size /2) **2)*math.pi  for size in pizza_data["Size"]]
pizza_data["Price_per_SqInch"]=pizza_data["Price"]/pizza_data["Area"]
pizzas= pizza_data.sort_values(by=['Price_per_SqInch'], ascending=True)
print(pizzas)