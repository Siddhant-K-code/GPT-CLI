# GPT CLI Tool

This is a command line tool for interacting with the GPT API.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Siddhant-K-code/GPT-CLI)

## Usage

> **Note**: This tool requires OpenAI API key.

```bash
python app.py --help
```

## Commands:

- `authentication` Response is only generated after the API key is set
- `get-datetime` Returns the time when the key was set
- `get-key` Returns the authentication API key in use
- `get-selected-model` Returns the selected AI model in use
- `model` Checks whether the passed model is supported and sets it as the selected model
- `prompt` Returns a generated response from the GPT server
- `show-supported-models` Returns the list of supported models using the GPT API

## Options:

- `--help` Show this message and exit.
