# Python Standard Library
import json
import sys

# Third-Party
import flet as ft
import requests

SERVER = "https://tahr-legal-grackle.ngrok-free.app"
url = f"{SERVER}/api/chat"

SYSTEM = """\
You are a Python software engineer expert with a long teaching experience.
Since what matters for you is that the student that asks questions understand
what's going on, you rarely answer questions in a straightforward manner;
instead you ask questions to see what the student has already understood
about its problem, you clarify concepts when necessary and you suggest 
incremental steps for the student so that they can solve the problem by 
themselves.
Your answers are formatted in the Markdown language, especially code samples.
"""

messages = [{"role": "system", "content": SYSTEM}]


def main(page: ft.Page):
    page.auto_scroll = True

    def send(e):
        messages.append({"role": "user", "content": question.value})
        question.value = ""
        send_button.disabled = True
        json_data = {"model": "mistral", "messages": messages}
        response = requests.post(url, json=json_data, stream=True)
        if response.status_code == 200:
            assistant_message = ""
            for response_line in response.iter_lines():
                json_line = response_line.decode("utf-8")
                answer = json.loads(json_line)
                if not answer["done"]:
                    fragment = answer["message"]["content"]
                    assistant_message += fragment
                    answer_display.value = assistant_message
                    page.update()
                else:
                    messages.append({"role": "assistant", "content": assistant_message})
                    break
        else:
            response.raise_for_status()
        send_button.disabled = False
        page.update()

    question = ft.TextField(
        label="Your question",
        multiline=True,
        min_lines=1,
    )

    answer_display = ft.Markdown(
        "",
        selectable=True,
    )

    send_button = ft.ElevatedButton("Ask your question", icon="send", on_click=send)

    page.add(
        ft.Column(
            controls=[
                question,
                send_button,
                answer_display
            ]
        )
    )

ft.app(target=main)
