import pandas as pd
import numpy as np

sinapi = pd.read_excel("sheets/SINAPI_Custo_Ref_Composicoes_Sintetico_AL_202201_Desonerado.xlsx",
                       skiprows=4,
                       index_col=6,
                       na_filter=True)
sinapi = sinapi.drop(sinapi.index[0])
newCustoTotal = np.array(sinapi['CUSTO TOTAL'])
newCustoTotal = [custos.replace('.', '') for custos in newCustoTotal]
newCustoTotal = [custos.replace(',', '.') for custos in newCustoTotal]
sinapi['CUSTO TOTAL'] = sinapi['CUSTO TOTAL'].replace(newCustoTotal)
sinapi.iloc[:, 9:10] = newCustoTotal
sinapi['CUSTO TOTAL'] = pd.to_numeric(sinapi['CUSTO TOTAL'])
print(sinapi.dtypes)
