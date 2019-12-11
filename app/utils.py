import click
from app.constants import ISO_639


def validate_iso_639(ctx, param, lang_code: str) -> str:
    """Ensure that a given two-character code matches ISO 689 standards."""
    if lang_code not in ISO_639:
        raise click.BadParameter("Language must be ISO 639-1 format.")
    else:
        return lang_code
