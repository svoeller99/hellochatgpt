# Hello ChatGPT - A simple interactive prompt

## Usage
0. You're encouraged to use `pyenv` - note the included `.python-version` file.
1. `pip install -r requirements.txt`
2. Create a file called `constants.py` and populate your OpenAI API key, as follows:

```python
openai_api_key = '<YOUR_API_KEY>'
```

3. Run the program as follows and start sending prompts:

```sh
python ./chatgpt.py
```

Alternatively, send an optional style in which ChatGPT should respond, as follows:

```sh
python ./chatgpt.py --style "a pirate
```

Assuming you're on a Mac, you can optionally enable text-to-speech, like so:

```sh
python ./chatgpt.py --speak
```