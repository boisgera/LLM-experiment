import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    import json

    return (json,)


@app.cell
def _():
    import requests

    return (requests,)


@app.cell
def _():
    OLLAMA = "http://localhost:11434"
    return (OLLAMA,)


@app.cell
def _(OLLAMA, requests):
    _response = requests.get(OLLAMA)
    assert _response.ok
    _response.text
    return


@app.cell
def _(OLLAMA):
    URL = f"{OLLAMA}/api/generate"
    URL
    return (URL,)


@app.cell
def _(URL, requests):
    _response = requests.post(URL, json={"model": "mistral", "prompt": "Are you listening?"})
    assert _response.ok
    print(_response.text)
    return


@app.cell
def _(URL, json, requests):
    _response = requests.post(URL, json={"model": "mistral", "prompt": "Are you listening?"})
    assert _response.ok
    jsons = [json.loads(line) for line in _response.text.splitlines()]
    jsons
    return (jsons,)


@app.cell
def _(jsons):
    print("".join(_j["response"] for _j in jsons))
    return


if __name__ == "__main__":
    app.run()
