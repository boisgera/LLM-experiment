
OLLAMA = "http://localhost:11434"

import requests

response = requests.get(OLLAMA)
print(response.text)