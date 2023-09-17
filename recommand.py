import pandas as pd
import openai
from sentence_transformers import SentenceTransformer, util
import torch

openai.api_key_path = "./api_key.txt"

def embedding(text):
	response = openai.Embedding.create(
		model="text-embedding-ada-002",
		input=text
	)
	return response["data"][0]["embedding"]

def get_query_sim_top_k(vector):
	cos_scores = util.pytorch_cos_sim(vector, convert_data)[0]
	print(cos_scores.shape)
	top_results = torch.topk(cos_scores, k=10)
	return top_results

metadata = pd.read_csv("./fulldata_embedding.csv", sep="@")

convert_data = []
for data in metadata["embeddings"].values.tolist():
	convert_data.append(eval(data))

vector = embedding("한강이 보이는 곳에서 치맥 한잔")
top_result = get_query_sim_top_k(vector)
print(metadata.iloc[top_result[1].numpy(), :][['name']])
