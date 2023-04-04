class APIKeyNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "OpenAI API key is empty"
        super().__init__(self.message)


class PromptNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Prompt is empty"
        super().__init__(self.message)


class ModelNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Model is not set"
        super().__init__(self.message)


class ModelNotValidException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Model is not supported"
        super().__init__(self.message)
