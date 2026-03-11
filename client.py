import ollama
def ask_llm(context, user_query):
    context_text = "\n".join(context)
    print(context_text)
    prompt = f"""
    Here are some relevant Magic the Gathering Rules
    Rules:
    {context_text}

    Answer the question using the rules above:
    Question:
    {user_query}
    """
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a very Helpful Magic the Gathering Judge"},
            {"role": "user", "content": prompt},
        ]
    )
    

    return response["message"]["content"]