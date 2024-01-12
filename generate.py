# Python Standard Library
import json
import sys

# Third-Party
import requests

SERVER = "http://localhost:11434"
url = f"{SERVER}/api/generate"

def answer(prompt):
    json_data = {"model": "mistral", "prompt": prompt}
    response = requests.post(url, json=json_data, stream=True)
    if response.status_code == 200:
        for response_line in response.iter_lines():
            json_line = response_line.decode("utf-8")
            answer = json.loads(json_line)
            if not answer["done"]:
                print(answer["response"], end="", flush=True)
            else:
                print()
                break
    else:
        response.raise_for_status()

prompt = sys.argv[1]
answer(prompt)
    