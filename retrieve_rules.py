def retrieve_rules(user_query, index, rules, model):
    query = model.encode([user_query]).astype("float32")
    k = 15
    distances, indices = index.search(query, k)
    context = [rules[i] for i in indices[0]]
    return context