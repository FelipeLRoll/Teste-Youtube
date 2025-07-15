import pandas as pd


data ={ 
       "nome": ["João", "Maria", "Pedro", "Ana"],
       "idade": [28, 22, 35, 30],
       "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
}

df = pd.DataFrame(data)

df.describe(exclude='object')