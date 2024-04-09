# Ollama All The Way Down

## Ollama

![oolama landing page](images/ollama.jpg)

To begin with, download and install [Ollama](https://ollama.ai/). 

Congratulations, you now have a local web server listening on port 11434! Open a browser and go to [http://localhost:11434](http://localhost:11434); you should see the text "Ollama is running". Every interaction that you will have with the LLM model from now on will be go through this web server.

> [!TIP] 
> If for any reason this doesn't work for you but it works for a friend, 
> you may ask them to expose their local server to you using a service like 
> [ngrok](https://ngrok.com/). You will then have to replace
> `http://localhost:11434` by the URL they will give you.

To chat [Mistral-7B LLM](https://ollama.ai/library/mistral), simply type `ollama run mistral` in your terminal:

```
$ ollama run mistral
>>> Hey, anyone here?
Hello! I'm here. What can I assist you with today?

>>> Ah, nothing, everything's fine mate :)
Great to hear that! Is there anything specific you would like me to help with or any general questions you have on your mind? I'm here to assist you with anything you need.

>>> Send a message (/? for help)
```

> [!WARNING]
> The first time you run the `ollama run mistral` command,
> don't be suprised if it takes a few minutes to start up.
> This is because the Ollama
> is downloading the Mistral 7B model, a few gigabytes of data.
> The subsequent runs will be much faster.

> [!NOTE]
> You can also download a model without running it. For example
> `ollama download mistral` will download the Mistral 7B model:
>
> ```console
> $ ollama pull mistral
> pulling manifest
> pulling e8a35b5937a5... 100% ▕████████████████████████████████████████████████████▏ 4.1 GB
> pulling 43070e2d4e53... 100% ▕████████████████████████████████████████████████████▏  11 KB
> pulling e6836092461f... 100% ▕████████████████████████████████████████████████████▏   42 B
> pulling ed11eda7790d... 100% ▕████████████████████████████████████████████████████▏   30 B
> pulling f9b1e3196ecf... 100% ▕████████████████████████████████████████████████████▏  483 B
> verifying sha256 digest
> writing manifest
> removing any unused layers
> success
> ```




## Talk to Ollama with Python

Let `OLLAMA` be the URL of your Ollama server:

```pycon
>>> OLLAMA = "http://localhost:11434"
```

To check that the Ollama server is running, 
you don't actually need a web browser; you can actually use the Python `requests` library to get the same result:

```python
>>> import requests
>>> response = requests.get(OLLAMA)
>>> print(response.text)
Ollama is running
```

Now, to actually start using the Mistral-7B model, you can use the `generate` method exposed by the server. First, define `URL` as

```pycon
>>> URL = f"{OLLAMA}/api/generate"
```

This Web API expects you to post a JSON object with two keys: `model` and `prompt`. Since we are using the Mistral-7B model, the value of `model` is `"mistral"`. The value of `prompt` is the text that you want to use to start the conversation. For example:

```pycon
>>> data = {"model": "mistral", "prompt": "Are you listening?"}
>>> response = requests.post(URL, json=data)
>>> response
<Response [200]>
>>> response.content
b'{"model":"mistral","created_at":"2024-01-12T17:04:38.40368138Z","response":"Yes","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:38.487816228Z","response":",","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:38.571748355Z","response":" I","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:38.655072569Z","response":" am","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:38.738731374Z","response":" listening","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:38.82237177Z","response":".","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:38.906004206Z","response":" How","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:38.989575923Z","response":" may","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:39.076522724Z","response":" I","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:39.160705601Z","response":" assist","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:39.243577905Z","response":" you","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:39.327371113Z","response":" today","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:39.410974105Z","response":"?","done":false}\n{"model":"mistral","created_at":"2024-01-12T17:04:39.49568907Z","response":"","done":true,"context":[733,16289,28793,28705,4867,368,9857,28804,733,28748,16289,28793,13,5613,28725,315,837,9857,28723,1602,993,315,6031,368,3154,28804],"total_duration":3343392853,"load_duration":1583037589,"prompt_eval_count":14,"prompt_eval_duration":667000000,"eval_count":13,"eval_duration":1083890000}\n'
```

```pycon
>>> json_lines = response.content.decode("utf-8").splitlines()
>>> for json_line in json_lines:
...    print(json_line)
...
{"model":"mistral","created_at":"2024-01-12T17:04:38.40368138Z","response":"Yes","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:38.487816228Z","response":",","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:38.571748355Z","response":" I","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:38.655072569Z","response":" am","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:38.738731374Z","response":" listening","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:38.82237177Z","response":".","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:38.906004206Z","response":" How","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:38.989575923Z","response":" may","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:39.076522724Z","response":" I","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:39.160705601Z","response":" assist","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:39.243577905Z","response":" you","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:39.327371113Z","response":" today","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:39.410974105Z","response":"?","done":false}
{"model":"mistral","created_at":"2024-01-12T17:04:39.49568907Z","response":"","done":true,"context":[733,16289,28793,28705,4867,368,9857,28804,733,28748,16289,28793,13,5613,28725,315,837,9857,28723,1602,993,315,6031,368,3154,28804],"total_duration":3343392853,"load_duration":1583037589,"prompt_eval_count":14,"prompt_eval_duration":667000000,"eval_count":13,"eval_duration":1083890000}
```

That's better! And now we can convert these JSON strings into Python dictionaries:

```pycon
>>> answers = [json.loads(json_line) for json_line in json_lines]
>>> answers
[{'model': 'mistral', 'created_at': '2024-01-12T17:04:38.40368138Z', 'response': 'Yes', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:38.487816228Z', 'response': ',', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:38.571748355Z', 'response': ' I', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:38.655072569Z', 'response': ' am', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:38.738731374Z', 'response': ' listening', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:38.82237177Z', 'response': '.', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:38.906004206Z', 'response': ' How', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:38.989575923Z', 'response': ' may', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:39.076522724Z', 'response': ' I', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:39.160705601Z', 'response': ' assist', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:39.243577905Z', 'response': ' you', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:39.327371113Z', 'response': ' today', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:39.410974105Z', 'response': '?', 'done': False}, {'model': 'mistral', 'created_at': '2024-01-12T17:04:39.49568907Z', 'response': '', 'done': True, 'context': [733, 16289, 28793, 28705, 4867, 368, 9857, 28804, 733, 28748, 16289, 28793, 13, 5613, 28725, 315, 837, 9857, 28723, 1602, 993, 315, 6031, 368, 3154, 28804], 'total_duration': 3343392853, 'load_duration': 1583037589, 'prompt_eval_count': 14, 'prompt_eval_duration': 667000000, 'eval_count': 13, 'eval_duration': 1083890000}]
```

Execept for the last item, characterized by `"done":true`, all the other items have `"done":false`. This means that the answer is not finished yet. We can use the `response` key to get the fragments of the answer:

```pycon
>>> for answer in answers:
...     if not answer["done"]:
...         print(answer["response"], end="", flush=True)
...     else:
...         print()
...
Yes, I am listening. How may I assist you today?
```

You may have waited a little to get the answer, and then it came all at once. Since this is not the most pleasant experience, we can actually ask for the answer in chunks. To do this, we need to

```pycon
>>> json_data = {"model": "mistral", "prompt": "Are you listening?"}
>>> response = requests.post(URL, data, stream=True)
>>> for response_line in response.iter_lines():
...    json_line = response_line.decode("utf-8")
...    answer = json.loads(json_line)
...    if not answer["done"]:
...        print(answer["response"], end="", flush=True)
...    else:
...        print()
...
Yes, I am listening. How may I assist you today?
```

This is a similar experience, except that fragments of the answer are printed as soon as they are available, which is a more enjoyable experience.

With a bit of work, we can wrap this code into a program
[`generate.py`](https://github.com/boisgera/LLM-experiment/blob/master/generate.py) that takes a prompt as a command-line argument and prints the answer:

```console
$ python generate.py "Are you listening?"
Yes, I am listening. How may I assist you today?
```

## Let's Chat!

This program is nice, but it is not very useful to have a conversation since the LLM model forgets the context of the conversation at each step.
For example:

```console
$ python generate.py "Hey my name is Sébastien. What's yours?"
Hey Sébastien! My name's Mistral. Nice to meet you!
$ python generate.py "Do you remember my name?"
I'm sorry, I do not have the ability to remember names. I don't have a memory or a database where information about users is stored. I can only provide information and assistance based on the data available to me at the time of our interaction.
```

We can fix this by using a different endpoint, `api/chat` and submit the conversation history with each request.

We now have to provide the context, which is a list of message,
dictionaries with two keys: `role` and `content`. The value of `role` is either `"user"` or `"assistant"`. The value of `content` is the text of the message (yours or the answer of Mistral-7B).

For example start with the following conversation:

```json
{
  "model": "mistral",
  "messages": [
    {
      "role": "user",
      "content": "My name is Sébastien. Answer simply OK please."
    }
  ]
}
```

You will probably get the answer "OK" from Mistral-7B.
Then, you can continue the conversation with the recording of the answer
and your own subsequent message:

```json
{
  "model": "mistral",
  "messages": [
    {
      "role": "user",
      "content": "My name is Sébastien. Answer simply OK please."
    },
    {
      "role": "assistant",
      "content": "OK"
    },
    {
      "role": "user",
      "content": "Do you remember my name?"
    }
  ]
}
```

## System Prompts

There is a third role, `"system"`, that you can use to influence dratiscally
the conversation by giving specific instructions to the model. For example,
start you list of messages with:

```python
messages = [
    {
        "role": "system",
        "content": "You are impersonating a French person who doesn't speek English.",
    }
]
```

```
> Hello! How are you?
 Bonjour! Moi, je suis bien merci. Comment allez-vous? (Hello! I am good, thank you. And how are you?)
> I am fine, thanks :). Are you French?
 Oui, je suis Français. (Yes, I am French.)
```

You can see that the model is now speaking French, but he still speaks some English,
when he should not use English at all according to thour instructions.
A suitable, more explicit "system" message _may_ fix or at least improve this issue;
elaborating such instructions is a dark art known as [prompt engineering].

[prompt engineering]: https://en.wikipedia.org/wiki/Prompt_engineering

You can use prompt engineering to create an application with a very specific
role: a language translator, an english tutor ... or a Python tutor!

## Ollama Python Library

Now that you know how HTTP requests work, you can use the Ollama Python library 
instead to talk to the Ollama models. This library has a higher-level interface 
and performs these HTTP requests under the hood. 
First install it with:

```bash

You can use the Ollama Python library to interact with the Ollama server
and bypass the explicit HTTP requests. 
First install this Pypi library with:

```bash
$ pip install ollama
```

and have a look at its examples [here](https://pypi.org/project/ollama/).
The Python API closely match the [HTTP REST API] that we have been using so far.

[HTTP REST API]: https://github.com/ollama/ollama/blob/main/docs/api.md

The `ollama` package provides a `Client` class that you can use to interact 
with the server. Configure it 

```pycon
>>> import ollama
>>> OLLAMA = "http://localhost:11434"
>>> client = ollama.Client(OLLAMA)
```

then use it

```pycon
>>> response = client.generate(model="mistral", prompt="Are you listening?", stream=True)
>>> for item in response:
...     print(item)
... 
{'model': 'mistral', 'created_at': '2024-04-09T13:23:25.680580534Z', 'response': ' Yes', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:25.799762718Z', 'response': ',', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:25.900719162Z', 'response': ' I', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.001831592Z', 'response': ' am', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.102831378Z', 'response': ' designed', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.213537806Z', 'response': ' to', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.316528486Z', 'response': ' listen', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.419662332Z', 'response': ' and', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.523196232Z', 'response': ' process', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.645587884Z', 'response': ' text', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.746636995Z', 'response': '-', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.846603128Z', 'response': 'based', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:26.946918818Z', 'response': ' information', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.047300774Z', 'response': '.', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.159380488Z', 'response': ' However', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.262964302Z', 'response': ',', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.363336479Z', 'response': ' please', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.463975695Z', 'response': ' note', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.565530467Z', 'response': ' that', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.667000436Z', 'response': ' I', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.769670818Z', 'response': ' don', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.892389686Z', 'response': "'", 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:27.993936349Z', 'response': 't', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.094892319Z', 'response': ' have', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.215311985Z', 'response': ' the', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.317437962Z', 'response': ' ability', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.419479906Z', 'response': ' to', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.522863067Z', 'response': ' understand', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.644491146Z', 'response': ' or', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.745132462Z', 'response': ' respond', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.847172647Z', 'response': ' to', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:28.97008162Z', 'response': ' spoken', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.072910074Z', 'response': ' language', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.18548044Z', 'response': ' as', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.287616003Z', 'response': ' I', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.410997067Z', 'response': ' don', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.511360904Z', 'response': "'", 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.612428737Z', 'response': 't', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.713706766Z', 'response': ' possess', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.815131374Z', 'response': ' a', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:29.91828318Z', 'response': ' voice', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.023054501Z', 'response': ' or', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.143906908Z', 'response': ' the', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.245337817Z', 'response': ' capability', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.345974355Z', 'response': ' to', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.447156139Z', 'response': ' hear', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.549265371Z', 'response': ' sounds', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.651445618Z', 'response': '.', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.774632498Z', 'response': ' I', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.876239614Z', 'response': ' can', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:30.977270134Z', 'response': ' only', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.078862844Z', 'response': ' process', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.181845616Z', 'response': ' and', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.285042327Z', 'response': ' generate', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.390980219Z', 'response': ' text', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.493757598Z', 'response': '.', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.597075405Z', 'response': ' How', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.701150505Z', 'response': ' may', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.806059601Z', 'response': ' I', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:31.918584029Z', 'response': ' assist', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.022588861Z', 'response': ' you', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.144995742Z', 'response': ' with', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.246713325Z', 'response': ' a', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.349905342Z', 'response': ' specific', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.452706846Z', 'response': ' query', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.576903921Z', 'response': ' or', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.678284353Z', 'response': ' task', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.780471543Z', 'response': '?', 'done': False}
{'model': 'mistral', 'created_at': '2024-04-09T13:23:32.883449836Z', 'response': '', 'done': True, 'context': [733, 16289, 28793, 28705, 4867, 368, 9857, 28804, 733, 28748, 16289, 28793, 5592, 28725, 315, 837, 5682, 298, 7105, 304, 1759, 2245, 28733, 5527, 1871, 28723, 2993, 28725, 4665, 5039, 369, 315, 949, 28742, 28707, 506, 272, 5537, 298, 2380, 442, 9421, 298, 14382, 3842, 390, 315, 949, 28742, 28707, 14612, 264, 3441, 442, 272, 21368, 298, 3934, 7258, 28723, 315, 541, 865, 1759, 304, 8270, 2245, 28723, 1602, 993, 315, 6031, 368, 395, 264, 2948, 5709, 442, 3638, 28804], 'total_duration': 7738210780, 'load_duration': 310027, 'prompt_eval_count': 8, 'prompt_eval_duration': 534697000, 'eval_count': 69, 'eval_duration': 7202823000}
```

Alternatively, if you are only interested in the reply text:

```pycon
>>> response = client.generate(model="mistral", prompt="Are you listening?", stream=True)
>>> print("".join(item["response"] for item in response))
 Yes, I am designed to listen and respond. How may I assist you today?

Regarding your question about "Are you listening?", it's an important aspect of communication, as it helps ensure that both parties are engaged and focused on the conversation. In my case, as a text-based AI language model, I don't have the ability to listen in the same way humans do. However, I am programmed to process and understand text input, so feel free to type in your queries or requests, and I will do my best to provide accurate and helpful responses. Let me know if there's a specific topic you'd like to discuss or if you have any other questions!
```

## Python Tutor

Make your own Python tutor with a graphical interface using [flet](https://flet.dev/).
You may begin with the following system prompt:

```python
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
```

You can also use the following flet code template to get started:

```python
def main(page: ft.Page):

    def send(event):
        messages.append({"role": "user", "content": question.value})
        send_button.disabled = True
        ...
        question.value = ""
        send_button.disabled = False
        page.update()

    question = ft.TextField(
        label="Your question",
        multiline=True,
        min_lines=5,
    )

    answer_display = ft.Markdown(
        "",
        selectable=True,
    )

    send_button = ft.ElevatedButton(
        "Ask your question",
        icon="send",
        on_click=send,
    )

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
```
