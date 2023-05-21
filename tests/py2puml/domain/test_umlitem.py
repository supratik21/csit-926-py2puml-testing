import py2puml.domain.umlitem as module_0

def test_for_initialization_umlitem_object():
    uml_item = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    assert uml_item.name == "ItemName"
    assert uml_item.fqn == "ItemFQN"

def test_for_updating_name_of_umlitem_object():
    uml_item = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    uml_item.name = "UpdatedName"
    assert uml_item.name == "UpdatedName"

def test_for_updating_fqn_of_umlitem_object():
    uml_item = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    uml_item.fqn = "UpdatedFQN"
    assert uml_item.fqn == "UpdatedFQN"

def test_for_checking_equality_between_two_umlitem_object():
    uml_item1 = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    uml_item2 = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    assert uml_item1 == uml_item2

def test_for_checking_inequality_between_two_umlitem_object():
    uml_item1 = module_0.UmlItem(name="Item1", fqn="1")
    uml_item2 = module_0.UmlItem(name="Item2", fqn="2")
    assert uml_item1 != uml_item2

def test_for_checking_string_representation_of_umlitem():
    uml_item = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    expected_string = "UmlItem(name='ItemName', fqn='ItemFQN')"
    assert str(uml_item) == expected_string

def test_for_initializing_umlitem_with_empty_name():
    uml_item = module_0.UmlItem(name="", fqn="ItemFQN")
    assert uml_item.name == ""
    assert uml_item.fqn == "ItemFQN"

def test_for_initializing_umlitem_with_empty_fqn():
    uml_item = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    uml_item.fqn = ""
    assert uml_item.fqn == ""

def test_for_comparing_umlitem_object_with_none():
    uml_item = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    assert uml_item != None

def test_for_comparing_umlitem_object_with_different_type():
    uml_item = module_0.UmlItem(name="ItemName", fqn="ItemFQN")
    other_object = "SomeString"
    assert uml_item != other_object

def test_for_checking_umitem_with_special_character_in_name():
    uml_item = module_0.UmlItem(name="Item#Name", fqn="ItemFQN")
    expected_string = "UmlItem(name='Item#Name', fqn='ItemFQN')"
    assert str(uml_item) == expected_string

def test_for_checking_umitem_with_special_character_in_fqn():
    uml_item = module_0.UmlItem(name="ItemName", fqn="Item#FQN")
    expected_string = "UmlItem(name='ItemName', fqn='Item#FQN')"
    assert str(uml_item) == expected_string

def test_for_checking_umitem_with_special_character_in_name_and_fqn_both():
    uml_item = module_0.UmlItem(name="Item@Name", fqn="Item#FQN")
    expected_string = "UmlItem(name='Item@Name', fqn='Item#FQN')"
    assert str(uml_item) == expected_string

def test_for_checking_umitem_with_empty_character_in_name():
    uml_item = module_0.UmlItem(name="", fqn="ItemFQN")
    expected_string = "UmlItem(name='', fqn='ItemFQN')"
    assert str(uml_item) == expected_string

def test_for_checking_umitem_with_empty_character_in_fqn():
    uml_item = module_0.UmlItem(name="ItemName", fqn="")
    expected_string = "UmlItem(name='ItemName', fqn='')"
    assert str(uml_item) == expected_string

def test_for_checking_umitem_with_empty_character_in_name_and_fqn_both():
    uml_item = module_0.UmlItem(name="", fqn="")
    expected_string = "UmlItem(name='', fqn='')"
    assert str(uml_item) == expected_string

def test_for_checking_umitem_with_only_space_character_in_name():
    uml_item = module_0.UmlItem(name=" ", fqn="ItemFQN")
    expected_string = "UmlItem(name=' ', fqn='ItemFQN')"
    assert str(uml_item) == expected_string

def test_for_checking_umitem_with_only_space_character_in_fqn():
    uml_item = module_0.UmlItem(name="ItemName", fqn=" ")
    expected_string = "UmlItem(name='ItemName', fqn=' ')"
    assert str(uml_item) == expected_string

def test_for_checking_umitem_with_only_space_character_in_name_and_fqn_both():
    uml_item = module_0.UmlItem(name=" ", fqn=" ")
    expected_string = "UmlItem(name=' ', fqn=' ')"
    assert str(uml_item) == expected_string
