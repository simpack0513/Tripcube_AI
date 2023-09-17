# 한국관광공사에서 받은 데이터 csv 파일로 병합
import pandas as pd

metadata = []

for i in range(1, 30):
	path = './datas/sparql' + str(i)
	metadata.append(pd.read_csv(path, sep="@ko,"))

for i in range(1, 29):
	metadata[0] = pd.concat([metadata[0], metadata[i]], ignore_index=True)

idx = metadata[0][metadata[0]['description'] == '"-"'].index
metadata[0].drop(idx, inplace=True)

metadata[0].to_csv("./fulldata.csv", index=False,)
print(metadata[0].shape)
