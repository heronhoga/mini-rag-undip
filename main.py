from operations.get_answer import get_answer
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  

# Inisialisasi ChromaDB
chroma_client = chromadb.PersistentClient(path="./db_undip")  # Pastikan path sesuai
collection = chroma_client.get_or_create_collection(name="faq_kampus")

# Fungsi utama
def main():
    while True:
        query = input("Masukkan pertanyaan Anda: ")  
        if query.lower() in ["exit", "quit"]:
            break  

        answer = get_answer(query, collection, model, top_k=1)  
        print(answer)

if __name__ == "__main__":
    main()
