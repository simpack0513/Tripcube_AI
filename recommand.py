import pandas as pd
import openai
from sentence_transformers import SentenceTransformer, util
import torch

class Recommand:

	def __init__(self):
		openai.api_key_path = "./api_key.txt"
		self.metadata = pd.read_csv("./fulldata_embedding.csv", sep="@")
		self.convert_data = []
		for data in self.metadata["embeddings"].values.tolist():
			self.convert_data.append(eval(data))

	def embedding(self, text):
		response = openai.Embedding.create(
			model="text-embedding-ada-002",
			input=text
		)
		return response["data"][0]["embedding"]

	def get_query_sim_top_k(self, text):
		vector = self.embedding(text)
		cos_scores = util.pytorch_cos_sim(vector, self.convert_data)[0]
		top_results = torch.topk(cos_scores, k=5)
		return (self.metadata.iloc[top_results[1].numpy(), :][['name']])
