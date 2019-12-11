import click
import pytest
from app.utils import validate_iso_639


def test_validate_iso_639_valid_return():
    valid_code = "en"
    assert validate_iso_639(ctx=None, param=None, lang_code=valid_code) == valid_code

def test_validate_iso_639_string_raise_error():
    invalid_code = "INVALID"
    with pytest.raises(click.BadParameter):
        validate_iso_639(ctx=None, param=None, lang_code=invalid_code)
