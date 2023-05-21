
from typing import Dict, Type

from py2puml.domain.umlclass import UmlClass, UmlAttribute
from py2puml.domain.umlitem import UmlItem


def inspect_namedtuple_type(
    namedtuple_type: Type,
    namedtuple_type_fqn: str,
    domain_items_by_fqn: Dict[str, UmlItem]
):
    domain_items_by_fqn[namedtuple_type_fqn] = UmlClass(
        name=namedtuple_type.__name__,
        fqn=namedtuple_type_fqn,
        attributes=[
            UmlAttribute(tuple_field, 'Any', False)
            for tuple_field in namedtuple_type._fields
        ]
    )
import py2puml.inspection.inspectnamedtuple
import py2puml.domain.umlclass
import py2puml.domain.umlitem
import typing
from hypothesis import given, strategies as st
from py2puml.inspection.inspectnamedtuple import UmlAttribute

@given(name=st.text(), type=st.text(), static=st.booleans())
def test_fuzz_UmlAttribute(name: str, type: str, static: bool) -> None:
    py2puml.inspection.inspectnamedtuple.UmlAttribute(name=name, type=type, static=static)



@given(
    name=st.text(),
    fqn=st.text(),
    attributes=st.lists(st.builds(UmlAttribute)),
    is_abstract=st.booleans(),
)
def test_fuzz_UmlClass(
    name: str,
    fqn: str,
    attributes: typing.List[py2puml.domain.umlclass.UmlAttribute],
    is_abstract: bool,
) -> None:
    py2puml.inspection.inspectnamedtuple.UmlClass(
        name=name, fqn=fqn, attributes=attributes, is_abstract=is_abstract
    )



@given(name=st.text(), fqn=st.text())
def test_fuzz_UmlItem(name: str, fqn: str) -> None:
    py2puml.inspection.inspectnamedtuple.UmlItem(name=name, fqn=fqn)



@given(
    namedtuple_type=st.just(type),
    namedtuple_type_fqn=st.text(),
    domain_items_by_fqn=st.dictionaries(keys=st.text(), values=st.builds(UmlItem)),
)
def test_fuzz_inspect_namedtuple_type(
    namedtuple_type: typing.Type,
    namedtuple_type_fqn: str,
    domain_items_by_fqn: typing.Dict[str, py2puml.domain.umlitem.UmlItem],
) -> None:
    py2puml.inspection.inspectnamedtuple.inspect_namedtuple_type(
        namedtuple_type=namedtuple_type,
        namedtuple_type_fqn=namedtuple_type_fqn,
        domain_items_by_fqn=domain_items_by_fqn,
    )
