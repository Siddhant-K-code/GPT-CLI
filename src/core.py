import openai
import dbm
from tabulate import tabulate
from datetime import datetime
from src.error import (
    APIKeyNotSetException,
    PromptNotSetException,
    ModelNotSetException,
    ModelNotValidException,
)

from src.constant import (
    model_list,
    CACHE_PATH,
    CLI_GPT_MODEL,
    CLI_GPT_API_KEY,
    CLI_GPT_API_LAST_UPDATED_DATE,
)

path = CACHE_PATH

# The function fetches the selected model from the system cache


def get_selected_model_name():
    with dbm.open(path) as db:
        datetime = db.get(CLI_GPT_MODEL).decode()
        return datetime


# The function fetches the api key from the system cache
def get_api_key():
    with dbm.open(path) as db:
        api_key = db.get(CLI_GPT_API_KEY).decode()
        return api_key


# The function fetches the date when the api key was updated and saved in the system cache
def get_api_key_date():
    with dbm.open(path) as db:
        datetime = db.get(CLI_GPT_API_LAST_UPDATED_DATE).decode()
        return datetime


# The function sets the authentication api key.
def set_api_key(api_key=""):
    now = datetime.now()

    if api_key == "" or api_key == None:
        raise APIKeyNotSetException()

    with dbm.open(path, "c") as db:
        db[CLI_GPT_API_KEY] = api_key
        db[CLI_GPT_API_LAST_UPDATED_DATE] = now.strftime("%d/%m/%Y %H:%M:%S")


# The function returns information about all the models supported in the cli
def show_model_list():
    models = [[model] for model in model_list]
    return tabulate(models, headers=["model_name"], tablefmt="grid")


# The function sets the model to be used for the response
def set_model(model_name=""):
    if model_name == "" or model_name == None:
        raise ModelNotSetException()

    if model_name not in model_list:
        raise ModelNotValidException()

    with dbm.open(path, "c") as db:
        db[CLI_GPT_MODEL] = model_name


# The function queries the Open AI server for the GPT response.
def get_gpt_response(prompt=""):
    with dbm.open(path) as db:
        api_key = db.get(CLI_GPT_API_KEY).decode()
        model_name = db.get(CLI_GPT_MODEL).decode()
        if api_key == "" or api_key == None or type(api_key) != str:
            raise APIKeyNotSetException()
        if model_name == "" or model_name == None or type(model_name) != str:
            raise ModelNotSetException()

    if prompt == "" or prompt == None or type(prompt) != str:
        raise PromptNotSetException()

    openai.api_key = api_key

    response = openai.Completion.create(
        model=model_name,
        prompt=prompt,
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response
