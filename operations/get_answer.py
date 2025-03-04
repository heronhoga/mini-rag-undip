def get_answer(question, collection, model, top_k=1):
    query_vector = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_vector],  
        n_results=top_k,
        include=["documents", "distances", "metadatas"]
    )

    if not results["documents"]:
        return "Maaf, saya tidak menemukan jawaban yang sesuai."

    best_answer = results["documents"][0][0]
    similarity_score = results["distances"][0][0]
    
    return f"Jawaban: {best_answer} (Confidence: {1 - similarity_score:.2f})"

