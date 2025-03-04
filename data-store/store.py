from sentence_transformers import SentenceTransformer
import chromadb
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

with open('data/faq.json', 'r') as file:
    data = json.load(file)

client = chromadb.PersistentClient(path="db_undip")

collection = client.get_or_create_collection(name="faq_kampus")

for idx, item in enumerate(data):
    vector = model.encode(item["pertanyaan"]).tolist()
    collection.add(
        embeddings=[vector],
        documents=[item["jawaban"]],
        metadatas=[{"kategori": item["kategori"], "pertanyaan": item["pertanyaan"]}],
        ids=[str(idx)]
    )

print("Data berhasil disimpan di ChromaDB")