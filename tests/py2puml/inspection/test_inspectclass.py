from typing import Dict, List
from importlib import import_module
from string import ascii_letters
from py2puml.domain.umlitem import UmlItem
from py2puml.domain.umlclass import UmlClass, UmlAttribute
from py2puml.domain.umlrelation import UmlRelation, RelType
from py2puml.inspection.inspectmodule import inspect_module
from tests.modules.withinheritancewithinmodule import Animal, Fish, Light, GlowingFish
from tests.asserts.attribute import assert_attribute
from tests.asserts.relation import assert_relation
import dataclasses
import py2puml.inspection.inspectclass
import py2puml.domain.umlclass
import py2puml.domain.umlitem
import py2puml.domain.umlrelation
import py2puml.parsing.moduleresolver
import typing
from hypothesis import given, strategies as st
from py2puml.inspection.inspectclass import ModuleResolver, UmlAttribute, UmlRelation, dataclass
import py2puml.inspection.inspectclass as module_0

def test_inspect_module_returns_valid_output_for_basic_classs(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn or domain_relations

def test_inspect_module_spits_domain_items_by_fqn_for_basic_types(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn

def test_inspect_module_spits_domain_relations_for_basic_types_without_relation(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations == []

def test_inspect_module_should_identify_correct_number_of_classes_for_basic_types(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    assert len(domain_items_by_fqn) == 1, '1 class must be inspected'

def test_inspect_module_should_identify_attributes_in_basic_type_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    assert len(contact_umlitem.attributes) == 4, '4 attributes of Contact must be inspected'

def test_inspect_module_should_map_attributes_in_basic_type_class_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert_attribute(fullname_attribute, 'full_name', 'str', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_basic_type_class_first_attribute_map_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert fullname_attribute == UmlAttribute(name='full_name', type='str', static=False)

def test_inspect_module_should_map_attributes_in_basic_type_class_second_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert_attribute(age_attribute, 'age', 'int', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_basic_type_class_second_attribute_map_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert age_attribute == UmlAttribute(name='age', type='int', static=False)

def test_inspect_module_should_map_attributes_in_basic_type_class_third_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert_attribute(weight_attribute, 'weight', 'float', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_basic_type_class_third_attribute_map_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert weight_attribute == UmlAttribute(name='weight', type='float', static=False)

def test_inspect_module_should_map_attributes_in_basic_type_class_fourth_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert_attribute(tongue_attribute, 'can_twist_tongue', 'bool', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_basic_type_class_fourth_attribute_map_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert tongue_attribute == UmlAttribute(name='can_twist_tongue', type='bool', static=False)


def test_inspect_module_depicts_basic_type_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withbasictypes'),
        'tests.modules.withbasictypes',
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 1, '1 class must be inspected'
    # Contact UmlClass
    contact_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withbasictypes.Contact']
    assert len(contact_umlitem.attributes) == 4, '4 attributes of Coordinates must be inspected'
    fullname_attribute, age_attribute, weight_attribute, tongue_attribute = contact_umlitem.attributes
    assert_attribute(fullname_attribute, 'full_name', 'str', expected_staticity=False)
    assert_attribute(age_attribute, 'age', 'int', expected_staticity=False)
    assert_attribute(weight_attribute, 'weight', 'float', expected_staticity=False)
    assert_attribute(tongue_attribute, 'can_twist_tongue', 'bool', expected_staticity=False)

def test_inspect_module_returns_valid_output_for_withconstructor_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn or domain_relations

def test_inspect_module_spits_domain_items_by_fqn_for_withconstructor_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn

def test_inspect_module_spits_domain_relations_for_withconstructor_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations

def test_inspect_module_should_identify_correct_number_of_classes_having_static_and_instance_attributes(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    assert len(domain_items_by_fqn) == 2, 'two classes must be inspected'

def test_inspect_module_should_identify_static_and_instance_attributes_in_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    # Coordinates UmlClass
    coordinates_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Coordinates']
    assert len(coordinates_umlitem.attributes) == 2, '2 attributes of Coordinates must be inspected'

def test_inspect_module_should_map_static_and_instance_attributes_in_class_first_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    # Coordinates UmlClass
    coordinates_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Coordinates']
    x_attribute, y_attribute = coordinates_umlitem.attributes
    assert x_attribute == UmlAttribute(name='x', type='float', static=False)

def test_inspect_module_should_map_static_and_instance_attributes_in_class_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    # Coordinates UmlClass
    coordinates_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Coordinates']
    x_attribute, y_attribute = coordinates_umlitem.attributes
    assert_attribute(x_attribute, 'x', 'float', expected_staticity=False)

def test_inspect_module_should_map_static_and_instance_attributes_in_class_second_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    # Coordinates UmlClass
    coordinates_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Coordinates']
    x_attribute, y_attribute = coordinates_umlitem.attributes
    assert y_attribute == UmlAttribute(name='y', type='float', static=False)

def test_inspect_module_should_map_static_and_instance_attributes_in_class_second_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    # Coordinates UmlClass
    coordinates_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Coordinates']
    x_attribute, y_attribute = coordinates_umlitem.attributes
    assert_attribute(y_attribute, 'y', 'float', expected_staticity=False)

def test_inspect_module_should_verify_subclass_attribute_in_class_has_PI(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[0].name == "PI"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_PI_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[0].type == "float"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_PI_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[0].static == True

def test_inspect_module_should_verify_subclass_attribute_in_class_has_coordinates(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[1].name == "coordinates"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_coordinates_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[1].type == "Coordinates"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_coordinates_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[1].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_day_unit(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[2].name == "day_unit"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_day_unit_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[2].type == "TimeUnit"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_day_unit_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[2].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_hour_unit(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[3].name == "hour_unit"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_hour_unit_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[3].type == "TimeUnit"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_hour_unit_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[3].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_time_resolution(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[4].name == "time_resolution"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_time_resolution_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[4].type == "Tuple[str, TimeUnit]"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_time_resolution_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[4].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_x(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[5].name == "x"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_x_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[5].type == "int"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_x_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[5].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_y(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[6].name == "y"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_y_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[6].type == "str"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_y_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[6].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_x_unit(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[7].name == "x_unit"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_x_unit_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[7].type == "str"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_x_unit_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[7].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_y_unit(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[8].name == "y_unit"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_y_unit_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[8].type == "str"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_y_unit_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[8].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_z(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[9].name == "z"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_z_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[9].type == None

def test_inspect_module_should_verify_subclass_attribute_in_class_has_z_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[9].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_w(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[10].name == "w"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_w_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[10].type == "int"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_w_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[10].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_u(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[11].name == "u"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_u_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[11].type == None

def test_inspect_module_should_verify_subclass_attribute_in_class_has_u_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[11].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_v(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[12].name == "v"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_v_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[12].type == None

def test_inspect_module_should_verify_subclass_attribute_in_class_has_v_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[12].static == False

def test_inspect_module_should_verify_subclass_attribute_in_class_has_dates(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[13].name == "dates"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_dates_type(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[13].type == "List[date]"

def test_inspect_module_should_verify_subclass_attribute_in_class_has_v_static(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    print(point_umlitem.attributes)
    assert point_umlitem.attributes[13].static == False

def test_inspect_module_should_verify_all_subclass_attribute_in_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    point_expected_attributes = {
        'PI': ('float', True),
        # 'origin': (None, True), # not annotated class variable -> not handled for now
        'coordinates': ('Coordinates', False),
        'day_unit': ('TimeUnit', False),
        'hour_unit': ('TimeUnit', False),
        'time_resolution': ('Tuple[str, TimeUnit]', False),
        'x': ('int', False),
        'y': ('str', False),
        'x_unit': ('str', False),
        'y_unit': ('str', False),
        'z': (None, False),
        'w': ('int', False),
        'u': (None, False),
        'v': (None, False),
        'dates': ('List[date]', False),
    }
    assert len(point_umlitem.attributes) == len(point_expected_attributes), 'all Point attributes must be verified'

def test_inspect_module_should_verify_individual_attributes_of_subclass(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    point_expected_attributes = {
        'PI': ('float', True),
        # 'origin': (None, True), # not annotated class variable -> not handled for now
        'coordinates': ('Coordinates', False),
        'day_unit': ('TimeUnit', False),
        'hour_unit': ('TimeUnit', False),
        'time_resolution': ('Tuple[str, TimeUnit]', False),
        'x': ('int', False),
        'y': ('str', False),
        'x_unit': ('str', False),
        'y_unit': ('str', False),
        'z': (None, False),
        'w': ('int', False),
        'u': (None, False),
        'v': (None, False),
        'dates': ('List[date]', False),
    }
    for attribute_name, (atrribute_type, attribute_staticity) in point_expected_attributes.items():
        point_attribute: UmlAttribute = next((
            attribute
            for attribute in point_umlitem.attributes
            if attribute.name == attribute_name
        ), None)
        assert point_attribute is not None, f'attribute {attribute_name} must be detected'
        assert_attribute(point_attribute, attribute_name, atrribute_type, expected_staticity=attribute_staticity)

def test_inspect_module_should_find_static_and_instance_attributes(
    domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    # Coordinates is a component of Point
    assert len(domain_relations) == 1, '1 composition'

def test_inspect_module_should_find_static_and_instance_attributes_relation(
    domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )
    assert_relation(
        domain_relations[0],
        'tests.modules.withconstructor.Point',
        'tests.modules.withconstructor.Coordinates',
        RelType.COMPOSITION
    )

def test_inspect_module_should_depictstatic_and_instance_attributes(
    domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withconstructor'),
        'tests.modules.withconstructor',
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 2, 'two classes must be inspected'

    # Coordinates UmlClass
    coordinates_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Coordinates']
    assert len(coordinates_umlitem.attributes) == 2, '2 attributes of Coordinates must be inspected'
    x_attribute, y_attribute = coordinates_umlitem.attributes
    assert_attribute(x_attribute, 'x', 'float', expected_staticity=False)
    assert_attribute(y_attribute, 'y', 'float', expected_staticity=False)

    # Point UmlClass
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withconstructor.Point']
    point_expected_attributes = {
        'PI': ('float', True),
        # 'origin': (None, True), # not annotated class variable -> not handled for now
        'coordinates': ('Coordinates', False),
        'day_unit': ('TimeUnit', False),
        'hour_unit': ('TimeUnit', False),
        'time_resolution': ('Tuple[str, TimeUnit]', False),
        'x': ('int', False),
        'y': ('str', False),
        'x_unit': ('str', False),
        'y_unit': ('str', False),
        'z': (None, False),
        'w': ('int', False),
        'u': (None, False),
        'v': (None, False),
        'dates': ('List[date]', False),
    }
    assert len(point_umlitem.attributes) == len(point_expected_attributes), 'all Point attributes must be verified'
    for attribute_name, (atrribute_type, attribute_staticity) in point_expected_attributes.items():
        point_attribute: UmlAttribute = next((
            attribute
            for attribute in point_umlitem.attributes
            if attribute.name == attribute_name
        ), None)
        assert point_attribute is not None, f'attribute {attribute_name} must be detected'
        assert_attribute(point_attribute, attribute_name, atrribute_type, expected_staticity=attribute_staticity)

    # Coordinates is a component of Point
    assert len(domain_relations) == 1, '1 composition'
    assert_relation(
        domain_relations[0],
        'tests.modules.withconstructor.Point',
        'tests.modules.withconstructor.Coordinates',
        RelType.COMPOSITION
    )

def test_inspect_module_returns_valid_output_for_compositon_classs(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn or domain_relations

def test_inspect_module_spits_domain_items_by_fqn_for_composition(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn

def test_inspect_module_spits_domain_relations_for_composition_with_relation(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations

def test_inspect_module_should_identify_correct_number_of_classes_for_composition(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    assert len(domain_items_by_fqn) == 3, '3 classes must be inspected'

def test_inspect_module_should_identify_attributes_in_composition_subclass1(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    assert len(address_umlitem.attributes) == 3, '3 attributes of Address must be Addressed'

def test_inspect_module_should_map_attributes_in_composition_subclass2_first_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert name_attribute == UmlAttribute(name='name', type='str', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert_attribute(name_attribute, 'name', 'str', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_second_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    print(worker_umlitem)
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert colleagues_attribute == UmlAttribute(name='colleagues', type='List[Worker]', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_second_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert_attribute(colleagues_attribute, 'colleagues', 'List[Worker]', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_third_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    print(worker_umlitem)
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert boss_attribute == UmlAttribute(name='boss', type='Worker', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_third_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert_attribute(boss_attribute, 'boss', 'Worker', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_fourth_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    print(worker_umlitem)
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert home_address_attribute == UmlAttribute(name='home_address', type='Address', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_fourth_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert_attribute(home_address_attribute, 'home_address', 'Address', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_fifth_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    print(worker_umlitem)
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert work_address_attribute == UmlAttribute(name='work_address', type='Address', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_fifth_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    name_attribute, colleagues_attribute, boss_attribute, home_address_attribute, work_address_attribute = worker_umlitem.attributes
    assert_attribute(work_address_attribute, 'work_address', 'Address', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass2_is_not_abstract(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    assert worker_umlitem.is_abstract == False

def test_inspect_module_should_map_attributes_in_composition_subclass1_is_not_abstract(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    assert address_umlitem.is_abstract == False

def test_inspect_module_should_map_attributes_in_composition_subclass3_is_not_abstract(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Firm UmlClass
    firm_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Firm']
    assert firm_umlitem.is_abstract == False
   
def test_inspect_module_should_identify_attributes_in_composition_subclass2(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Worker UmlClass
    worker_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Worker']
    assert len(worker_umlitem.attributes) == 5, '5 attributes of Worker must be Addressed'

def test_inspect_module_should_identify_attributes_in_composition_subclass3(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Firm UmlClass
    firm_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Firm']
    assert len(firm_umlitem.attributes) == 2, '2 attributes of Contact must be Addressed'

def test_inspect_module_should_map_attributes_in_composition_subclass3_first_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Firm UmlClass
    firm_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Firm']
    name_attribute, employees_attribute = firm_umlitem.attributes
    assert name_attribute == UmlAttribute(name='name', type='str', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass3_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Firm UmlClass
    firm_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Firm']
    name_attribute, employees_attribute = firm_umlitem.attributes
    assert_attribute(name_attribute, 'name', 'str', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass3_second_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Firm UmlClass
    firm_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Firm']
    name_attribute, employees_attribute = firm_umlitem.attributes
    assert employees_attribute == UmlAttribute(name='employees', type='List[Worker]', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass3_second_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Firm UmlClass
    firm_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Firm']
    name_attribute, employees_attribute = firm_umlitem.attributes
    assert_attribute(employees_attribute, 'employees', 'List[Worker]', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass1_first_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    street_attribute, zipcode_attribute, city_attribute = address_umlitem.attributes
    assert street_attribute == UmlAttribute(name='street', type='str', static=False)
    

def test_inspect_module_should_map_attributes_in_composition_subclass1_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    street_attribute, zipcode_attribute, city_attribute = address_umlitem.attributes
    assert_attribute(street_attribute, 'street', 'str', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass1_second_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    street_attribute, zipcode_attribute, city_attribute = address_umlitem.attributes
    assert zipcode_attribute == UmlAttribute(name='zipcode', type='str', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass1_second_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    street_attribute, zipcode_attribute, city_attribute = address_umlitem.attributes
    assert_attribute(zipcode_attribute, 'zipcode', 'str', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_composition_subclass1_third_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    street_attribute, zipcode_attribute, city_attribute = address_umlitem.attributes
    assert city_attribute == UmlAttribute(name='city', type='str', static=False)

def test_inspect_module_should_map_attributes_in_composition_subclass1_third_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    street_attribute, zipcode_attribute, city_attribute = address_umlitem.attributes
    print(city_attribute)
    assert_attribute(city_attribute, 'city', 'str', expected_staticity=False)

def test_inspect_module_depicts_composition_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcomposition'),
        'tests.modules.withcomposition',
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 3, '3 classes must be inspected'
    # Address UmlClass
    address_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcomposition.Address']
    street_attribute, zipcode_attribute, city_attribute = address_umlitem.attributes
    assert_attribute(street_attribute, 'street', 'str', expected_staticity=False)
    assert_attribute(zipcode_attribute, 'zipcode', 'str', expected_staticity=False)
    assert_attribute(city_attribute, 'city', 'str', expected_staticity=False)

def test_inspect_module_returns_valid_output_for_compound_classs(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn or domain_relations

def test_inspect_module_spits_domain_items_by_fqn_for_compound_with_digits(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn

def test_inspect_module_spits_domain_relations_for_compound_with_digits_with_relation(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations

def test_inspect_module_should_identify_correct_number_of_classes_for_compound_with_digits(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    assert len(domain_items_by_fqn) == 2, '2 classes must be inspected'

def test_inspect_module_should_identify_attributes_in_compound_with_digits_class_subclass1(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    # Address UmlClass
    IPv6_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcompoundtypewithdigits.IPv6']
    assert len(IPv6_umlitem.attributes) == 1, '1 attribute1 of IPv6 must be Addressed'

def test_inspect_module_should_identify_attributes_in_compound_with_digits_class_subclass2(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    # Multicast UmlClass
    multicast_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcompoundtypewithdigits.Multicast']
    assert len(multicast_umlitem.attributes) == 1, '1 attribute1 of Multicast must be Addressed'


def test_inspect_module_should_map_attributes_in_compound_with_digits_subclass1(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    # IPv6 UmlClass
    IPv6_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcompoundtypewithdigits.IPv6']
    address_attribute = IPv6_umlitem.attributes
    assert address_attribute

def test_inspect_module_should_map_attributes_in_compound_with_digits_subclass1_content(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    # IPv6 UmlClass
    IPv6_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcompoundtypewithdigits.IPv6']
    address_attribute = IPv6_umlitem.attributes
    assert address_attribute == [UmlAttribute(name='address', type='str', static=False)]

def test_inspect_module_should_map_attributes_in_compound_with_digits_subclass2(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    # Multicast UmlClass
    Multicast_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcompoundtypewithdigits.Multicast']
    addresses_attribute = Multicast_umlitem.attributes
    assert addresses_attribute

def test_inspect_module_should_map_attributes_in_compound_with_digits_subclass2_content(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )
    # Multicast UmlClass
    Multicast_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcompoundtypewithdigits.Multicast']
    addresses_attribute = Multicast_umlitem.attributes
    assert addresses_attribute == [UmlAttribute(name='addresses', type='List[IPv6]', static=False)]

def test_inspect_module_depicts_compound_with_digits_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withcompoundtypewithdigits'),
        'tests.modules.withcompoundtypewithdigits',
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 2, '2 classes must be inspected'
    # IPv6 UmlClass
    IPv6_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withcompoundtypewithdigits.IPv6']
    address_attribute = IPv6_umlitem.attributes
    assert address_attribute

def test_inspect_module_returns_valid_output_for_withenum_classs(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn or domain_relations

def test_inspect_module_spits_domain_items_by_fqn_for_withenum(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn

def test_inspect_module_spits_domain_relations_for_withenum_with_no_relation(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations == []

def test_inspect_module_should_identify_correct_number_of_classes_for_withenum(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    assert len(domain_items_by_fqn) == 1, '1 class must be inspected'

def test_inspect_module_in_withenum_class_as_uml_item(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    assert TimeUnit_umlitem

def test_inspect_module_should_map_right_number_of_members_in_withenum_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    TimeUnit_members = TimeUnit_umlitem.members
    assert len(TimeUnit_members) == 3, 'All the 3 members of the Enum class are identified'
    
def test_inspect_module_should_map_first_member_in_withenum_subclass(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    TimeUnit_members = TimeUnit_umlitem.members
    assert TimeUnit_members[0].name == "DAYS"

def test_inspect_module_should_map_first_member_value_in_withenum_subclass(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    TimeUnit_members = TimeUnit_umlitem.members
    assert TimeUnit_members[0].value == "d"

def test_inspect_module_should_map_second_member_in_withenum_subclass(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    TimeUnit_members = TimeUnit_umlitem.members
    assert TimeUnit_members[1].name == "HOURS"

def test_inspect_module_should_map_second_member_value_in_withenum_subclass(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    TimeUnit_members = TimeUnit_umlitem.members
    assert TimeUnit_members[1].value == "h"

def test_inspect_module_should_map_third_member_in_withenum_subclass(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    TimeUnit_members = TimeUnit_umlitem.members
    assert TimeUnit_members[2].name == "MINUTE"

def test_inspect_module_should_map_third_member_value_in_withenum_subclass(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    TimeUnit_members = TimeUnit_umlitem.members
    assert TimeUnit_members[2].value == "m"

def test_inspect_module_depicts_withenum_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withenum'),
        'tests.modules.withenum',
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 1, '1 classes must be inspected'
    # TimeUnit UmlClass
    TimeUnit_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withenum.TimeUnit']
    assert TimeUnit_umlitem

def test_inspect_module_returns_valid_output_for_withabstract_classs(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn or domain_relations

def test_inspect_module_spits_domain_items_by_fqn_for_withabstract(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn

def test_inspect_module_spits_domain_relations_for_abstract_with_relation(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations

def test_inspect_module_spits_right_number_for_abstract_classes(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert len(domain_items_by_fqn) == 2, 'two classes must be inspected'

def test_inspect_module_identifies_first_abstract_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    class_template_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withabstract.ClassTemplate']
    assert class_template_umlitem.is_abstract

def test_inspect_module_identifies_second_abstract_class(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    concrete_class_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withabstract.ConcreteClass']
    assert not concrete_class_umlitem.is_abstract

def test_inspect_module_identifies_inheritance_relation_between_abstract_classes(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert len(domain_relations) == 1, 'one inheritance relationship between the two must be inspected'

def test_inspect_module_identifies_source_exists_between_abstract_classes(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations[0].source_fqn

def test_inspect_module_identifies_right_source_between_abstract_classes(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations[0].source_fqn == 'tests.modules.withabstract.ClassTemplate'

def test_inspect_module_identifies_target_exists_between_abstract_classes(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations[0].target_fqn

def test_inspect_module_identifies_right_target_between_abstract_classes(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations[0].target_fqn == 'tests.modules.withabstract.ConcreteClass'

# Abstract
def test_inspect_module_should_find_abstract_class(
    domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withabstract'),
        'tests.modules.withabstract',
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 2, 'two classes must be inspected'

    class_template_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withabstract.ClassTemplate']
    assert class_template_umlitem.is_abstract

    concrete_class_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withabstract.ConcreteClass']
    assert not concrete_class_umlitem.is_abstract

    assert len(domain_relations) == 1, 'one inheritance relationship between the two must be inspected'
    assert domain_relations[0].source_fqn == 'tests.modules.withabstract.ClassTemplate'
    assert domain_relations[0].target_fqn == 'tests.modules.withabstract.ConcreteClass'

def test_inspect_module_parse_class_constructor_should_not_process_inherited_constructor(
    domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    # inspects the two sub-modules
    inspect_module(
        import_module('tests.modules.withinheritedconstructor.point'),
        'tests.modules.withinheritedconstructor.point',
        domain_items_by_fqn, domain_relations
    )
    inspect_module(
        import_module('tests.modules.withinheritedconstructor.metricorigin'),
        'tests.modules.withinheritedconstructor.metricorigin',
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 3, 'three classes must be inspected'

    # Point UmlClass
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritedconstructor.point.Point']
    assert len(point_umlitem.attributes) == 2, '2 attributes of Point must be inspected'
    x_attribute, y_attribute = point_umlitem.attributes
    assert_attribute(x_attribute, 'x', 'float', expected_staticity=False)
    assert_attribute(y_attribute, 'y', 'float', expected_staticity=False)

    # Origin UmlClass
    origin_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritedconstructor.point.Origin']
    assert len(origin_umlitem.attributes) == 1, '1 attribute of Origin must be inspected'
    is_origin_attribute = origin_umlitem.attributes[0]
    assert_attribute(is_origin_attribute, 'is_origin', 'bool', expected_staticity=True)

    # MetricOrigin UmlClass
    metric_origin_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritedconstructor.metricorigin.MetricOrigin']
    assert len(metric_origin_umlitem.attributes) == 1, '1 attribute of MetricOrigin must be inspected'
    unit_attribute = metric_origin_umlitem.attributes[0]
    assert_attribute(unit_attribute, 'unit', 'str', expected_staticity=True)

def test_inspect_module_should_unwrap_decorated_constructor(
    domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withwrappedconstructor'),
        'tests.modules.withwrappedconstructor',
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 2, 'two classes must be inspected'

    # Point UmlClass
    point_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withwrappedconstructor.Point']
    assert len(point_umlitem.attributes) == 2, '2 attributes of Point must be inspected'
    x_attribute, y_attribute = point_umlitem.attributes
    assert_attribute(x_attribute, 'x', 'float', expected_staticity=False)
    assert_attribute(y_attribute, 'y', 'float', expected_staticity=False)

    # PointDecoratedWithoutWrapping UmlClass
    point_without_wrapping_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withwrappedconstructor.PointDecoratedWithoutWrapping']
    assert len(point_without_wrapping_umlitem.attributes) == 0, 'the attributes of the original constructor could not be found, the constructor was not wrapped by the decorator'

def test_inspect_module_should_handle_compound_types_with_numbers_in_their_name(
    domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    fqdn = 'tests.modules.withcompoundtypewithdigits'
    inspect_module(
        import_module(fqdn), fqdn,
        domain_items_by_fqn, domain_relations
    )

    assert len(domain_items_by_fqn) == 2, 'two classes must be inspected'

    # IPv6 UmlClass
    ipv6_umlitem: UmlClass = domain_items_by_fqn[f'{fqdn}.IPv6']
    assert len(ipv6_umlitem.attributes) == 1, '1 attributes of IPv6 must be inspected'
    address_attribute = ipv6_umlitem.attributes[0]
    assert_attribute(address_attribute, 'address', 'str', expected_staticity=False)

    # Multicast UmlClass
    multicast_umlitem: UmlClass = domain_items_by_fqn[f'{fqdn}.Multicast']
    assert len(multicast_umlitem.attributes) == 1, '1 attributes of Multicast must be inspected'
    address_attribute = multicast_umlitem.attributes[0]
    assert_attribute(address_attribute, 'addresses', 'List[IPv6]', expected_staticity=False)

# withinheritancewithinmodule
def test_inspect_module_returns_valid_output_for_inheritancewithinmodule_classs(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn or domain_relations

def test_inspect_module_spits_domain_items_by_fqn_for_inheritancewithinmodule(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    assert domain_items_by_fqn

def test_inspect_module_spits_domain_relations_for_inheritancewithinmodule_with_relation(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    assert domain_relations

def test_inspect_module_should_identify_correct_number_of_classes_for_inheritancewithinmodule(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    assert len(domain_items_by_fqn) == 4, '4 classes must be inspected'

def test_inspect_module_should_identify_attributes_in_inheritancewithinmodule_subclass1(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Animal UmlClass
    animal_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Animal']
    assert len(animal_umlitem.attributes) == 1, '1 attribute of Animal must be Addressed'

def test_inspect_module_should_identify_attributes_in_inheritancewithinmodule_subclass2(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Fish UmlClass
    fish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Fish']
    assert len(fish_umlitem.attributes) == 1, '1 attribute of Fish must be Addressed'

def test_inspect_module_should_identify_attributes_in_inheritancewithinmodule_subclass3(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Light UmlClass
    light_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Light']
    assert len(light_umlitem.attributes) == 1, '1 attributes of Light must be Addressed'


def test_inspect_module_should_identify_attributes_in_inheritancewithinmodule_subclass4(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # GlowingFish UmlClass
    glowingfish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.GlowingFish']
    assert len(glowingfish_umlitem.attributes) == 2, '2 attributes of GlowingFish must be Addressed'

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass1_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Animal UmlClass
    animal_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Animal']
    has_notochord_attribute = animal_umlitem.attributes[0]
    print(has_notochord_attribute)
    assert_attribute(has_notochord_attribute, 'has_notochord', 'bool', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass1_first_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Animal UmlClass
    animal_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Animal']
    has_notochord_attribute = animal_umlitem.attributes[0]
    assert has_notochord_attribute == UmlAttribute(name='has_notochord', type='bool', static=False)


def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass2_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Fish UmlClass
    fish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Fish']
    fins_number_attribute = fish_umlitem.attributes[0]
    assert_attribute(fins_number_attribute, 'fins_number', 'int', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass2_first_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Fish UmlClass
    fish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Fish']
    fins_number_attribute = fish_umlitem.attributes[0]
    assert fins_number_attribute == UmlAttribute(name='fins_number', type='int', static=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass3_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Light UmlClass
    light_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Light']
    luminosity_max_attribute = light_umlitem.attributes[0]
    assert_attribute(luminosity_max_attribute, 'luminosity_max', 'float', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass3_first_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
     # Light UmlClass
    light_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Light']
    luminosity_max_attribute = light_umlitem.attributes[0]
    assert luminosity_max_attribute == UmlAttribute(name='luminosity_max', type='float', static=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass4_first_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # GlowingFish UmlClass
    glowingfish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.GlowingFish']
    glow_for_hunting_attribute = glowingfish_umlitem.attributes[0]
    assert_attribute(glow_for_hunting_attribute, 'glow_for_hunting', 'bool', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass4_first_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
     # GlowingFish UmlClass
    glowingfish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.GlowingFish']
    glow_for_hunting_attribute = glowingfish_umlitem.attributes[0]
    assert glow_for_hunting_attribute == UmlAttribute(name='glow_for_hunting', type='bool', static=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass4_second_attribute(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # GlowingFish UmlClass
    glowingfish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.GlowingFish']
    glow_for_mating_attribute = glowingfish_umlitem.attributes[1]
    assert_attribute(glow_for_mating_attribute, 'glow_for_mating', 'bool', expected_staticity=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass4_second_attribute_structure(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
     # GlowingFish UmlClass
    glowingfish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.GlowingFish']
    glow_for_mating_attribute = glowingfish_umlitem.attributes[1]
    assert glow_for_mating_attribute == UmlAttribute(name='glow_for_mating', type='bool', static=False)

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass1_is_not_abstract(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Animal UmlClass
    animal_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Animal']
    assert animal_umlitem.is_abstract == False

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass2_is_not_abstract(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Fish UmlClass
    fish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Fish']
    assert fish_umlitem.is_abstract == False

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass3_is_not_abstract(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # Light UmlClass
    light_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.Light']
    assert light_umlitem.is_abstract == False

def test_inspect_module_should_map_attributes_in_inheritancewithinmodule_subclass4_is_not_abstract(domain_items_by_fqn: Dict[str, UmlItem], domain_relations: List[UmlRelation]
):
    inspect_module(
        import_module('tests.modules.withinheritancewithinmodule'),
        'tests.modules.withinheritancewithinmodule',
        domain_items_by_fqn, domain_relations
    )
    # GlowingFish UmlClass
    glowingfish_umlitem: UmlClass = domain_items_by_fqn['tests.modules.withinheritancewithinmodule.GlowingFish']
    assert glowingfish_umlitem.is_abstract == False

def test_case_0():
    try:
        str_0 = ">_\tvj1(js\tnxU'"
        dict_0 = None
        list_0 = None
        var_0 = module_0.inspect_class_type(str_0, str_0, str_0, dict_0, list_0)
    except BaseException:
        pass
def test_case_1():
    str_0 = 'vwmyLuDM%):iTJ}%>'
    list_0 = None
    var_0 = module_0.handle_inheritance_relation(str_0, str_0, str_0, list_0)

@given(name=st.text(), type=st.text(), static=st.booleans())
def test_fuzz_UmlAttribute(name: str, type: str, static: bool) -> None:
    py2puml.inspection.inspectclass.UmlAttribute(name=name, type=type, static=static)

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
    py2puml.inspection.inspectclass.UmlClass(
        name=name, fqn=fqn, attributes=attributes, is_abstract=is_abstract
    )

@given(name=st.text(), fqn=st.text())
def test_fuzz_UmlItem(name: str, fqn: str) -> None:
    py2puml.inspection.inspectclass.UmlItem(name=name, fqn=fqn)

@given(
    source_fqn=st.text(),
    target_fqn=st.text(),
    type=st.sampled_from(py2puml.domain.umlrelation.RelType),
)
def test_fuzz_UmlRelation(
    source_fqn: str, target_fqn: str, type: py2puml.domain.umlrelation.RelType
) -> None:
    py2puml.inspection.inspectclass.UmlRelation(source_fqn=source_fqn, target_fqn=target_fqn, type=type)

@given(
    cls=st.none(),
    init=st.booleans(),
    repr=st.booleans(),
    eq=st.booleans(),
    order=st.booleans(),
    unsafe_hash=st.booleans(),
    frozen=st.booleans(),
    match_args=st.booleans(),
    kw_only=st.booleans(),
    slots=st.booleans(),
    weakref_slot=st.booleans(),
)
def test_fuzz_dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
) -> None:
    py2puml.inspection.inspectclass.dataclass(
        cls,
        init=init,
        repr=repr,
        eq=eq,
        order=order,
        unsafe_hash=unsafe_hash,
        frozen=frozen,
    )

@given(
    class_type=st.just(type),
    class_fqn=st.text(),
    root_module_name=st.text(),
    domain_relations=st.lists(st.builds(UmlRelation)),
)
def test_fuzz_handle_inheritance_relation(
    class_type: typing.Type,
    class_fqn: str,
    root_module_name: str,
    domain_relations: typing.List[py2puml.domain.umlrelation.UmlRelation],
) -> None:
    py2puml.inspection.inspectclass.handle_inheritance_relation(
        class_type=class_type,
        class_fqn=class_fqn,
        root_module_name=root_module_name,
        domain_relations=domain_relations,
    )

@given(
    class_type=st.just(type),
    class_type_fqn=st.text(),
    root_module_name=st.text(),
    domain_items_by_fqn=st.dictionaries(keys=st.text(), values=st.builds(UmlItem)),
    domain_relations=st.lists(st.builds(UmlRelation)),
)
def test_fuzz_inspect_class_type(
    class_type: typing.Type,
    class_type_fqn: str,
    root_module_name: str,
    domain_items_by_fqn: typing.Dict[str, py2puml.domain.umlitem.UmlItem],
    domain_relations: typing.List[py2puml.domain.umlrelation.UmlRelation],
) -> None:
    py2puml.inspection.inspectclass.inspect_class_type(
        class_type=class_type,
        class_type_fqn=class_type_fqn,
        root_module_name=root_module_name,
        domain_items_by_fqn=domain_items_by_fqn,
        domain_relations=domain_relations,
    )

@given(
    class_type=st.just(type),
    class_type_fqn=st.text(),
    root_module_name=st.text(),
    domain_items_by_fqn=st.dictionaries(keys=st.text(), values=st.builds(UmlItem)),
    domain_relations=st.lists(st.builds(UmlRelation)),
)
def test_fuzz_inspect_static_attributes(
    class_type: typing.Type,
    class_type_fqn: str,
    root_module_name: str,
    domain_items_by_fqn: typing.Dict[str, py2puml.domain.umlitem.UmlItem],
    domain_relations: typing.List[py2puml.domain.umlrelation.UmlRelation],
) -> None:
    py2puml.inspection.inspectclass.inspect_static_attributes(
        class_type=class_type,
        class_type_fqn=class_type_fqn,
        root_module_name=root_module_name,
        domain_items_by_fqn=domain_items_by_fqn,
        domain_relations=domain_relations,
    )

@given(object=st.builds(object))
def test_fuzz_isabstract(object) -> None:
    py2puml.inspection.inspectclass.isabstract(object=object)

@given(class_type=st.just(type), class_fqn=st.text(), root_module_name=st.text())
def test_fuzz_parse_class_constructor(
    class_type: typing.Type, class_fqn: str, root_module_name: str
) -> None:
    py2puml.inspection.inspectclass.parse_class_constructor(
        class_type=class_type, class_fqn=class_fqn, root_module_name=root_module_name
    )