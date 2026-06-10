import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import inspect

    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    return np, plt


@app.cell
def _():
    import ollama

    return (ollama,)


@app.cell
def _(ollama):
    OLLAMA = "http://localhost:11434"
    client = ollama.Client(OLLAMA)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ///error

    sjdks

    ///
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    /// error
    ///
    """)
    return


@app.cell
def _(mo, np, ollama, plt):
    def extract_function(text):
        # try markdown block first
        if "```" in text:
            start = text.find("```python\n")
            if start == -1:
                start = text.find("```\n")
            start = text.index("\n", start) + 1
            end = text.find("```", start)
            code = text[start:end].strip()
        elif "def " in text:
            start = text.find("def ")
            code = text[start:].strip()
        else:
            return None

        # TODO: replace this with new name analysis after eval.
        # extract function name and replace with "f"
        def_line = code.splitlines()[0]  # "def some_name(x):"
        name_start = def_line.index("def ") + 4
        name_end = def_line.index("(")
        original_name = def_line[name_start:name_end]
    
        return code.replace(original_name, "f", 1)
    
    def chat():
        system_prompt = {
            "role": "system",
            "content": """
    - You are a Python code generator. Output ONLY valid Python code, no explanation, no markdown, no backticks. Your response must be directly executable with eval() or exec().
    - Analyse each user query to find the most recent description of a math function,
    - Output the Python code that implements this function as a function named `f`,
    - You may use NumPy. Don't reimport it, it is already available as `np`.)
            """,
        }

        def model(messages, _):
            messages = [system_prompt] + [
                {"role": m.role, "content": m.content} for m in messages
            ]
            response = ollama.chat(
                model="mistral",
                messages=messages
            )

            text = response["message"]["content"]
            fun_code = extract_function(text)
            print(repr(fun_code))
            try:
                globs = {"np": np}
                exec(fun_code, globs)
                print(list(globs.keys()))
                fig, axes = plt.subplots(1, 1, figsize=(8, 2)) 
                x = np.linspace(-2, 2)
                axes.plot(x, globs["f"](x))
                axes.grid(True)
                return fig
            except Exception as e:
                return mo.md(f"/// error\n\n{e}\n\n///")

        return mo.ui.chat(
            model,
        )


    chat()
    return


if __name__ == "__main__":
    app.run()
