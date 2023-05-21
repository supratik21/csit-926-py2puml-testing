from typing import Tuple
from pytest import raises, mark
from py2puml.parsing.compoundtypesplitter import CompoundTypeSplitter, remove_forward_references
import py2puml.parsing.compoundtypesplitter as module_0

@mark.parametrize('type_annotation', [
    'int',
    'str',
    '_ast.Name',
    'Tuple[str, withenum.TimeUnit]',
    'List[datetime.date]',
    'modules.withenum.TimeUnit',
    'Dict[str, Dict[str,builtins.float]]',
])
def test_CompoundTypeSplitter_from_valid_types(type_annotation: str):
    splitter = CompoundTypeSplitter(type_annotation, 'type.module')
    assert splitter.compound_type_annotation == type_annotation

@mark.parametrize('type_annotation', [
    None,
    '',
    '@dataclass',
    'Dict[str: withenum.TimeUnit]',
])
def test_CompoundTypeSplitter_from_invalid_types(type_annotation: str):
    with raises(ValueError) as ve:
        splitter = CompoundTypeSplitter(type_annotation, 'type.module')
    assert str(ve.value) == f'{type_annotation} seems to be an invalid type annotation'

@mark.parametrize('type_annotation,expected_parts', [
    ('int', ('int',)),
    ('str', ('str',)),
    ('_ast.Name', ('_ast.Name',)),
    ('Tuple[str, withenum.TimeUnit]', ('Tuple', '[', 'str', ',', 'withenum.TimeUnit', ']')),
    ('List[datetime.date]', ('List', '[', 'datetime.date', ']')),
    ('List[IPv6]', ('List', '[', 'IPv6', ']')),
    ('modules.withenum.TimeUnit', ('modules.withenum.TimeUnit',)),
    ('Dict[str, Dict[str,builtins.float]]', ('Dict', '[', 'str', ',', 'Dict', '[', 'str', ',', 'builtins.float', ']', ']')),
    ("typing.List[Package]", ('typing.List', '[', 'Package', ']')),
    ("typing.List[ForwardRef('Package')]", ('typing.List', '[', 'py2puml.domain.package.Package', ']')),
    ('typing.List[py2puml.domain.umlclass.UmlAttribute]', ('typing.List', '[', 'py2puml.domain.umlclass.UmlAttribute', ']'))
])
def test_CompoundTypeSplitter_get_parts(type_annotation: str, expected_parts: Tuple[str]):
    splitter = CompoundTypeSplitter(type_annotation, 'py2puml.domain.package')
    assert splitter.get_parts() == expected_parts

@mark.parametrize('type_annotation,type_module,without_forward_references', [
    (None, None, None),
    ("typing.List[ForwardRef('Package')]", 'py2puml.domain.package', 'typing.List[py2puml.domain.package.Package]'),
])
def test_remove_forward_references(type_annotation: str, type_module: str, without_forward_references: str):
    assert remove_forward_references(type_annotation, type_module) == without_forward_references

def test_case_0():
    try:
        str_0 = ';L1Ogwn0'
        str_1 = 's9YrE\x0b9+pH2W"m]'
        compound_type_splitter_0 = module_0.CompoundTypeSplitter(str_0, str_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '8'
        str_1 = ';'
        compound_type_splitter_0 = module_0.CompoundTypeSplitter(str_0, str_1)
        assert compound_type_splitter_0.compound_type_annotation == '8'
        assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
        tuple_0 = compound_type_splitter_0.get_parts()
        assert tuple_0 == ('8',)
        str_2 = None
        compound_type_splitter_1 = module_0.CompoundTypeSplitter(str_2, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'gKG\tJ<O*'
        str_1 = '[kdzOU'
        compound_type_splitter_0 = module_0.CompoundTypeSplitter(str_1, str_0)
        assert compound_type_splitter_0.compound_type_annotation == '[kdzOU'
        assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
        tuple_0 = compound_type_splitter_0.get_parts()
        assert tuple_0 == ('[', 'kdzOU')
        str_2 = '~B8}:|wsXBohAC ny'
        str_3 = 'O'
        compound_type_splitter_1 = module_0.CompoundTypeSplitter(str_2, str_3)
    except BaseException:
        pass

def test_case_3():
    str_0 = None
    str_1 = None
    str_2 = module_0.remove_forward_references(str_0, str_1)
    assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')

def test_case_4():
    str_0 = 'ODFo;D'
    str_1 = '.'
    str_2 = module_0.remove_forward_references(str_0, str_1)
    assert str_2 == 'ODFo;D'
    assert module_0.SPLITTING_CHARACTERS == ('[', ']', ',')
    str_3 = 'di|aQ\rba'
    compound_type_splitter_0 = module_0.CompoundTypeSplitter(str_3, str_1)
    assert compound_type_splitter_0.compound_type_annotation == 'di|aQ\rba'
    tuple_0 = compound_type_splitter_0.get_parts()
    assert tuple_0 == ('di|aQ\rba',)
    tuple_1 = compound_type_splitter_0.get_parts()
    assert tuple_1 == ('di|aQ\rba',)