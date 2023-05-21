import py2puml.domain.package as module_0

def test_package_returns_empty():
    str_0 = None
    package_0 = module_0.Package(str_0)
    assert package_0.name is None
    assert package_0.children == []
    assert package_0.items_number == 0
    assert module_0.Package.items_number == 0

def test_for_initializing_package_object_with_name_and_default_values():
    package = module_0.Package("Folder")
    assert package.name == "Folder"
    assert package.children == []
    assert package.items_number == 0

def test_for_updating_item_number_of_package():
    package = module_0.Package("Folder")
    package.items_number = 10
    assert package.items_number == 10

def test_for_updating_the_name_of_package():
    package = module_0.Package("Folder")
    package.name = "Updated Folder"
    assert package.name == "Updated Folder"

def test_for_adding_a_child_to_package():
    package = module_0.Package("Folder")
    child = module_0.Package("Child")
    package.children.append(child)
    assert package.children == [child]

def test_for_initializing_package_object_with_name_and_children():
    child1 = module_0.Package("Child1")
    child2 = module_0.Package("Child2")
    package = module_0.Package("Folder", [child1, child2])
    assert package.name == "Folder"
    assert package.children == [child1, child2]
    assert package.items_number == 0

def test_for_adding_multiple_children_to_package():
    child1 = module_0.Package("Child1")
    child2 = module_0.Package("Child2")
    child3 = module_0.Package("Child3")
    package = module_0.Package("Folder", [child1])
    package.children.extend([child2, child3])
    assert package.children == [child1, child2, child3]

def test_for_updating_items_number_of_package_with_negative_value():
    package = module_0.Package("Folder")
    package.items_number = -5
    assert package.items_number == -5

def test_for_modifying_a_child_within_package():
    child1 = module_0.Package("Child1")
    child2 = module_0.Package("Child2")
    package = module_0.Package("Folder", [child1, child2])
    child2.name = "Updated Child2"
    assert package.children[1].name == "Updated Child2"

def test_for_removing_a_child_from_package():
    child1 = module_0.Package("Child1")
    child2 = module_0.Package("Child2")
    package = module_0.Package("Folder", [child1, child2])
    package.children.remove(child1)
    assert package.children == [child2]

def test_for_checking_equality_between_two_packages():
    package1 = module_0.Package("Folder")
    package2 = module_0.Package("Folder")
    assert package1 == package2

def test_for_checking_inequality_between_two_packages():
    package1 = module_0.Package("Folder1")
    package2 = module_0.Package("Folder2")
    assert package1 != package2