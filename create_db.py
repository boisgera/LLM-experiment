import pathlib

import ollama
import chromadb
import nltk.data
import requests

# Ollama model
MODEL = "mistral"

client = chromadb.PersistentClient(path="history-of-music")
if not pathlib.Path("history-of-music").exists():
    # 📖 A Complete History of Music by W. J. Baltzell
    BOOK_URL = f"https://www.gutenberg.org/ebooks/54392.txt.utf-8"
    text = requests.get(BOOK_URL).text
    tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
    sentences = tokenizer.tokenize(text)
    sentences = [sentence.replace("\r\n", " ") for sentence in sentences]
    for sentence in sentences:
        print(sentence)
    print()
    print(f"{len(sentences) = }")
    print()

    collection = client.create_collection(name="history-of-music")

    ids = [f"sentence-{i}" for i, _ in enumerate(sentences)]
    collection.add(documents=sentences, ids=ids)

collection = client.get_collection("history-of-music")

while True:
    print("> ", end="", flush=True)
    query = input()
    results = collection.query(query_texts=query, n_results=10)
    print(results)


exit()

documents = [
  "Llamas are members of the camelid family meaning they're pretty closely related to vicuñas and camels",
  "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands",
  "Llamas can grow as much as 6 feet tall though the average llama between 5 feet 6 inches and 5 feet 9 inches tall",
  "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight",
  "Llamas are vegetarians and have very efficient digestive systems",
  "Llamas live to be about 20 years old, though some only live for 15 years and others live to be 30 years old",
]

client = chromadb.Client()
collection = client.create_collection(name="docs")

# store each document in a vector embedding database
for i, d in enumerate(documents):
  response = ollama.embeddings(model="mxbai-embed-large", prompt=d)
  embedding = response["embedding"]
  collection.add(
    ids=[str(i)],
    embeddings=[embedding],
    documents=[d]
  )