import click
from src.core import set_api_key
from src.core import get_api_key
from src.core import get_api_key_date
from src.core import get_gpt_response
from src.core import set_model
from src.core import show_model_list
from src.core import get_selected_model_name

from src.util import success, error

about = """
Language modeling (LM) is the use of various statistical and probabilistic techniques to determine 
the probability of a given sequence of words occurring in a sentence. Language models analyze bodies 
of text data to provide a basis for their word predictions.

Examples,
ChatGPT is an artificial-intelligence chatbot developed by OpenAI and launched in November 2022. 
It is built on top of OpenAI's GPT-3.5 and GPT-4 families of large language models and has been 
fine-tuned using both supervised and reinforcement learning techniques.

The command line sends a request and generates a response based on the entered prompt by using Open AI's Language Models.
"""
main = click.Group(help=about)


about_authentication_command = """
Response is only generated after the api key is added to the command line.
"""


@main.command("authentication", help=about_authentication_command)
@click.option("--key", required=True, help="OpenAI authentication api key")
def command_set_api_key(key):
    try:
        set_api_key(key)
        response = "{}: API key added!".format(success("Status"))
        click.echo(response)
    except:
        click.echo(error() + ": Failed to set the api key.")


about_model_command = """
Checks whether the passed model is supported and if valid then use it by default
"""


# This function allows the user to set the model they want to use
# by the name of the model. It also checks if the name is valid
# and displays an error message if it is not valid.

@main.command("model", help=about_model_command)
@click.option("--name", required=True, help="OpenAI supported model name")
def command_set_selected_model(name):
    try:
        set_model(name)
        response = "{}: The selected model name is valid. Added to the cache.".format(
            success("Status")
        )
        click.echo(response)
    except:
        click.echo(error() + ": Failed to set the model.")


about_prompt_command = """
Returns a generated response from the GPT server
"""


@main.command("prompt", help=about_prompt_command)
@click.option(
    "--message", required=True, help="Prompt based on what the response is generated"
)
def commaand_get_gpt_response(message):
    try:
        response = get_gpt_response(message)
        choices = response.get("choices")

        for choice in choices:
            if choice != None:
                text = choice.get("text")
                text = text.replace("\n\n", "\n")
            response = "{}\n{}".format(success("Response"), text)
            click.echo(response)
    except:
        click.echo(
            error()
            + ": Failed to generate a response based on the entered prompt. Please try again later."
        )


about_show_supported_model_command = """
Returns the list of supported models using the command line
"""


@main.command("show-supported-models", help=about_show_supported_model_command)
def command_show_supported_models():
    try:
        models = show_model_list()
        response = "{}\n\n{}".format(success("Models"), models)
        click.echo(response)
    except:
        click.echo(
            error() + ": Failed to show the supported models from the system cache."
        )


about_get_key_command = """
Returns the selected AI model in use
"""


# This function returns the name of the selected model from the system cache.
# It is used to get the name of the selected model when the user runs the
# "get-selected-model" command. The name of the selected model is used to
# determine which model to use when predicting.

@main.command("get-selected-model", help=about_get_key_command)
def command_get_selected_model_name():
    try:
        key = get_selected_model_name()
        response = "{}: {}".format(success("Key"), key)
        click.echo(response)
    except:
        click.echo(
            error() + ": Failed to get the selected model from the system cache."
        )


about_get_datetime_command = """
Returns the time when the key was set
"""


# This function is used to get the date from the system cache.
# It is used to display the date and time of the last time the user called the "get_api_key_date" function.

@main.command("get-datetime", help=about_get_datetime_command)
def command_show_api_key_date():
    try:
        datetime = get_api_key_date()
        response = "{}: {}".format(success("Datetime"), datetime)
        click.echo(response)
    except:
        click.echo(
            error() + ": Failed to get the datetime from the system cache.")


about_get_key_command = """
Returns the authentication api key in use
"""


# Retrieves the api key from the system cache and prints it to the console.
# Parameters: None
# Returns: None

@main.command("get-key", help=about_get_key_command)
def command_show_api_key():
    try:
        key = get_api_key()
        response = "{}: {}".format(success("Key"), key)
        click.echo(response)
    except:
        click.echo(error() + ": Failed to get the api key from the system cache.")


if __name__ == "__main__":
    main()
