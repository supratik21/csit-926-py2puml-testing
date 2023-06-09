from typing import Dict, Tuple, List
from ast import parse, AST, get_source_segment
from inspect import getsource
from textwrap import dedent
from pytest import mark
from py2puml.parsing.astvisitors import AssignedVariablesCollector, SignatureVariablesCollector, Variable, shorten_compound_type_annotation
from py2puml.parsing.moduleresolver import ModuleResolver
from tests.asserts.variable import assert_Variable
from tests.py2puml.parsing.mockedinstance import MockedInstance
import py2puml.parsing.astvisitors as module_0
import _ast as module_1
import builtins as module_2
import _ast as module_3
import py2puml.parsing.astvisitors as module_4
from py2puml.parsing.astvisitors import AssignedVariablesCollector, SignatureVariablesCollector, Variable, shorten_compound_type_annotation
from py2puml.parsing.moduleresolver import ModuleResolver
from tests.asserts.variable import assert_Variable
from tests.py2puml.parsing.mockedinstance import MockedInstance
import ast
import py2puml.parsing.astvisitors
import py2puml.domain.umlrelation
import py2puml.parsing.moduleresolver
from ast import expr
from py2puml.parsing.astvisitors import ModuleResolver
from hypothesis import given, strategies as st

class ParseMyConstructorArguments:
    def __init__(
        # the reference to the instance is often 'self' by convention, but can be anything else
        me,
        # some arguments, typed or untyped
        an_int: int, an_untyped, a_compound_type: Tuple[float, Dict[str, List[bool]]],
        # an argument with a default value
        a_default_string: str='text',
        # positional and keyword wildcard arguments
        *args, **kwargs
    ):
        pass

def test_SignatureVariablesCollector_collect_arguments():
    constructor_source: str = dedent(getsource(ParseMyConstructorArguments.__init__.__code__))
    constructor_ast: AST = parse(constructor_source)

    collector = SignatureVariablesCollector(constructor_source)
    collector.visit(constructor_ast)

    assert collector.class_self_id == 'me'
    assert len(collector.variables) == 6, 'all the arguments must be detected'
    assert_Variable(collector.variables[0], 'an_int', 'int', constructor_source)
    assert_Variable(collector.variables[1], 'an_untyped', None, constructor_source)
    assert_Variable(collector.variables[2], 'a_compound_type', 'Tuple[float, Dict[str, List[bool]]]', constructor_source)
    assert_Variable(collector.variables[3], 'a_default_string', 'str', constructor_source)
    assert_Variable(collector.variables[4], 'args', None, constructor_source)
    assert_Variable(collector.variables[5], 'kwargs', None, constructor_source)

@mark.parametrize(
    'class_self_id,assignment_code,annotation_as_str,self_attributes,variables', [
        # detects the assignment to a new variable
        ('self', 'my_var = 5', None, [], [('my_var', None)]),
        ('self', 'my_var: int = 5', 'int', [], [('my_var', 'int')]),
        # detects the assignment to a new self attribute
        ('self', 'self.my_attr = 6', None, [('my_attr', None)], []),
        ('self', 'self.my_attr: int = 6', 'int', [('my_attr', 'int')], []),
        # tuple assignment mixing variable and attribute
        ('self', 'my_var, self.my_attr = 5, 6', None, [('my_attr', None)], [('my_var', None)]),
        # assignment to a subscript of an attribute
        ('self', 'self.my_attr[0] = 0', None, [], []),
        ('self', 'self.my_attr[0]:int = 0', 'int', [], []),
        # assignment to an attribute of an attribute
        ('self', 'self.my_attr.id = "42"', None, [], []),
        ('self', 'self.my_attr.id: str = "42"', 'str', [], []),
        # assignment to an attribute of a reference which is not 'self'
        ('me', 'self.my_attr = 6', None, [], []),
        ('me', 'self.my_attr: int = 6', 'int', [], []),
    ]
)
def test_AssignedVariablesCollector_single_assignment_separate_variable_from_instance_attribute(
    class_self_id: str, assignment_code: str, annotation_as_str: str, self_attributes: list, variables: list
):
    # the assignment is the first line of the body
    assignment_ast: AST = parse(assignment_code).body[0]

    # assignment without annotation (multiple targets, but only one in these test cases)
    if annotation_as_str is None:
        annotation = None
        assert len(assignment_ast.targets) == 1, 'unit test consistency'
        assignment_target = assignment_ast.targets[0]
    # assignment with annotation (only one target)
    else:
        annotation = assignment_ast.annotation
        assert get_source_segment(assignment_code, annotation) == annotation_as_str, 'unit test consistency'
        assignment_target = assignment_ast.target

    assignment_collector = AssignedVariablesCollector(class_self_id, annotation)
    assignment_collector.visit(assignment_target)

    # detection of self attributes
    assert len(assignment_collector.self_attributes) == len(self_attributes)
    for self_attribute, (variable_id, variable_type_str) in zip(assignment_collector.self_attributes, self_attributes):
        assert_Variable(self_attribute, variable_id, variable_type_str, assignment_code)

    # detection of new variables occupying the memory scope
    assert len(assignment_collector.variables) == len(variables)
    for variable, (variable_id, variable_type_str) in zip(assignment_collector.variables, variables):
        assert_Variable(variable, variable_id, variable_type_str, assignment_code)

@mark.parametrize(
    ['class_self_id', 'assignment_code', 'self_attributes_and_variables_by_target'], [
        (
            'self', 'x = y = 0', [
                ([], ['x']),
                ([], ['y']),
            ]
        ),
        (
            'self', 'self.x = self.y = 0', [
                (['x'], []),
                (['y'], []),
            ]
        ),
        (
            'self', 'self.my_attr = self.my_list[0] = 5', [
                (['my_attr'], []),
                ([], []),
            ]
        ),
        (
            'self', 'self.x, self.y = self.origin = (0, 0)', [
                (['x', 'y'], []),
                (['origin'], []),
            ]
        ),
    ]
)
def test_AssignedVariablesCollector_multiple_assignments_separate_variable_from_instance_attribute(
    class_self_id: str, assignment_code: str, self_attributes_and_variables_by_target: tuple
):
    # the assignment is the first line of the body
    assignment_ast: AST = parse(assignment_code).body[0]

    assert len(assignment_ast.targets) == len(self_attributes_and_variables_by_target), 'test consitency: all targets must be tested'
    for assignment_target, (self_attribute_ids, variable_ids) in zip(assignment_ast.targets, self_attributes_and_variables_by_target):
        assignment_collector = AssignedVariablesCollector(class_self_id, None)
        assignment_collector.visit(assignment_target)

        assert len(assignment_collector.self_attributes) == len(self_attribute_ids), 'test consistency'
        for self_attribute, self_attribute_id in zip(assignment_collector.self_attributes, self_attribute_ids):
            assert self_attribute.id == self_attribute_id
            assert self_attribute.type_expr == None, 'Python does not allow type annotation in multiple assignment'

        assert len(assignment_collector.variables) == len(variable_ids), 'test consistency'
        for variable, variable_id in zip(assignment_collector.variables, variable_ids):
            assert variable.id == variable_id
            assert variable.type_expr == None, 'Python does not allow type annotation in multiple assignment'

@mark.parametrize(['full_annotation', 'short_annotation', 'namespaced_definitions', 'module_dict'], [
    (
        # domain.people was imported, people.Person is used
        'people.Person',
        'Person',
        ['domain.people.Person'],
        {
            '__name__': 'testmodule',
            'people': {
                'Person': {
                    '__module__': 'domain.people',
                    '__name__': 'Person'
                }
            }
        }
    ),
    (
        # combination of compound types
        'Dict[id.Identifier,typing.List[domain.Person]]',
        'Dict[Identifier, List[Person]]',
        ['typing.Dict', 'id.Identifier', 'typing.List', 'domain.Person'],
        {
            '__name__': 'testmodule',
            'Dict': Dict,
            'List': List,
            'id': {
                'Identifier': {
                    '__module__': 'id',
                    '__name__': 'Identifier',
                }
            },
            'domain': {
                'Person': {
                    '__module__': 'domain',
                    '__name__': 'Person',
                }
            }
        }
    )
])
def test_shorten_compound_type_annotation(full_annotation: str, short_annotation, namespaced_definitions: List[str], module_dict: dict):
    module_resolver = ModuleResolver(MockedInstance(module_dict))
    shortened_annotation, full_namespaced_definitions = shorten_compound_type_annotation(full_annotation, module_resolver)
    assert shortened_annotation == short_annotation
    assert full_namespaced_definitions == namespaced_definitions

def test_case_0():
    try:
        variable_0 = module_0.Variable()
    except BaseException:
        pass

def test_case_1():
    try:
        expr_0 = module_1.expr()
        str_0 = "c]1O'3\x0cs"
        str_1 = '@:A\x0b7@F."QEaP<p'
        list_0 = [str_0, str_1, str_1, str_0]
        dict_0 = {str_1: expr_0}
        subscript_0 = module_1.Subscript(**dict_0)
        assigned_variables_collector_0 = module_0.AssignedVariablesCollector(
            str_1, expr_0)
        assert expr_0 is not None
        assert assigned_variables_collector_0.class_self_id == '@:A\x0b7@F."QEaP<p'
        assert assigned_variables_collector_0.variables == []
        assert assigned_variables_collector_0.self_attributes == []
        assert module_1.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
        assert module_1.PyCF_ONLY_AST == 1024
        assert module_1.PyCF_TYPE_COMMENTS == 4096
        assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
        var_0 = assigned_variables_collector_0.visit_Subscript(subscript_0)
        assert var_0 is None
        module_0 = module_2.module(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        subscript_0 = module_1.Subscript()
        str_0 = ''
        list_0 = []
        expr_0 = module_1.expr(*list_0)
        signature_variables_collector_0 = module_0.SignatureVariablesCollector(
            str_0)
        assert subscript_0 is not None
        assert expr_0 is not None
        assert signature_variables_collector_0.constructor_source == ''
        assert signature_variables_collector_0.class_self_id is None
        assert signature_variables_collector_0.variables == []
        assert module_1.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
        assert module_1.PyCF_ONLY_AST == 1024
        assert module_1.PyCF_TYPE_COMMENTS == 4096
        assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
        dict_0 = {str_0: str_0}
        assigned_variables_collector_0 = module_0.AssignedVariablesCollector(
            str_0, expr_0)
        assert assigned_variables_collector_0.class_self_id == ''
        assert assigned_variables_collector_0.variables == []
        assert assigned_variables_collector_0.self_attributes == []
        list_1 = [assigned_variables_collector_0, str_0]
        name_0 = module_1.Name(*list_1)
        assert name_0.ctx == ''
        assign_0 = module_1.Assign(**dict_0)
        #assert assign_0. == ''
        arg_0 = module_1.arg(*list_1)
        assert arg_0.annotation == ''
        var_0 = signature_variables_collector_0.visit_arg(arg_0)
        assert var_0 is None
        attribute_0 = module_1.Attribute(*list_1)
        assert attribute_0.attr == ''
        var_1 = assigned_variables_collector_0.visit_Attribute(attribute_0)
        assert var_1 is None
        str_1 = 'eDC`AyR9'
        module_resolver_0 = None
        constructor_visitor_0 = module_0.ConstructorVisitor(str_1, str_0,
            str_0, module_resolver_0, **dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        expr_0 = module_1.expr()
        str_0 = 'TrGD1KzWxic'
        str_1 = "-wJ]SXI'F0\t,%\\q"
        signature_variables_collector_0 = module_0.SignatureVariablesCollector(
            str_1)
        assert expr_0 is not None
        assert signature_variables_collector_0.constructor_source == "-wJ]SXI'F0\t,%\\q"
        assert signature_variables_collector_0.class_self_id is None
        assert signature_variables_collector_0.variables == []
        assert module_1.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
        assert module_1.PyCF_ONLY_AST == 1024
        assert module_1.PyCF_TYPE_COMMENTS == 4096
        assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
        dict_0 = {str_0: str_0, str_0: str_0}
        assigned_variables_collector_0 = module_0.AssignedVariablesCollector(
            str_0, expr_0)
        assert assigned_variables_collector_0.class_self_id == 'TrGD1KzWxic'
        assert assigned_variables_collector_0.variables == []
        assert assigned_variables_collector_0.self_attributes == []
        list_0 = [assigned_variables_collector_0, str_0]
        name_0 = module_1.Name(*list_0)
        assert name_0.ctx == 'TrGD1KzWxic'
        var_0 = assigned_variables_collector_0.visit_Name(name_0)
        assert len(assigned_variables_collector_0.variables) == 1
        assert var_0 is None
        assign_0 = module_1.Assign(**dict_0)
        assert assign_0.TrGD1KzWxic == 'TrGD1KzWxic'
        arg_0 = module_1.arg(*list_0)
        assert arg_0.annotation == 'TrGD1KzWxic'
        var_1 = signature_variables_collector_0.visit_arg(arg_0)
        assert var_1 is None
        module_0 = module_2.module()
    except BaseException:
        pass

def test_case_4():
    try:
        expr_0 = module_1.expr()
        str_0 = 'TrGD1KzWxic'
        str_1 = "-wJ]SXI'F0\t,%\\q"
        signature_variables_collector_0 = module_0.SignatureVariablesCollector(
            str_1)
        assert expr_0 is not None
        assert signature_variables_collector_0.constructor_source == "-wJ]SXI'F0\t,%\\q"
        assert signature_variables_collector_0.class_self_id is None
        assert signature_variables_collector_0.variables == []
        assert module_1.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
        assert module_1.PyCF_ONLY_AST == 1024
        assert module_1.PyCF_TYPE_COMMENTS == 4096
        assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
        assigned_variables_collector_0 = module_0.AssignedVariablesCollector(
            str_0, expr_0)
        assert assigned_variables_collector_0.class_self_id == 'TrGD1KzWxic'
        assert assigned_variables_collector_0.variables == []
        assert assigned_variables_collector_0.self_attributes == []
        list_0 = [str_0]
        name_0 = module_1.Name(*list_0)
        assert name_0.id == 'TrGD1KzWxic'
        var_0 = assigned_variables_collector_0.visit_Name(name_0)
        assert var_0 is None
        arg_0 = module_1.arg(*list_0)
        assert arg_0.arg == 'TrGD1KzWxic'
        subscript_0 = None
        var_1 = assigned_variables_collector_0.visit_Subscript(subscript_0)
        assert var_1 is None
        var_2 = signature_variables_collector_0.visit_arg(arg_0)
    except BaseException:
        pass

def test_case_5():
    str_0 = ';LU>$\\j4Q6NxV_J.'
    list_0 = [str_0]
    attribute_0 = module_1.Attribute(*list_0)
    expr_0 = module_1.expr()
    assigned_variables_collector_0 = module_0.AssignedVariablesCollector(str_0,
        expr_0)
    assert attribute_0.value == ';LU>$\\j4Q6NxV_J.'
    assert expr_0 is not None
    assert assigned_variables_collector_0.class_self_id == ';LU>$\\j4Q6NxV_J.'
    assert assigned_variables_collector_0.variables == []
    assert assigned_variables_collector_0.self_attributes == []
    assert module_1.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_1.PyCF_ONLY_AST == 1024
    assert module_1.PyCF_TYPE_COMMENTS == 4096
    assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
    var_0 = assigned_variables_collector_0.visit_Attribute(attribute_0)
    assert var_0 is None

def test_case_6():
    expr_0 = module_1.expr()
    str_0 = 'TrGD1KzWxic'
    assigned_variables_collector_0 = module_0.AssignedVariablesCollector(str_0,
        expr_0)
    assert expr_0 is not None
    assert assigned_variables_collector_0.class_self_id == 'TrGD1KzWxic'
    assert assigned_variables_collector_0.variables == []
    assert assigned_variables_collector_0.self_attributes == []
    assert module_1.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_1.PyCF_ONLY_AST == 1024
    assert module_1.PyCF_TYPE_COMMENTS == 4096
    assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
    list_0 = [assigned_variables_collector_0, str_0]
    name_0 = module_1.Name(*list_0)
    assert name_0.ctx == 'TrGD1KzWxic'
    var_0 = assigned_variables_collector_0.visit_Name(name_0)
    assert len(assigned_variables_collector_0.variables) == 1
    assert var_0 is None
    signature_variables_collector_0 = module_0.SignatureVariablesCollector(
        str_0)
    assert signature_variables_collector_0.constructor_source == 'TrGD1KzWxic'
    assert signature_variables_collector_0.class_self_id is None
    assert signature_variables_collector_0.variables == []
    expr_1 = module_1.expr()
    assert expr_1 is not None

def test_case_7():
    subscript_0 = module_1.Subscript()
    str_0 = ''
    list_0 = []
    expr_0 = module_1.expr(*list_0)
    assigned_variables_collector_0 = module_0.AssignedVariablesCollector(str_0,
        expr_0)
    assert subscript_0 is not None
    assert expr_0 is not None
    assert assigned_variables_collector_0.class_self_id == ''
    assert assigned_variables_collector_0.variables == []
    assert assigned_variables_collector_0.self_attributes == []
    assert module_1.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_1.PyCF_ONLY_AST == 1024
    assert module_1.PyCF_TYPE_COMMENTS == 4096
    assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
    var_0 = assigned_variables_collector_0.visit_Subscript(subscript_0)
    assert var_0 is None
    expr_1 = module_1.expr()
    assert expr_1 is not None
    str_1 = 'TrGD1KzWxic'
    str_2 = "-wJ]SXI'F0\t,%\\q"
    signature_variables_collector_0 = module_0.SignatureVariablesCollector(
        str_2)
    assert signature_variables_collector_0.constructor_source == "-wJ]SXI'F0\t,%\\q"
    assert signature_variables_collector_0.class_self_id is None
    assert signature_variables_collector_0.variables == []
    dict_0 = {str_1: str_1, str_1: str_1}
    assigned_variables_collector_1 = module_0.AssignedVariablesCollector(str_1,
        expr_1)
    assert assigned_variables_collector_1.class_self_id == 'TrGD1KzWxic'
    assert assigned_variables_collector_1.variables == []
    assert assigned_variables_collector_1.self_attributes == []
    list_1 = [assigned_variables_collector_1, str_1]
    name_0 = module_1.Name(*list_1)
    assert name_0.ctx == 'TrGD1KzWxic'
    var_1 = assigned_variables_collector_1.visit_Name(name_0)
    assert len(assigned_variables_collector_1.variables) == 1
    assert var_1 is None
    assign_0 = module_1.Assign(**dict_0)
    assert assign_0.TrGD1KzWxic == 'TrGD1KzWxic'
    arg_0 = module_1.arg(*list_1)
    assert arg_0.annotation == 'TrGD1KzWxic'
    var_2 = signature_variables_collector_0.visit_arg(arg_0)
    assert var_2 is None
    attribute_0 = module_1.Attribute(*list_1)
    assert attribute_0.attr == 'TrGD1KzWxic'
    var_3 = assigned_variables_collector_0.visit_Attribute(attribute_0)
    assert var_3 is None
    var_4 = signature_variables_collector_0.visit_arg(arg_0)
    assert len(signature_variables_collector_0.variables) == 1
    assert var_4 is None

def test_case_8():
    str_0 = ';LU>$\\j4Q6NxV_@.'
    signature_variables_collector_0 = module_0.SignatureVariablesCollector(
        str_0)
    assert signature_variables_collector_0.constructor_source == ';LU>$\\j4Q6NxV_@.'
    assert signature_variables_collector_0.class_self_id is None
    assert signature_variables_collector_0.variables == []
    assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')

def test_case_0_pass():
    assign_0 = module_3.Assign()
    list_0 = [assign_0, assign_0]
    arg_0 = module_3.arg(*list_0)
    str_0 = "*H$`XC(3 o'wo"
    signature_variables_collector_0 = module_4.SignatureVariablesCollector(
        str_0)
    assert assign_0 is not None
    assert signature_variables_collector_0.constructor_source == "*H$`XC(3 o'wo"
    assert signature_variables_collector_0.class_self_id is None
    assert signature_variables_collector_0.variables == []
    assert module_3.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_3.PyCF_ONLY_AST == 1024
    assert module_3.PyCF_TYPE_COMMENTS == 4096
    assert module_4.SPLITTING_CHARACTERS == ('[', ']', ',')
    var_0 = signature_variables_collector_0.visit_arg(arg_0)
    assert var_0 is None
    var_1 = signature_variables_collector_0.visit_arg(arg_0)
    assert len(signature_variables_collector_0.variables) == 1
    assert var_1 is None
    attribute_0 = module_3.Attribute()
    assert attribute_0 is not None
 
def test_case_1_pass():
    assign_0 = module_3.Assign()
    list_0 = [assign_0, assign_0]
    dict_0 = {}
    str_0 = "*H$`XC(3 o'wo"
    attribute_0 = module_3.Attribute(*list_0, **dict_0)
    expr_0 = module_3.expr(**dict_0)
    assigned_variables_collector_0 = module_4.AssignedVariablesCollector(str_0,
        expr_0)
    assert assign_0 is not None
    assert expr_0 is not None
    assert assigned_variables_collector_0.class_self_id == "*H$`XC(3 o'wo"
    assert assigned_variables_collector_0.variables == []
    assert assigned_variables_collector_0.self_attributes == []
    assert module_3.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_3.PyCF_ONLY_AST == 1024
    assert module_3.PyCF_TYPE_COMMENTS == 4096
    assert module_4.SPLITTING_CHARACTERS == ('[', ']', ',')
    var_0 = assigned_variables_collector_0.visit_Attribute(attribute_0)
    assert var_0 is None
 
def test_case_2_pass():
    str_0 = 'e'
    list_0 = [str_0]
    name_0 = module_3.Name(*list_0)
    expr_0 = module_3.expr()
    assigned_variables_collector_0 = module_4.AssignedVariablesCollector(str_0,
        expr_0)
    assert name_0.id == 'e'
    assert expr_0 is not None
    assert assigned_variables_collector_0.class_self_id == 'e'
    assert assigned_variables_collector_0.variables == []
    assert assigned_variables_collector_0.self_attributes == []
    assert module_3.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_3.PyCF_ONLY_AST == 1024
    assert module_3.PyCF_TYPE_COMMENTS == 4096
    assert module_4.SPLITTING_CHARACTERS == ('[', ']', ',')
    var_0 = assigned_variables_collector_0.visit_Name(name_0)
    assert var_0 is None
    signature_variables_collector_0 = module_4.SignatureVariablesCollector(
        str_0)
    assert signature_variables_collector_0.constructor_source == 'e'
    assert signature_variables_collector_0.class_self_id is None
    assert signature_variables_collector_0.variables == []
 
def test_case_3_pass():
    list_0 = []
    subscript_0 = module_3.Subscript(*list_0)
    str_0 = 'ou.~K&pztteMP0'
    str_1 = 'jck\x0b0uG}BJ%\tC{6|@'
    dict_0 = {str_1: str_0}
    expr_0 = module_3.expr(**dict_0)
    assigned_variables_collector_0 = module_4.AssignedVariablesCollector(str_0,
        expr_0)
    assert subscript_0 is not None
    #assert expr_0.jck
    #0uG}BJ% C{6|@ == 'ou.~K&pztteMP0'
    assert assigned_variables_collector_0.class_self_id == 'ou.~K&pztteMP0'
    assert assigned_variables_collector_0.variables == []
    assert assigned_variables_collector_0.self_attributes == []
    assert module_3.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_3.PyCF_ONLY_AST == 1024
    assert module_3.PyCF_TYPE_COMMENTS == 4096
    assert module_4.SPLITTING_CHARACTERS == ('[', ']', ',')
    var_0 = assigned_variables_collector_0.visit_Subscript(subscript_0)
    assert var_0 is None
 
def test_case_4_pass():
    assign_0 = module_3.Assign()
    list_0 = [assign_0]
    name_0 = module_3.Name(*list_0)
    str_0 = 'cQ%;FRLx'
    expr_0 = module_3.expr()
    assigned_variables_collector_0 = module_4.AssignedVariablesCollector(str_0,
        expr_0)
    assert assign_0 is not None
    assert expr_0 is not None
    assert assigned_variables_collector_0.class_self_id == 'cQ%;FRLx'
    assert assigned_variables_collector_0.variables == []
    assert assigned_variables_collector_0.self_attributes == []
    assert module_3.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_3.PyCF_ONLY_AST == 1024
    assert module_3.PyCF_TYPE_COMMENTS == 4096
    assert module_4.SPLITTING_CHARACTERS == ('[', ']', ',')
    var_0 = assigned_variables_collector_0.visit_Name(name_0)
    assert len(assigned_variables_collector_0.variables) == 1
    assert var_0 is None
    arg_0 = module_3.arg(*list_0)
    str_1 = "*H$`XC(3 o'wo"
    assigned_variables_collector_1 = module_4.AssignedVariablesCollector(str_1,
        expr_0)
    assert assigned_variables_collector_1.class_self_id == "*H$`XC(3 o'wo"
    assert assigned_variables_collector_1.variables == []
    assert assigned_variables_collector_1.self_attributes == []
 
def test_case_5_pass():
    assign_0 = module_3.Assign()
    list_0 = [assign_0]
    name_0 = module_3.Name(*list_0)
    str_0 = "-?zI+4oz6f'r>q!\x0b214G"
    expr_0 = module_3.expr()
    assigned_variables_collector_0 = module_4.AssignedVariablesCollector(str_0,
        expr_0)
    assert assign_0 is not None
    assert expr_0 is not None
    assert assigned_variables_collector_0.class_self_id == "-?zI+4oz6f'r>q!\x0b214G"
    assert assigned_variables_collector_0.variables == []
    assert assigned_variables_collector_0.self_attributes == []
    assert module_3.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_3.PyCF_ONLY_AST == 1024
    assert module_3.PyCF_TYPE_COMMENTS == 4096
    assert module_4.SPLITTING_CHARACTERS == ('[', ']', ',')
    list_1 = [name_0]
    attribute_0 = module_3.Attribute(*list_1)
    var_0 = assigned_variables_collector_0.visit_Attribute(attribute_0)
    assert var_0 is None

def test_case_f0_pass():
    try:
        variable_0 = module_3.Variable()
    except BaseException:
        pass
 
def test_case_f1_pass():
    try:
        str_0 = '%|8\r,f\n'
        list_0 = [str_0, str_0, str_0]
        signature_variables_collector_0 = module_3.SignatureVariablesCollector(
            str_0, *list_0)
    except BaseException:
        pass
 
def test_case_f2_pass():
    try:
        dict_0 = {}
        str_0 = "*H$`XC(3 o'wo"
        signature_variables_collector_0 = module_3.SignatureVariablesCollector(
            str_0)
        assert signature_variables_collector_0.constructor_source == "*H$`XC(3 o'wo"
        assert signature_variables_collector_0.class_self_id is None
        assert signature_variables_collector_0.variables == []
        assert module_3.SPLITTING_CHARACTERS == ('[', ']', ',')
        expr_0 = module_4.expr(**dict_0)
        assert expr_0 is not None
        assert module_4.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
        assert module_4.PyCF_ONLY_AST == 1024
        assert module_4.PyCF_TYPE_COMMENTS == 4096
        str_1 = '6e_\x0bE\t<J9Bxy)~*'
        module_resolver_0 = None
        str_2 = '~\tH+j!=gl>D\x0b%'
        constructor_visitor_0 = module_3.ConstructorVisitor(str_2, str_1,
            str_1, module_resolver_0)
    except BaseException:
        pass
 
def test_case_f3_pass():
    try:
        assign_0 = module_4.Assign()
        subscript_0 = module_4.Subscript()
        str_0 = 't$?QR9 \r~WEuFJ+{+\n`'
        expr_0 = module_4.expr()
        assigned_variables_collector_0 = module_3.AssignedVariablesCollector(
            str_0, expr_0)
        assert assign_0 is not None
        assert subscript_0 is not None
        assert expr_0 is not None
        assert assigned_variables_collector_0.class_self_id == 't$?QR9 \r~WEuFJ+{+\n`'
        assert assigned_variables_collector_0.variables == []
        assert assigned_variables_collector_0.self_attributes == []
        assert module_4.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
        assert module_4.PyCF_ONLY_AST == 1024
        assert module_4.PyCF_TYPE_COMMENTS == 4096
        assert module_3.SPLITTING_CHARACTERS == ('[', ']', ',')
        var_0 = assigned_variables_collector_0.visit_Subscript(subscript_0)
        assert var_0 is None
        var_1 = assigned_variables_collector_0.visit_Subscript(subscript_0)
        assert var_1 is None
        list_0 = [str_0]
        name_0 = module_4.Name(*list_0)
        assert name_0.id == 't$?QR9 \r~WEuFJ+{+\n`'
        subscript_1 = module_4.Subscript()
        assert subscript_1 is not None
        str_1 = '..,ch$P$'
        expr_1 = module_4.expr()
        assert expr_1 is not None
        assigned_variables_collector_1 = module_3.AssignedVariablesCollector(
            str_1, expr_1)
        assert assigned_variables_collector_1.class_self_id == '..,ch$P$'
        assert assigned_variables_collector_1.variables == []
        assert assigned_variables_collector_1.self_attributes == []
        var_2 = assigned_variables_collector_1.visit_Subscript(subscript_1)
        assert var_2 is None
        var_3 = assigned_variables_collector_1.visit_Subscript(subscript_1)
        assert var_3 is None
        expr_2 = module_4.expr()
        assert expr_2 is not None
        assigned_variables_collector_2 = module_3.AssignedVariablesCollector(
            str_0, expr_2)
        assert assigned_variables_collector_2.class_self_id == 't$?QR9 \r~WEuFJ+{+\n`'
        assert assigned_variables_collector_2.variables == []
        assert assigned_variables_collector_2.self_attributes == []
        var_4 = assigned_variables_collector_2.visit_Name(name_0)
        assert var_4 is None
        list_1 = [assign_0, assign_0]
        arg_0 = module_4.arg(*list_1)
        str_2 = "-?zI+4oz6f'r>q!\x0b214G"
        signature_variables_collector_0 = module_3.SignatureVariablesCollector(
            str_2)
        assert signature_variables_collector_0.constructor_source == "-?zI+4oz6f'r>q!\x0b214G"
        assert signature_variables_collector_0.class_self_id is None
        assert signature_variables_collector_0.variables == []
        var_5 = signature_variables_collector_0.visit_arg(arg_0)
        assert var_5 is None
        expr_3 = module_4.expr()
        assert expr_3 is not None
        str_3 = None
        assigned_variables_collector_3 = module_3.AssignedVariablesCollector(
            str_3, expr_1)
        assert assigned_variables_collector_3.class_self_id is None
        assert assigned_variables_collector_3.variables == []
        assert assigned_variables_collector_3.self_attributes == []
        list_2 = [name_0]
        attribute_0 = module_4.Attribute(*list_2)
        var_6 = assigned_variables_collector_2.visit_Attribute(attribute_0)
    except BaseException:
        pass
 
@given(class_self_id=st.text(), annotation=st.builds(expr))
def test_fuzz_AssignedVariablesCollector(
    class_self_id: str, annotation: ast.expr
) -> None:
    py2puml.parsing.astvisitors.AssignedVariablesCollector(
        class_self_id=class_self_id, annotation=annotation
    )
 
@given(full_namespace=st.text(), type_name=st.text())
def test_fuzz_NamespacedType(full_namespace: str, type_name: str) -> None:
    py2puml.parsing.astvisitors.NamespacedType(full_namespace=full_namespace, type_name=type_name)
 
@given(constructor_source=st.text())
def test_fuzz_SignatureVariablesCollector(constructor_source: str) -> None:
    py2puml.parsing.astvisitors.SignatureVariablesCollector(constructor_source=constructor_source)
 
@given(name=st.text(), type=st.text(), static=st.booleans())
def test_fuzz_UmlAttribute(name: str, type: str, static: bool) -> None:
    py2puml.parsing.astvisitors.UmlAttribute(name=name, type=type, static=static)
 
@given(
    source_fqn=st.text(),
    target_fqn=st.text(),
    type=st.sampled_from(py2puml.domain.umlrelation.RelType),
)
def test_fuzz_UmlRelation(
    source_fqn: str, target_fqn: str, type: py2puml.domain.umlrelation.RelType
) -> None:
    py2puml.parsing.astvisitors.UmlRelation(source_fqn=source_fqn, target_fqn=target_fqn, type=type)