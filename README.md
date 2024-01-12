# The LLaMa Experiment

## Ollama

![oolama landing page](images/ollama.jpg)

If you work with MacOS or Linux, download and install [Ollama](https://ollama.ai/). Otherwise, get the URL of a running ollama instance from your instructor and skip to the next section.

Then test [Mistral-7B LLM] with `ollama run mistral`:

```
$ ollama run mistral
>>> Hey, anyone here?
Hello! I'm here. What can I assist you with today?

>>> Ah, nothing, everything's fine mate :)
Great to hear that! Is there anything specific you would like me to help 
with or any general questions you have on your mind? I'm here to assist 
you with anything you need.

>>> Send a message (/? for help)
```

> [!WARNING] Have patience and all will be revealed
> The first time you run the `ollama run mistral` command, don't be suprised
> if it takes a few minutes to start up. This is because the ollama instance
> is downloading the Mistral 7B model which represent a few GB of data.
> The subsequent run will be much faster.

## Web (HTTP) Interface

