from typing import Dict, List
from py2puml.domain.umlitem import UmlItem
from py2puml.domain.umlclass import UmlClass
from py2puml.domain.umlrelation import UmlRelation
from py2puml.inspection.inspectmodule import inspect_domain_definition
from collections import namedtuple
from tests.modules.withnamedtuple import Circle
from tests.asserts.attribute import assert_attribute
import py2puml.inspection.inspectnamedtuple as module_0
import py2puml.inspection.inspectnamedtuple
import py2puml.domain.umlclass
import py2puml.domain.umlitem
import typing
from hypothesis import given, strategies as st
from py2puml.inspection.inspectnamedtuple import UmlAttribute
import unittest
from py2puml.domain.umlclass import UmlClass, UmlAttribute
from py2puml.domain.umlitem import UmlItem
from py2puml.inspection.inspectnamedtuple import inspect_namedtuple_type

def test_parse_namedtupled_class():
    domain_items_by_fqn: Dict[str, UmlItem] = {}
    domain_relations: List[UmlRelation] = []
    inspect_domain_definition(Circle, 'tests.modules.withnamedtuple', domain_items_by_fqn, domain_relations)

    umlitems_by_fqn = list(domain_items_by_fqn.items())
    assert len(umlitems_by_fqn) == 1, 'one namedtuple must be inspected'
    namedtupled_class: UmlClass
    fqn, namedtupled_class = umlitems_by_fqn[0]
    assert fqn == 'tests.modules.withnamedtuple.Circle'
    assert namedtupled_class.fqn == fqn
    assert namedtupled_class.name == 'Circle'
    attributes = namedtupled_class.attributes
    assert len(attributes) == 3, '3 attributes must be detected in the namedtupled class'
    assert_attribute(attributes[0], 'x', 'Any', False)
    assert_attribute(attributes[1], 'y', 'Any', False)
    assert_attribute(attributes[2], 'radius', 'Any', False)

    assert len(domain_relations) == 0, 'inspecting namedtuple must add no relation'

def test_case_0():
    try:
        str_0 = 'ps'
        dict_0 = {}
        var_0 = module_0.inspect_namedtuple_type(str_0, str_0, dict_0)
    except BaseException:
        pass

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

class TestInspectNamedTuple(unittest.TestCase):

    def test_inspect_namedtuple_type(self):
        namedtuple_type = namedtuple('Person', ['name', 'age'])
        namedtuple_type_fqn = 'py2puml.domain.Person'
        domain_items_by_fqn = {}

        inspect_namedtuple_type(namedtuple_type, namedtuple_type_fqn, domain_items_by_fqn)

        expected_attributes = [
            UmlAttribute('name', 'Any', False),
            UmlAttribute('age', 'Any', False)
        ]

        self.assertIn(namedtuple_type_fqn, domain_items_by_fqn)
        uml_class = domain_items_by_fqn[namedtuple_type_fqn]
        self.assertIsInstance(uml_class, UmlClass)
        self.assertEqual(uml_class.name, 'Person')
        self.assertEqual(uml_class.fqn, 'py2puml.domain.Person')
        self.assertEqual(uml_class.attributes, expected_attributes)

if __name__ == '__main__':
    unittest.main()
