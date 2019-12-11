#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import pytest
from src.utils import _validate_iso_639


def test_validate_iso_639_valid_return(iso_639_fixture):
    for valid_code in iso_639_fixture:
        assert _validate_iso_639(ctx=None, param=None, lang_code=valid_code) == valid_code


def test_validate_iso_639_string_raise_error():
    invalid_code = "INVALID"
    with pytest.raises(click.BadParameter):
        _validate_iso_639(ctx=None, param=None, lang_code=invalid_code)
