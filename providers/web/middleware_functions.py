from providers.web.fastapi.exceptions import MissingHeaderException


def infer_user_language_from_header(header_value: str | None) -> str:
    if header_value is None or header_value == '':
        raise MissingHeaderException

    language = header_value.split(",")[0].strip()

    return language
