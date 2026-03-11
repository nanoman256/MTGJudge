from sentence_transformers import SentenceTransformer

import embeddings
import retrieve_rules
import client
import parser
import requests

data = requests.get("https://magicthegathering.io/vi/cards").json()
cards = data["cards"]

model = SentenceTransformer('all-MiniLM-L6-v2')
file_path = "mtg-rules-2026.txt"
pattern = r"^\d{1,3}\.\d{1,2}[a-z]?\b.*$"
rules = parser.parse_rules(file_path, pattern)
index = embeddings.build_index(rules, model)

user_query = "How does warp work with my creature if it left the battlefield and reentered?"

context = retrieve_rules.retrieve_rules(user_query, index, rules, model)

response = client.ask_llm(context, user_query)

print(response)