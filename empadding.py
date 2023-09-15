import os
import pandas as pd
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

metadata = []

for i in range(1, 30):
	path = './datas/sparql' + str(i)
	metadata.append(pd.read_csv(path, sep="@ko,"))

for i in range(1, 29):
	metadata[0] = pd.concat([metadata[0], metadata[i]], ignore_index=True)

metadata[0].to_csv("./fulldata.csv", index=False,)
print(metadata[0].shape)





def embedding(text):
	response = openai.Embedding.create(
		model="text-embedding-ada-002",
		input=text
	)
