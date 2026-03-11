import faiss

def build_index(rules, model):
    embeddings = model.encode(rules).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index
