import pandas as pd
import openai
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class QueryEngine:
    def __init__(self, openai_api_key):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.data = pd.read_csv('data/bigBasketProducts.csv')
        self.embeddings = pd.read_csv('embeddings/vector_embeddings.csv')
        openai.api_key = openai_api_key

    def query(self, query_text):
        query_embedding = self.model.encode([query_text])[0]
        similarities = cosine_similarity([query_embedding], self.embeddings.values)[0]
        most_similar_idx = similarities.argmax()
        return self.data.iloc[most_similar_idx]

    def get_gpt_response(self, query, product_info):
        prompt = f"Question: {query}\nProduct Information: {product_info}\nAnswer:"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()

