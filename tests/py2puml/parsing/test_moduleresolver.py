from py2puml.parsing.moduleresolver import ModuleResolver, NamespacedType
from tests.py2puml.parsing.mockedinstance import MockedInstance
import py2puml.parsing.moduleresolver as module_0
import builtins as module_1

def assert_NamespacedType(namespaced_type: NamespacedType, full_namespace_type: str, short_type: str):
    assert namespaced_type.full_namespace == full_namespace_type
    assert namespaced_type.type_name == short_type

def test_ModuleResolver_resolve_full_namespace_type():
    source_module = MockedInstance({
        '__name__': 'tests.modules.withconstructor',
        'modules': {
            'withenum': {
                'TimeUnit': {
                    '__module__': 'tests.modules.withenum',
                    '__name__': 'TimeUnit'
                }
            }
        },
        'withenum': {
            'TimeUnit': {
                '__module__': 'tests.modules.withenum',
                '__name__': 'TimeUnit'
            }
        },
        'Coordinates': {
            '__module__': 'tests.modules.withconstructor',
            '__name__': 'Coordinates'
        }
    })
    module_resolver = ModuleResolver(source_module)
    assert_NamespacedType(module_resolver.resolve_full_namespace_type(
        'modules.withenum.TimeUnit'
    ), 'tests.modules.withenum.TimeUnit', 'TimeUnit')
    assert_NamespacedType(module_resolver.resolve_full_namespace_type(
        'withenum.TimeUnit'
    ), 'tests.modules.withenum.TimeUnit', 'TimeUnit')
    assert_NamespacedType(module_resolver.resolve_full_namespace_type(
        'Coordinates'
    ), 'tests.modules.withconstructor.Coordinates', 'Coordinates')

def test_ModuleResolver_get_module_full_name():
    source_module = MockedInstance({
        '__name__': 'tests.modules.withconstructor'
    })
    module_resolver = ModuleResolver(source_module)
    assert module_resolver.get_module_full_name() == 'tests.modules.withconstructor'

def test_case_0():
    try:
        namespaced_type_0 = module_0.NamespacedType()
    except BaseException:
        pass

def test_case_1():
    try:
        module_0 = None
        module_resolver_0 = module_0.ModuleResolver(module_0)
        assert module_resolver_0.module is None
        str_0 = None
        var_0 = module_0.search_in_module_or_builtins(module_0, str_0)
        assert var_0 is None
        assert module_0.EMPTY_NAMESPACED_TYPE == (None, None)
        str_1 = module_resolver_0.__repr__()
        assert str_1 == 'ModuleResolver(None)'
        module_resolver_1 = module_0.ModuleResolver(module_0)
        assert module_resolver_1.module is None
        str_2 = module_resolver_0.get_module_full_name()
    except BaseException:
        pass

def test_case_2():
    try:
        module_0 = None
        module_resolver_0 = module_0.ModuleResolver(module_0)
        assert module_resolver_0.module is None
        str_0 = module_resolver_0.__repr__()
        assert str_0 == 'ModuleResolver(None)'
        module_1 = module_1.module()
    except BaseException:
        pass

def test_case_3():
    try:
        module_0 = None
        module_resolver_0 = module_0.ModuleResolver(module_0)
        assert module_resolver_0.module is None
        str_0 = None
        namespaced_type_0 = module_resolver_0.resolve_full_namespace_type(str_0
            )
        assert namespaced_type_0 == (None, None)
        assert module_0.EMPTY_NAMESPACED_TYPE == (None, None)
        str_1 = '|L#p[lr;\roPC'
        namespaced_type_1 = module_resolver_0.resolve_full_namespace_type(str_1
            )
    except BaseException:
        pass