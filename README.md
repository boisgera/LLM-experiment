# The LLaMa Experiment

## Ollama

![oolama landing page](images/ollama.jpg)

If you work with MacOS or Linux, download and install [Ollama](https://ollama.ai/). Otherwise, skip to the next section.

Then test [Mistral-7B LLM](https://ollama.ai/library/mistral) with `ollama run mistral`:

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

> [!WARNING]
> The first time you run the `ollama run mistral` command, 
> don't be suprised if it takes a few minutes to start up. 
> This is because the ollama instance
> is downloading the Mistral 7B model, a few GB of data.
> The subsequent runs will be much faster.

## Web Interface

If you have a local ollama instance running, there is a web server 
listening on port 11434.

```pycon
>>> SERVER = "http://localhost:11434"
```

Otherwise, get the address of a running ollama instance from your instructor.

We define `url` as the endpoint for the method `generate`:

```pycon
>>> url = f"{SERVER}/api/generate"
```

This Web API expects you to post a JSON object with two keys: `model` and `prompt`. Since we are using the Mistral-7B model, the value of `model` is `"mistral"`. The value of `prompt` is the text that you want to use to start the conversation. For example:

```pycon
>>> json_data = {"model": "mistral", "prompt": "Are you listening?"}
>>> response = requests.post(url, data)
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

Execept for the last item, characterized by `"done":true`, all the other items have `"done":false`. This means that the conversation is not over yet. We can use the `response` key to get the fragments of the answer:

```pycon
>>> for answer in answers:
...     if not answer["done"]:
...         print(answer["response"], end="", flush=True)
...     else:
...         print()
... 
Yes, I am listening. How may I assist you today?
```

```console
$ python generate.py "Are you listening?"
Yes, I am listening. How may I assist you today?
```