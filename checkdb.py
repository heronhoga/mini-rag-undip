import chromadb
client = chromadb.PersistentClient(path="db_undip")
collection = client.get_collection("faq_kampus")
