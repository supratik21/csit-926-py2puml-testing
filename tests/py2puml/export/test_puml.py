import py2puml.export.puml
import py2puml.domain.umlclass
import py2puml.domain.umlenum
import py2puml.domain.umlitem
import py2puml.domain.umlrelation
import typing
from hypothesis import given, strategies as st
from py2puml.export.puml import UmlItem, UmlRelation
from py2puml.domain.umlclass import UmlAttribute
from py2puml.domain.umlenum import Member
from py2puml.export.puml import to_puml_content
from py2puml.domain.umlitem import UmlItem
from py2puml.domain.umlclass import UmlClass
from py2puml.domain.umlenum import UmlEnum
from py2puml.domain.umlrelation import UmlRelation

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
    py2puml.export.puml.UmlClass(name=name, fqn=fqn, attributes=attributes, is_abstract=is_abstract)

@given(name=st.text(), fqn=st.text(), members=st.lists(st.builds(Member)))
def test_fuzz_UmlEnum(
    name: str, fqn: str, members: typing.List[py2puml.domain.umlenum.Member]
) -> None:
    py2puml.export.puml.UmlEnum(name=name, fqn=fqn, members=members)

@given(name=st.text(), fqn=st.text())
def test_fuzz_UmlItem(name: str, fqn: str) -> None:
    py2puml.export.puml.UmlItem(name=name, fqn=fqn)

@given(
    source_fqn=st.text(),
    target_fqn=st.text(),
    type=st.sampled_from(py2puml.domain.umlrelation.RelType),
)
def test_fuzz_UmlRelation(
    source_fqn: str, target_fqn: str, type: py2puml.domain.umlrelation.RelType
) -> None:
    py2puml.export.puml.UmlRelation(source_fqn=source_fqn, target_fqn=target_fqn, type=type)

@given(uml_items=st.lists(st.builds(UmlItem)))
def test_fuzz_puml_namespace_content(
    uml_items: typing.List[py2puml.domain.umlitem.UmlItem],
) -> None:
    py2puml.export.puml.puml_namespace_content(uml_items=uml_items)

@given(
    diagram_name=st.text(),
    uml_items=st.lists(st.builds(UmlItem)),
    uml_relations=st.lists(st.builds(UmlRelation)),
)
def test_fuzz_to_puml_content(
    diagram_name: str,
    uml_items: typing.List[py2puml.domain.umlitem.UmlItem],
    uml_relations: typing.List[py2puml.domain.umlrelation.UmlRelation],
) -> None:
    py2puml.export.puml.to_puml_content(
        diagram_name=diagram_name, uml_items=uml_items, uml_relations=uml_relations
    )