import click


def success(text):
    return click.style(text, fg="green", bold=True)


def error(text="Error"):
    return click.style(text, fg="red", bold=True)
