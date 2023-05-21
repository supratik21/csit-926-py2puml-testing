import _io
import py2puml.asserts
import pathlib
import typing
from py2puml.asserts import StringIO
from collections import ChainMap
from hypothesis import given, strategies as st
from pathlib import Path

@given(initial_value=st.just(""), newline=st.just("\n"))
def test_fuzz_StringIO(initial_value, newline) -> None:
    StringIO(initial_value=initial_value, newline=newline)