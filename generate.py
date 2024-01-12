# Python Standard Library
import json
import sys

# Third-Party
import requests

SERVER = "http://localhost:11434"
url = f"{SERVER}/api/generate"

def answer(prompt):
    json_data = {"model": "mistral", "prompt": prompt}
    response = requests.post(url, json=json_data)
    if response.status_code == 200:
        json_lines = response.content.decode("utf-8").splitlines()
        answers = [json.loads(json_line) for json_line in json_lines]
        for answer in answers:
            if not answer["done"]:
                print(answer["response"], end="", flush=True)
            else:
                print()
                break
    else:
        response.raise_for_status()

prompt = sys.argv[1]
answer(prompt)
    