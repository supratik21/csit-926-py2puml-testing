import py2puml.domain.umlclass as module_0

def test_initializing_umlattribute_object():
    attribute = module_0.UmlAttribute(name="attribute_name", type="int", static=False)
    assert attribute.name == "attribute_name"
    assert attribute.type == "int"
    assert attribute.static == False

def test_for_updating_name_of_umlattribute():
    attribute = module_0.UmlAttribute(name="attribute_name", type="int", static=False)
    attribute.name = "updated_name"
    assert attribute.name == "updated_name"

def test_for_initializing_umlclass_object_with_default_value():
    uml_class = module_0.UmlClass(name="ClassName", fqn="1", attributes=[])
    assert uml_class.name == "ClassName"
    assert uml_class.attributes == []
    assert uml_class.is_abstract == False

def test_for_initializing_umlclass_object_with_attributes():
    attribute1 = module_0.UmlAttribute(name="attribute1", type="int", static=False)
    attribute2 = module_0.UmlAttribute(name="attribute2", type="str", static=True)
    uml_class = module_0.UmlClass(name= "str", fqn= "1", attributes= [attribute1, attribute2], is_abstract= True)
    assert uml_class.attributes == [attribute1, attribute2]
    assert uml_class.is_abstract == True

def test_for_updating_is_abstract_of_uml_class():
    uml_class = module_0.UmlClass(name="ClassName", fqn= "1", attributes=[])
    uml_class.is_abstract = True
    assert uml_class.is_abstract == True

def test_case_for_adding_new_attribute_to_umlclass():
    attribute1 = module_0.UmlAttribute(name="attribute1", type="int", static=False)
    attribute2 = module_0.UmlAttribute(name="attribute2", type="str", static=True)
    uml_class = module_0.UmlClass(name="ClassName", fqn="1", attributes=[attribute1])
    uml_class.attributes.append(attribute2)
    assert uml_class.attributes == [attribute1, attribute2]

def test_for_updating_type_of_uml_attribute():
    attribute = module_0.UmlAttribute(name="attribute_name", type="int", static=False)
    attribute.type = "float"
    assert attribute.type == "float"

def test_for_modifying_static_flag_of_uml_attribute():
    attribute = module_0.UmlAttribute(name="attribute_name", type="int", static=False)
    attribute.static = True
    assert attribute.static == True

def test_for_setting_umlclass_as_abstract():
    uml_class = module_0.UmlClass(name="ClassName", fqn="1", attributes=[])
    uml_class.is_abstract = True
    assert uml_class.is_abstract == True

def test_for_checking_equality_of_two_uml_attributes():
    attribute1 = module_0.UmlAttribute(name="attribute_name", type="int", static=False)
    attribute2 = module_0.UmlAttribute(name="attribute_name", type="int", static=False)
    assert attribute1 == attribute2

def test_for_checking_inequality_of_two_uml_attributes():
    attribute1 = module_0.UmlAttribute(name="attribute1", type="str", static=False)
    attribute2 = module_0.UmlAttribute(name="attribute2", type="int", static=True)
    assert attribute1 != attribute2

def test_for_checking_equality_of_two_umlclass_object():
    uml_class1 = module_0.UmlClass(name="ClassName", fqn="1", attributes=[])
    uml_class2 = module_0.UmlClass(name="ClassName", fqn ="1", attributes=[])
    assert uml_class1 == uml_class2

def test_for_checking_inequality_of_two_umlclass_object():
    uml_class1 = module_0.UmlClass(name="Class1", fqn="1", attributes=[])
    uml_class2 = module_0.UmlClass(name="Class2", fqn ="2", attributes=[])
    assert uml_class1 != uml_class2

def test_for_removing_attribute_from_umlclass():
    attribute1 = module_0.UmlAttribute(name="attribute1", type="int", static=False)
    attribute2 = module_0.UmlAttribute(name="attribute2", type="str", static=True)
    uml_class = module_0.UmlClass(name="ClassName", fqn="1", attributes=[attribute1, attribute2])
    uml_class.attributes.remove(attribute1)
    assert uml_class.attributes == [attribute2]

def test_for_updating_multiple_aattributes_of_umlclass():
    attribute1 = module_0.UmlAttribute(name="attribute1", type="int", static=False)
    attribute2 = module_0.UmlAttribute(name="attribute2", type="str", static=True)
    uml_class = module_0.UmlClass(name="ClassName", fqn="1", attributes=[attribute1])
    uml_class.attributes[0] = attribute2
    uml_class.is_abstract = True
    assert uml_class.attributes == [attribute2]
    assert uml_class.is_abstract == True

def test_for_checking_string_representation_of_umlclass():
    attribute1 = module_0.UmlAttribute(name="attribute1", type="int", static=False)
    attribute2 = module_0.UmlAttribute(name="attribute2", type="str", static=True)
    uml_class = module_0.UmlClass(name="ClassName", fqn="1", attributes=[attribute1, attribute2], is_abstract=True)
    expected_string = "UmlClass(name='ClassName', fqn='1', attributes=[UmlAttribute(name='attribute1', type='int', static=False), UmlAttribute(name='attribute2', type='str', static=True)], is_abstract=True)"
    assert str(uml_class) == expected_string








