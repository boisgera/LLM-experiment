# Python Standard Library
import json
import sys

# Third-Party
import requests

SERVER = "http://localhost:11434"
url = f"{SERVER}/api/chat"

messages = []

def answer(prompt):
    messages.append({"role": "user", "content": prompt})
    json_data = {"model": "mistral", "messages": messages}
    response = requests.post(url, json=json_data, stream=True)
    if response.status_code == 200:
        assistant_message = ""
        for response_line in response.iter_lines():
            print("*", response_line, flush=True)
            json_line = response_line.decode("utf-8")
            answer = json.loads(json_line)
            if not answer["done"]:
                fragment = answer["message"]["content"]
                print(fragment, end="", flush=True)
                assistant_message += fragment
            else:
                print()
                messages.append({"role": "assistant", "content": assistant_message})
                break
    else:
        response.raise_for_status()

while True:
    prompt = input("> ")
    print(repr(prompt))
    answer(prompt)
    