import py2puml.domain.umlenum as module_0

def test_for_initialing_member_object():
    member = module_0.Member(name="MemberName", value="MemberValue")
    assert member.name == "MemberName"
    assert member.value == "MemberValue"

def test_for_updating_name_of_member():
    member = module_0.Member(name="MemberName", value="MemberValue")
    member.name = "UpdatedName"
    assert member.name == "UpdatedName"

def test_for_intialization_of_umlenum_object_with_default_values():
    uml_enum = module_0.UmlEnum(name="EnumName", fqn="1", members=[])
    assert uml_enum.name == "EnumName"
    assert uml_enum.members == []

def test_for_intialization_of_umlenum_object_with_members():
    member1 = module_0.Member(name="Member1", value="Value1")
    member2 = module_0.Member(name="Member2", value="Value2")
    uml_enum = module_0.UmlEnum(name="EnumName", fqn="1", members=[member1, member2])
    assert uml_enum.name == "EnumName"
    assert uml_enum.members == [member1, member2]

def test_for_updating_member_of_umlenum():
    member1 = module_0.Member(name="Member1", value="Value1")
    member2 = module_0.Member(name="Member2", value="Value2")
    uml_enum = module_0.UmlEnum(name="EnumName", fqn="1", members=[member1])
    uml_enum.members.append(member2)
    assert uml_enum.members == [member1, member2]

def test_for_checking_equality_between_two_member_obejects():
    member1 = module_0.Member(name="MemberName", value="MemberValue")
    member2 = module_0.Member(name="MemberName", value="MemberValue")
    assert member1 == member2

def test_for_checking_inequality_between_two_member_obejects():
    member1 = module_0.Member(name="Member1", value="Member1")
    member2 = module_0.Member(name="Member2", value="Member2")
    assert member1 != member2

def test_for_checking_equality_between_two_umlenum_objects():
    member1 = module_0.Member(name="Member1", value="Value1")
    uml_enum1 = module_0.UmlEnum(name="EnumName", fqn="1", members=[member1])
    uml_enum2 = module_0.UmlEnum(name="EnumName", fqn="1", members=[member1])
    assert uml_enum1 == uml_enum2

def test_for_checking_inequality_between_two_umlenum_objects():
    member1 = module_0.Member(name="Member1", value="Value1")
    member2 = module_0.Member(name="Member2", value="Value2")
    uml_enum1 = module_0.UmlEnum(name="EnumName", fqn="1", members=[member1])
    uml_enum2 = module_0.UmlEnum(name="EnumName", fqn="1", members=[member2])
    assert uml_enum1 != uml_enum2

def test_for_removing_member_from_umlenum():
    member1 = module_0.Member(name="Member1", value="Value1")
    member2 = module_0.Member(name="Member2", value="Value2")
    uml_enum = module_0.UmlEnum(name="EnumName", fqn="1", members=[member1, member2])
    uml_enum.members.remove(member1)
    assert uml_enum.members == [member2]

def test_for_updating_value_of_member():
    member = module_0.Member(name="MemberName", value="Value1")
    member.value = "UpdatedValue"
    assert member.value == "UpdatedValue"

def test_for_checking_string_representation_of_umlenum():
    member1 = module_0.Member(name="Member1", value="Value1")
    member2 = module_0.Member(name="Member2", value="Value2")
    uml_enum = module_0.UmlEnum(name="EnumName", fqn="1", members=[member1, member2])
    expected_string = "UmlEnum(name='EnumName', fqn='1', members=[Member(name='Member1', value='Value1'), Member(name='Member2', value='Value2')])"
    assert str(uml_enum) == expected_string

def test_for_intializing_umlenum_empty_memberlist():
    uml_enum = module_0.UmlEnum(name="EnumName", fqn="1", members=[])
    assert uml_enum.members == []
