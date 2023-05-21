from typing import Dict, List
from py2puml.domain.umlenum import UmlEnum, Member
from py2puml.domain.umlitem import UmlItem
from py2puml.domain.umlrelation import UmlRelation
from py2puml.inspection.inspectmodule import inspect_domain_definition
from tests.modules.withenum import TimeUnit
import py2puml.inspection.inspectenum as module_0
import enum
import py2puml.inspection.inspectenum
import py2puml.domain.umlenum
import py2puml.domain.umlitem
import typing
from enum import Enum
from hypothesis import given, strategies as st
from py2puml.inspection.inspectenum import Member

def assert_member(member: Member, expected_name: str, expected_value: str):
    assert member.name == expected_name
    assert member.value == expected_value

def test_inspect_enum_type():
    domain_items_by_fqn: Dict[str, UmlItem] = {}
    domain_relations: List[UmlRelation] = []
    inspect_domain_definition(TimeUnit, 'tests.modules.withenum', domain_items_by_fqn, domain_relations)

    umlitems_by_fqn = list(domain_items_by_fqn.items())
    assert len(umlitems_by_fqn) == 1, 'one enum must be inspected'
    umlenum: UmlEnum
    fqn, umlenum = umlitems_by_fqn[0]
    assert fqn == 'tests.modules.withenum.TimeUnit'
    assert umlenum.fqn == fqn
    assert umlenum.name == 'TimeUnit'
    members: List[Member] = umlenum.members
    assert len(members) == 3, 'enum has 3 members'
    assert_member(members[0], 'DAYS', 'd')
    assert_member(members[1], 'HOURS', 'h')
    assert_member(members[2], 'MINUTE', 'm')

    assert len(domain_relations) == 0, 'inspecting enum must add no relation'

def test_case_0():
    try:
        str_0 = 'ps'
        dict_0 = {}
        var_0 = module_0.inspect_enum_type(str_0, str_0, dict_0)
    except BaseException:
        pass

@given(name=st.text(), value=st.text())
def test_fuzz_Member(name: str, value: str) -> None:
    py2puml.inspection.inspectenum.Member(name=name, value=value)

@given(name=st.text(), fqn=st.text(), members=st.lists(st.builds(Member)))
def test_fuzz_UmlEnum(
    name: str, fqn: str, members: typing.List[py2puml.domain.umlenum.Member]
) -> None:
    py2puml.inspection.inspectenum.UmlEnum(name=name, fqn=fqn, members=members)

@given(name=st.text(), fqn=st.text())
def test_fuzz_UmlItem(name: str, fqn: str) -> None:
    py2puml.inspection.inspectenum.UmlItem(name=name, fqn=fqn)

@given(
    enum_type=st.just(Enum),
    enum_type_fqn=st.text(),
    domain_items_by_fqn=st.dictionaries(keys=st.text(), values=st.builds(UmlItem)),
)
def test_fuzz_inspect_enum_type(
    enum_type: typing.Type[enum.Enum],
    enum_type_fqn: str,
    domain_items_by_fqn: typing.Dict[str, py2puml.domain.umlitem.UmlItem],
) -> None:
    py2puml.inspection.inspectenum.inspect_enum_type(
        enum_type=enum_type,
        enum_type_fqn=enum_type_fqn,
        domain_items_by_fqn=domain_items_by_fqn,
    )