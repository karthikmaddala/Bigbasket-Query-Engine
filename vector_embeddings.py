from sentence_transformers import SentenceTransformer
import pandas as pd
import os
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings():
    # Load your dataset
    df = pd.read_csv('data/bigBasketProducts.csv')

    # Ensure descriptions are strings and handle NaN values
    df['description'] = df['description'].fillna('')  # Replace NaN with empty string
    df['description'] = df['description'].astype(str)  # Convert all to strings

    descriptions = df['description'].tolist()

    # Generate embeddings
    embeddings = model.encode(descriptions, show_progress_bar=True)
    # Create 'embeddings' directory if it doesn't exist
    if not os.path.exists('embeddings'):
        os.makedirs('embeddings')
    # Save embeddings
    pd.DataFrame(embeddings).to_csv('embeddings/vector_embeddings.csv', index=False)

if __name__ == '__main__':
    generate_embeddings()



