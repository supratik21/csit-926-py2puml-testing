import py2puml.domain.umlrelation as module_0

def test_case_0():
    str_0 = 'X'
    str_1 = '--l$=aMZREtk?~'
    rel_type_0 = module_0.RelType.INHERITANCE
    uml_relation_0 = module_0.UmlRelation(str_0, str_1, rel_type_0)
    assert uml_relation_0.source_fqn == 'X'
    assert uml_relation_0.target_fqn == '--l$=aMZREtk?~'
    assert uml_relation_0.type == module_0.RelType.INHERITANCE

def test_case_initializing_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    assert uml_relation.source_fqn == "SourceFQN"
    assert uml_relation.target_fqn == "TargetFQN"
    assert uml_relation.type == module_0.RelType.COMPOSITION

def test_for_comparing_two_umlrelation_with_same_source_fqn_and_target_fqn():
    uml_relation1 = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation2 = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    assert uml_relation1 == uml_relation2

def test_for_comparing_two_umlrelation_with_diff_source_fqn():
    uml_relation1 = module_0.UmlRelation(source_fqn="SourceFQN1", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation2 = module_0.UmlRelation(source_fqn="SourceFQN2", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    assert uml_relation1 != uml_relation2

def test_for_comparing_two_umlrelation_with_diff_target_fqn():
    uml_relation1 = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN1", type=module_0.RelType.COMPOSITION)
    uml_relation2 = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN2", type=module_0.RelType.COMPOSITION)
    assert uml_relation1 != uml_relation2

def test_for_comparing_two_umlrelation_with_diff_type():
    uml_relation1 = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation2 = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.INHERITANCE)
    assert uml_relation1 != uml_relation2

def test_for_comparing_umlrelation_with_diff_types_of_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    other_object = "SomeString"
    assert uml_relation != other_object


def test_case_for_updating_source_fqn_attribute_in_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation.source_fqn = "UpdatedSourceFQN"
    assert uml_relation.source_fqn == "UpdatedSourceFQN"

def test_case_for_updating_target_fqn_attribute_in_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation.target_fqn = "UpdatedTargetFQN"
    assert uml_relation.target_fqn == "UpdatedTargetFQN"

def test_case_for_updating_type_attribute_in_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation.type = module_0.RelType.INHERITANCE
    assert uml_relation.type == module_0.RelType.INHERITANCE

def test_case_for_updating_source_fqn_and_target_fqn_both_attributes_in_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation.source_fqn = "UpdatedSourceFQN"
    uml_relation.target_fqn = "UpdatedTargetFQN"
    assert uml_relation.source_fqn == "UpdatedSourceFQN"
    assert uml_relation.target_fqn == "UpdatedTargetFQN"

def test_case_for_updating_source_fqn_and_type_both_attributes_in_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation.source_fqn = "UpdatedSourceFQN"
    uml_relation.type = module_0.RelType.INHERITANCE
    assert uml_relation.source_fqn == "UpdatedSourceFQN"
    assert uml_relation.type == module_0.RelType.INHERITANCE

def test_case_for_updating_target_fqn_and_type_both_attributes_in_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation.target_fqn = "UpdatedTargetFQN"
    uml_relation.type = module_0.RelType.INHERITANCE
    assert uml_relation.target_fqn == "UpdatedTargetFQN"
    assert uml_relation.type == module_0.RelType.INHERITANCE

def test_case_for_updating_all_attributes_in_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    uml_relation.source_fqn = "UpdatedSourceFQN"
    uml_relation.target_fqn = "UpdatedTargetFQN"
    uml_relation.type = module_0.RelType.INHERITANCE
    assert uml_relation.source_fqn == "UpdatedSourceFQN"
    assert uml_relation.target_fqn == "UpdatedTargetFQN"
    assert uml_relation.type == module_0.RelType.INHERITANCE

def test_for_checking_string_representation_of_umlrelation_object():
    uml_relation = module_0.UmlRelation(source_fqn="SourceFQN", target_fqn="TargetFQN", type=module_0.RelType.COMPOSITION)
    expected_string = "UmlRelation(source_fqn='SourceFQN', target_fqn='TargetFQN', type=<RelType.COMPOSITION: '*'>)"
    assert str(uml_relation) == expected_string

def test_case_for_checking_presence_of_reltype_enum_value():
    assert module_0.RelType.COMPOSITION in module_0.RelType
    assert module_0.RelType.INHERITANCE in module_0.RelType