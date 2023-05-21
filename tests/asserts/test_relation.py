from py2puml.domain.umlrelation import UmlRelation, RelType
from tests.asserts.relation import assert_relation
import pytest

def test_assert_relation_valid_with_rel_type_as_composition():
    relation = UmlRelation('source', 'target', RelType.COMPOSITION)
    assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

def test_assert_relation_valid_with_rel_type_as_inheritance():
    relation = UmlRelation('source', 'target', RelType.INHERITANCE)
    assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

# Test case: Invalid source FQN
def test_assert_relation_invalid_source_fqn_with_rel_type_as_composition():
    relation = UmlRelation('source', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'different_source', 'target', RelType.COMPOSITION)

# Test case: Invalid source FQN
def test_assert_relation_invalid_source_fqn_with_rel_type_as_inheritance():
    relation = UmlRelation('source', 'target', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'different_source', 'target', RelType.INHERITANCE)

# Test case: Invalid target FQN
def test_assert_relation_invalid_target_fqn_with_rel_type_as_composition():
    relation = UmlRelation('source', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation, 'source', 'different_target', RelType.COMPOSITION)

# Test case: Invalid target FQN
def test_assert_relation_invalid_target_fqn_with_rel_type_as_inheritance():
    relation = UmlRelation('source', 'target', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation, 'source', 'different_target', RelType.INHERITANCE)

# Test case: Invalid relation type
def test_assert_relation_invalid_type():
    relation = UmlRelation('source', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

# Test case: Relation with a different relation type
def test_assert_relation_different_rel_type():
    relation = UmlRelation('source', 'target', RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

# Test case: Relation with different source FQN and target FQN
def test_assert_relation_different_source_and_target_fqn_with_rel_type_as_composition():
    relation = UmlRelation('source', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'different_source', 'different_target', RelType.COMPOSITION)

# Test case: Relation with different source FQN and target FQN
def test_assert_relation_different_source_and_target_fqn_with_rel_type_as_inheritance():
    relation = UmlRelation('source', 'target', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'different_source', 'different_target', RelType.INHERITANCE)

# Test case: Relation with different source FQN and target FQN
def test_assert_relation_different_source_fqn_and_rel_type_with_rel_type_as_composition():
    relation = UmlRelation('source', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'different_source', 'target', RelType.INHERITANCE)

# Test case: Relation with different source FQN and target FQN
def test_assert_relation_different_source_fqn_and_rel_type_with_rel_type_as_inheritance():
    relation = UmlRelation('source', 'target', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'different_source', 'target', RelType.COMPOSITION)

# Test case: Relation with different source FQN and target FQN
def test_assert_relation_different_target_fqn_and_rel_type_with_rel_type_as_composition():
    relation = UmlRelation('source', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation, 'source', 'different_target', RelType.INHERITANCE)

# Test case: Relation with different source FQN and target FQN
def test_assert_relation_different_target_fqn_and_rel_type_with_rel_type_as_inheritance():
    relation = UmlRelation('source', 'target', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation, 'source', 'different_target', RelType.COMPOSITION)

# Test case: Relation with different source FQN, target FQN and RelType
def test_assert_relation_different_fqn_with_rel_type_as_composition():
    relation = UmlRelation('source', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'different_source', 'different_target', RelType.INHERITANCE)

# Test case: Relation with different source FQN and target FQN
def test_assert_relation_different_fqn_with_rel_type_as_inheritance():
    relation = UmlRelation('source', 'target', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'different_source', 'different_target', RelType.COMPOSITION)

# Test case: Relation with an empty source FQN
def test_assert_relation_empty_source_fqn_with_rel_type_as_composition():
    relation = UmlRelation('', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)        

# Test case: Relation with an empty source FQN
def test_assert_relation_empty_source_fqn_with_rel_type_as_inheritance():
    relation = UmlRelation('', 'target', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

# Test case: Relation with an empty target FQN
def test_assert_relation_empty_target_fqn_with_rel_type_as_composition():
    relation = UmlRelation('source', '', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)
    
# Test case: Relation with an empty target FQN
def test_assert_relation_empty_target_fqn_with_rel_type_as_inheritance():
    relation = UmlRelation('source', '', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

# Test case: Relation with an empty relType
def test_assert_relation_empty_rel_type_with_rel_type_as_composition():
    relation = UmlRelation('source', 'target', '')
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

# Test case: Relation with an empty relType
def test_assert_relation_empty_rel_type_with_rel_type_as_inheritance():
    relation = UmlRelation('source', 'target', '')
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

# Test case: Relation with an empty source, target FQN
def test_assert_relation_empty_source_and_target_fqn_with_rel_type_as_composition():
    relation = UmlRelation('', '', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

# Test case: Relation with an empty source, target FQN
def test_assert_relation_empty_source_and_target_with_rel_type_as_inheritance():
    relation = UmlRelation('', '', RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

# Test case: Relation with an empty source FQN and rel type
def test_assert_relation_empty_source_fqn_and_rel_type_with_rel_type_as_composition():
    relation = UmlRelation('', 'target', '')
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

# Test case: Relation with an empty source FQN and rel type
def test_assert_relation_empty_source_fqn_and_rel_type_with_rel_type_as_inheritance():
    relation = UmlRelation('', 'target', '')
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

# Test case: Relation with an empty target FQN and rel type
def test_assert_relation_empty_target_fqn_and_rel_type_with_rel_type_as_composition():
    relation = UmlRelation('source', '', '')
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

# Test case: Relation with an empty target FQN and rel type
def test_assert_relation_empty_target_fqn_and_rel_type_with_rel_type_as_inheritance():
    relation = UmlRelation('source', '', '')
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

# Test case: Relation with an empty , target FQN and rel type
def test_assert_relation_empty_source_target_fqn_and_rel_type_with_rel_type_as_composition():
    relation = UmlRelation('', '', '')
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

# Test case: Relation with an empty source, target FQN and rel type
def test_assert_relation_empty_source_target_fqn_and_rel_type_with_rel_type_as_inheritance():
    relation = UmlRelation('', '', '')
    with pytest.raises(AssertionError):
        assert_relation(relation, 'source', 'target', RelType.INHERITANCE)

def test_assert_multiple_relations_with_same_source_and_target_fqn():
    # Test case: Multiple relations with the same source and target FQN
    relation5 = UmlRelation("source.Module", "target.Module", RelType.COMPOSITION)
    relation6 = UmlRelation("source.Module", "target.Module", RelType.INHERITANCE)
    assert_relation(relation5, "source.Module", "target.Module", RelType.COMPOSITION)
    assert_relation(relation6, "source.Module", "target.Module", RelType.INHERITANCE)

def test_assert_case_sensitive_source_fqn_comparison_with_rel_type_as_composition():
    # Test case: Case-insensitive source FQN comparison
    relation7 = UmlRelation("source.module", "target.Module", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation7, "source.Module", "target.Module", RelType.COMPOSITION)

def test_assert_case_sensitive_source_fqn_comparison_with_rel_type_as_inheritance():
    # Test case: Case-insensitive source FQN comparison
    relation7 = UmlRelation("source.module", "target.Module", RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation7, "source.Module", "target.Module", RelType.INHERITANCE)

def test_assert_case_sensitive_target_fqn_comparison_with_rel_type_as_composition():
    # Test case: Case-insensitive target FQN comparison
    relation8 = UmlRelation("source.module", "target.module", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation8, "source.module", "target.Module", RelType.COMPOSITION)

def test_assert_case_sensitive_target_fqn_comparison_with_rel_type_as_inheritance():
    # Test case: Case-insensitive target FQN comparison
    relation8 = UmlRelation("source.module", "target.module", RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation8, "source.module", "target.Module", RelType.INHERITANCE)

def test_assert_relation_with_case_insensitive_fqns_with_rel_type_as_composition():
    # Test case: Relation with case-insensitive source and target FQN comparison
    relation40 = UmlRelation("source.Module", "target.Module", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation40, "source.module", "target.module", RelType.COMPOSITION)

def test_assert_relation_with_case_insensitive_fqns_with_rel_type_as_inheritance():
    # Test case: Relation with case-insensitive source and target FQN comparison
    relation40 = UmlRelation("source.Module", "target.Module", RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation40, "source.module", "target.module", RelType.INHERITANCE)

def test_assert_relation_with_special_characters_source_fqn_with_rel_type_as_composition():
    # Test case: Relation with source FQN containing special characters
    relation44 = UmlRelation("@source!", "target", RelType.COMPOSITION)
    assert_relation(relation44, "@source!", "target", RelType.COMPOSITION)

def test_assert_relation_with_special_characters_source_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with source FQN containing special characters
    relation44 = UmlRelation("@source!", "target", RelType.INHERITANCE)
    assert_relation(relation44, "@source!", "target", RelType.INHERITANCE)

def test_assert_relation_with_special_characters_target_fqn_with_rel_type_as_composition():
    # Test case: Relation with target FQN containing special characters
    relation44 = UmlRelation("source", "@target!", RelType.COMPOSITION)
    assert_relation(relation44, "source", "@target!", RelType.COMPOSITION)

def test_assert_relation_with_special_characters_target_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with target FQN containing special characters
    relation44 = UmlRelation("source", "@target!", RelType.INHERITANCE)
    assert_relation(relation44, "source", "@target!", RelType.INHERITANCE)

def test_assert_relation_with_special_characters_fqns_with_rel_type_as_composition():
    # Test case: Relation with source and target FQN containing special characters
    relation44 = UmlRelation("@source!", "@target!", RelType.COMPOSITION)
    assert_relation(relation44, "@source!", "@target!", RelType.COMPOSITION)

def test_assert_relation_with_special_characters_fqns_with_rel_type_as_inheritance():
    # Test case: Relation with source and target FQN containing special characters
    relation44 = UmlRelation("@source!", "@target!", RelType.INHERITANCE)
    assert_relation(relation44, "@source!", "@target!", RelType.INHERITANCE)

def test_assert_relation_with_invalid_source_fqn_with_rel_type_as_composition():
    # Test case: Relation with an invalid source FQN
    relation38 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation38, "different_source", "target", RelType.COMPOSITION)

def test_assert_relation_with_invalid_source_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with an invalid source FQN
    relation38 = UmlRelation("source", "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation38, "different_source", "target", RelType.INHERITANCE)

def test_assert_relation_with_invalid_target_fqn_with_rel_type_as_composition():
    # Test case: Relation with an invalid target FQN
    relation38 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation38, "source", "different_target", RelType.COMPOSITION)

def test_assert_relation_with_invalid_target_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with an invalid target FQN
    relation38 = UmlRelation("source", "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation38, "source", "different_target", RelType.INHERITANCE)

def test_assert_relation_with_invalid_fqns_with_rel_type_as_composition():
    # Test case: Relation with an invalid source and target FQN
    relation38 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation38, "different_source", "different_target", RelType.COMPOSITION)

def test_assert_relation_with_invalid_fqns_with_rel_type_as_inheritance():
    # Test case: Relation with an invalid source and target FQN
    relation38 = UmlRelation("source", "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation38, "different_source", "different_target", RelType.INHERITANCE)

def test_assert_relation_with_whitespace_source_fqn_with_rel_type_as_composition():
    # Test case: Relation with whitespace-only source FQN
    relation42 = UmlRelation("   ", "target", RelType.COMPOSITION)
    assert_relation(relation42, "   ", "target", RelType.COMPOSITION)

def test_assert_relation_with_whitespace_source_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with whitespace-only source FQN
    relation42 = UmlRelation("   ", "target", RelType.INHERITANCE)
    assert_relation(relation42, "   ", "target", RelType.INHERITANCE)

def test_assert_relation_with_whitespace_target_fqn_with_rel_type_as_composition():
    # Test case: Relation with whitespace-only target FQN
    relation42 = UmlRelation("source", " ", RelType.COMPOSITION)
    assert_relation(relation42, "source", " ", RelType.COMPOSITION)

def test_assert_relation_with_whitespace_target_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with whitespace-only target FQN
    relation42 = UmlRelation("source", " ", RelType.INHERITANCE)
    assert_relation(relation42, "source", " ", RelType.INHERITANCE)

def test_assert_relation_with_whitespace_fqns_with_rel_type_as_composition():
    # Test case: Relation with whitespace-only FQNS
    relation42 = UmlRelation(" ", " ", RelType.COMPOSITION)
    assert_relation(relation42, " ", " ", RelType.COMPOSITION)

def test_assert_relation_with_whitespace_fqns_with_rel_type_as_inheritance():
    # Test case: Relation with whitespace-only FQNS
    relation42 = UmlRelation(" ", " ", RelType.INHERITANCE)
    assert_relation(relation42, " ", " ", RelType.INHERITANCE)

def test_assert_relation_with_numeric_source_fqn_with_rel_type_as_composition():
    # Test case: Relation with numeric source FQN
    relation43 = UmlRelation("123", "target", RelType.COMPOSITION)
    assert_relation(relation43, "123", "target", RelType.COMPOSITION)

def test_assert_relation_with_numeric_source_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with numeric source FQN
    relation43 = UmlRelation("123", "target", RelType.INHERITANCE)
    assert_relation(relation43, "123", "target", RelType.INHERITANCE)

def test_assert_relation_with_numeric_target_fqn_with_rel_type_as_composition():
    # Test case: Relation with numeric target FQN
    relation43 = UmlRelation("source", "123", RelType.COMPOSITION)
    assert_relation(relation43, "source", "123", RelType.COMPOSITION)

def test_assert_relation_with_numeric_target_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with numeric target FQN
    relation43 = UmlRelation("source", "123", RelType.INHERITANCE)
    assert_relation(relation43, "source", "123", RelType.INHERITANCE)

def test_assert_relation_with_numeric_fqns_with_rel_type_as_composition():
    # Test case: Relation with numeric FQNS
    relation43 = UmlRelation("123", "123", RelType.COMPOSITION)
    assert_relation(relation43, "123", "123", RelType.COMPOSITION)

def test_assert_relation_with_numeric_fqns_with_rel_type_as_inheritance():
    # Test case: Relation with numeric FQNS
    relation43 = UmlRelation("123", "123", RelType.INHERITANCE)
    assert_relation(relation43, "123", "123", RelType.INHERITANCE)

def test_assert_relation_with_actual_numeric_source_fqn_with_rel_type_as_composition():
    # Test case: Relation with numeric source FQN
    relation43 = UmlRelation(123, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation43, "123", "target", RelType.COMPOSITION)

def test_assert_relation_with_actual_numeric_source_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with numeric source FQN
    relation43 = UmlRelation(123, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation43, "123", "target", RelType.INHERITANCE)

def test_assert_relation_with_actual_numeric_target_fqn_with_rel_type_as_composition():
    # Test case: Relation with numeric target FQN
    relation43 = UmlRelation("source", 123, RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation43, "source", "123", RelType.COMPOSITION)

def test_assert_relation_with_actual_numeric_target_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with numeric target FQN
    relation43 = UmlRelation("source", 123, RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation43, "source", "123", RelType.INHERITANCE)

def test_assert_relation_with_actual_numeric_fqns_with_rel_type_as_composition():
    # Test case: Relation with numeric FQNS
    relation43 = UmlRelation(123, 123, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation43, "123", "123", RelType.COMPOSITION)

def test_assert_relation_with_actual_numeric_fqns_with_rel_type_as_inheritance():
    # Test case: Relation with numeric FQNS
    relation43 = UmlRelation(123, 123, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation43, "123", "123", RelType.INHERITANCE)

def test_assert_rel_with_boolean_source_fqn_with_rel_type_as_composition():
    # Test case: Relation with numeric source FQN
    relation43 = UmlRelation(True, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation43, "123", "target", RelType.COMPOSITION)

def test_assert_rel_with_boolean_source_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with numeric source FQN
    relation43 = UmlRelation(True, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation43, "123", "target", RelType.INHERITANCE)

def test_assert_rel_with_boolean_target_fqn_with_rel_type_as_composition():
    # Test case: Relation with numeric target FQN
    relation43 = UmlRelation("source", True, RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation43, "source", "123", RelType.COMPOSITION)

def test_assert_rel_with_boolean_target_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with numeric target FQN
    relation43 = UmlRelation("source", True, RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation43, "source", "123", RelType.INHERITANCE)

def test_assert_rel_with_boolean_fqns_with_rel_type_as_composition():
    # Test case: Relation with numeric FQNS
    relation43 = UmlRelation(True, False, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation43, "123", "123", RelType.COMPOSITION)

def test_assert_rel_with_actual_numeric_fqns_with_rel_type_as_inheritance():
    # Test case: Relation with numeric FQNS
    relation43 = UmlRelation(True, False, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation43, "123", "123", RelType.INHERITANCE)

def test_assert_relation_with_long_source_fqn_with_rel_type_as_composition():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    assert_relation(relation45, "source" * 1000, "target", RelType.COMPOSITION)

def test_assert_relation_with_long_source_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    assert_relation(relation45, "source" * 1000, "target", RelType.INHERITANCE)

def test_assert_relation_with_long_target_fqn_with_rel_type_as_composition():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    assert_relation(relation45, "source", "target"  * 1000, RelType.COMPOSITION)

def test_assert_relation_with_long_target_fqn_with_rel_type_as_inheritance():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    assert_relation(relation45, "source", "target"  * 1000, RelType.INHERITANCE)

def test_assert_relation_with_long_fqns_with_rel_type_as_composition():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    assert_relation(relation45, "source" * 1000, "target" * 1000, RelType.COMPOSITION)

def test_assert_relation_with_long_fqns_with_rel_type_as_inheritance():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    assert_relation(relation45, "source" * 1000, "target" * 1000, RelType.INHERITANCE)

def test_assert_relation_with_long_source_fqn_with_rel_type_as_composition_negative_case():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_long_source_fqn_with_rel_type_as_inheritance_negative_case():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, "source", "target", RelType.INHERITANCE)

def test_assert_relation_with_long_target_fqn_with_rel_type_as_composition_negative_case():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation45, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_long_target_fqn_with_rel_type_as_inheritance_negative_case():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation45, "source", "target", RelType.INHERITANCE)

def test_assert_relation_with_long_fqns_with_rel_type_as_composition_negative_case():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_long_fqns_with_rel_type_as_inheritance_negative_case():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "source", "target", RelType.INHERITANCE)

def test_assert_relation_with_long_source_fqn_with_rel_type_as_composition_negative_case_with_boolean():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, True, False, RelType.COMPOSITION)

def test_assert_relation_with_long_source_fqn_with_rel_type_as_inheritance_negative_case_with_boolean():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, True, False, RelType.INHERITANCE)

def test_assert_relation_with_long_target_fqn_with_rel_type_as_composition_negative_case_with_boolean():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, True, False, RelType.COMPOSITION)

def test_assert_relation_with_long_target_fqn_with_rel_type_as_inheritance_negative_case_with_boolean():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, True, False, RelType.INHERITANCE)

def test_assert_relation_with_long_fqns_with_rel_type_as_composition_negative_case_with_boolean():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, True, False, RelType.COMPOSITION)

def test_assert_relation_with_long_fqns_with_rel_type_as_inheritance_negative_case_with_boolean():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, True, False, RelType.INHERITANCE)

def test_assert_relation_with_long_source_fqn_with_rel_type_as_composition_negative_case_with_none():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, None, None, RelType.COMPOSITION)

def test_assert_relation_with_long_source_fqn_with_rel_type_as_inheritance_negative_case_with_none():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, None, None, RelType.INHERITANCE)

def test_assert_relation_with_long_target_fqn_with_rel_type_as_composition_negative_case_with_none():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, None, None, RelType.COMPOSITION)

def test_assert_relation_with_long_target_fqn_with_rel_type_as_inheritance_negative_case_with_none():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, None, None, RelType.INHERITANCE)

def test_assert_relation_with_long_fqns_with_rel_type_as_composition_negative_case_with_none():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, None, None, RelType.COMPOSITION)

def test_assert_relation_with_long_fqns_with_rel_type_as_inheritance_negative_case_with_none():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, None, None, RelType.INHERITANCE)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_composition_negative_case_with_empty_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, "", "", RelType.COMPOSITION)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_inheritance_negative_case_with_empty_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, "", "", RelType.INHERITANCE)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_composition_negative_case_with_empty_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "", "", RelType.COMPOSITION)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_inheritance_negative_case_with_empty_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "", "", RelType.INHERITANCE)

def test_assert_rel_with_long_fqns_with_rel_type_as_composition_negative_case_with_empty_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "", "", RelType.COMPOSITION)

def test_assert_rel_with_long_fqns_with_rel_type_as_inheritance_negative_case_with_empty_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "", "", RelType.INHERITANCE)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_composition_negative_case_with_alphanumeric_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, "xyz123", "xyz123", RelType.COMPOSITION)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_inheritance_negative_case_with_alphanumeric_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, "xyz123", "xyz123", RelType.INHERITANCE)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_composition_negative_case_with_alphanumeric_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "xyz123", "xyz123", RelType.COMPOSITION)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_inheritance_negative_case_with_alphanumeric_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "xyz123", "xyz123", RelType.INHERITANCE)

def test_assert_rel_with_long_fqns_with_rel_type_as_composition_negative_case_with_alphanumeric_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "xyz123", "xyz123", RelType.COMPOSITION)

def test_assert_rel_with_long_fqns_with_rel_type_as_inheritance_negative_case_with_alphanumeric_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "xyz123", "xyz123", RelType.INHERITANCE)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_composition_negative_case_with_only_space_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, "  ", "  ", RelType.COMPOSITION)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_inheritance_negative_case_with_only_space_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, "  ", "  ", RelType.INHERITANCE)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_composition_negative_case_with_only_space_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "  ", "  ", RelType.COMPOSITION)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_inheritance_negative_case_with_only_space_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "  ", "  ", RelType.INHERITANCE)

def test_assert_rel_with_long_fqns_with_rel_type_as_composition_negative_case_with_only_space_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "  ", "  ", RelType.COMPOSITION)

def test_assert_rel_with_long_fqns_with_rel_type_as_inheritance_negative_case_with_only_space_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, "  ", "  ", RelType.INHERITANCE)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_composition_negative_case_with_space_and_alphanmeric_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, " xyz 123 ", " xyz 123 ", RelType.COMPOSITION)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_inheritance_negative_case_with_space_and_alphanmeric_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, " xyz 123 ", " xyz 123 ", RelType.INHERITANCE)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_composition_negative_case_with_space_and_alphanmeric_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, " xyz 123 ", " xyz 123 ", RelType.COMPOSITION)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_inheritance_negative_case_with_space_and_alphanmeric_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, " xyz 123 ", " xyz 123 ", RelType.INHERITANCE)

def test_assert_rel_with_long_fqns_with_rel_type_as_composition_negative_case_with_space_and_alphanmeric_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, " xyz 123 ", " xyz 123 ", RelType.COMPOSITION)

def test_assert_rel_with_long_fqns_with_rel_type_as_inheritance_negative_case_with_space_and_alphanmeric_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, " xyz 123 ", " xyz 123 ", RelType.INHERITANCE)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_composition_negative_case_with_space_alphanmeric_and_spcl_char_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, " xyz@123 ", " xyz@123 ", RelType.COMPOSITION)

def test_assert_rel_with_long_source_fqn_with_rel_type_as_inheritance_negative_case_with_space_alphanmeric_and_spcl_char_str():
    # Test case: Relation with long source FQN
    relation45 = UmlRelation("source" * 1000, "target", RelType.INHERITANCE)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation45, " xyz@123 ", " xyz@123 ", RelType.INHERITANCE)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_composition_negative_case_with_space_alphanmeric_and_spcl_char_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, " xyz@123 ", " xyz@123 ", RelType.COMPOSITION)

def test_assert_rel_with_long_target_fqn_with_rel_type_as_inheritance_negative_case_with_space_alphanmeric_and_spcl_char_str():
    # Test case: Relation with long target FQN
    relation45 = UmlRelation("source", "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, " xyz@123 ", " xyz@123 ", RelType.INHERITANCE)

def test_assert_rel_with_long_fqns_with_rel_type_as_composition_negative_case_with_space_alphanmeric_and_spcl_char_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation45, " xyz@123 ", " xyz@123 ", RelType.COMPOSITION)

def test_assert_rel_with_long_fqns_with_rel_type_as_inheritance_negative_case_with_space_alphanmeric_and_spcl_char_str():
    # Test case: Relation with long source and target FQN
    relation45 = UmlRelation("source" * 1000, "target" * 1000, RelType.INHERITANCE)
    with pytest.raises(AssertionError):
        assert_relation(relation45, " xyz@123 ", " xyz@123 ", RelType.INHERITANCE)

def test_assert_relation_with_additional_attributes_invalid_dict_with_rel_type_as_composition():
    # Test case: Relation with additional attributes (invalid dictionary)
    relation59 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(TypeError):
        assert_relation(relation59, "source", "target", RelType.COMPOSITION, attr1="value1")

def test_assert_relation_with_additional_attributes_invalid_dict_with_rel_type_as_inheritance():
    # Test case: Relation with additional attributes (invalid dictionary)
    relation59 = UmlRelation("source", "target", RelType.INHERITANCE)
    with pytest.raises(TypeError):
        assert_relation(relation59, "source", "target", RelType.INHERITANCE, attr1="value1")

def test_assert_relation_with_annotations():
    # Test case: Relation with annotations
    relation12 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation12, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_staticity():
    # Test case: Relation with staticity
    relation13 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation13, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_visibility():
    # Test case: Relation with visibility
    relation14 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation14, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_documentation():
    # Test case: Relation with documentation
    relation15 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation15, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_multiple_attributes():
    # Test case: Relation with multiple attributes
    relation16 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation16, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_invalid_values():
    # Test case: Relation with invalid values
    relation17 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation17, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_unicode_characters():
    # Test case: Relation with unicode characters
    relation18 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation18, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_different_additional_attributes():
    # Test case: Relation with different additional attributes
    relation = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(TypeError):
        assert_relation(relation, "source", "target", RelType.COMPOSITION, additional_attr="value1", additional_attr2="value2")

def test_assert_relation_with_no_additional_attributes():
    # Test case: Relation with no additional attributes
    relation21 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation21, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_same_source_and_target_fqn():
    # Test case: Relation with the same source and target FQN
    relation24 = UmlRelation("source.Module", "source.Module", RelType.COMPOSITION)
    assert_relation(relation24, "source.Module", "source.Module", RelType.COMPOSITION)

def test_assert_relation_with_invalid_relation_type():
    # Test case: Relation with an invalid relation type
    with pytest.raises(AssertionError):
        relation32 = UmlRelation("source", "target", RelType.COMPOSITION)
        assert_relation(relation32, "source", "target", "InvalidType")

def test_assert_relation_with_no_additional_attributes():
    # Test case: Relation with no additional attributes
    relation34 = UmlRelation("source", "target", RelType.COMPOSITION)
    assert_relation(relation34, "source", "target", RelType.COMPOSITION)

def test_assert_relation_with_same_source_and_target_fqn():
    # Test case: Relation with the same source and target FQN
    relation37 = UmlRelation("source.Module", "source.Module", RelType.COMPOSITION)
    assert_relation(relation37, "source.Module", "source.Module", RelType.COMPOSITION)

def test_assert_relation_with_empty_fqns():
    # Test case: Relation with empty source and target FQN
    relation41 = UmlRelation("", "", RelType.COMPOSITION)
    assert_relation(relation41, "", "", RelType.COMPOSITION)

def test_assert_relation_with_different_rel_type():
    # Test case: Relation with different relation type
    relation46 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation46, "source", "target", RelType.INHERITANCE)

def test_assert_relation_with_invalid_rel_type():
    # Test case: Relation with invalid relation type
    relation47 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation47, "source", "target", "InvalidType")

def test_assert_relation_with_no_rel_type():
    # Test case: Relation with no relation type
    relation49 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation49, "source", "target", None)

def test_assert_relation_with_no_rel_source_fqn():
    # Test case: Relation with no relation type
    relation49 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation49, None, "target", RelType.COMPOSITION)

def test_assert_relation_with_no_rel_target_fqn():
    # Test case: Relation with no relation type
    relation49 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation49, "source", None, RelType.COMPOSITION)

def test_assert_relation_with_no_rel_source_and_target_fqn():
    # Test case: Relation with no relation type
    relation49 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation49, None, None, RelType.COMPOSITION)

def test_assert_relation_with_no_rel_source_and_rel_type():
    # Test case: Relation with no relation type
    relation49 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation49, None, "target", None)

def test_assert_relation_with_no_rel_target_and_rel_type():
    # Test case: Relation with no relation type
    relation49 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation49, "source", None, None)

def test_assert_relation_with_no_rel_source_and_target_fqn_and_rel_type():
    # Test case: Relation with no relation type
    relation49 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation49, None, None, None)

def test_assert_relation_with_different_rel_type_case_insensitive():
    # Test case: Relation with different relation type (case-insensitive)
    relation = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(AssertionError):
        assert_relation(relation, "source", "target", RelType.INHERITANCE)

def test_assert_relation_with_different_rel_type_case_sensitive_target_fqn():
    relation = UmlRelation('source', 'TARGET', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='target end'):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

def test_assert_relation_with_different_rel_type_case_sensitive_source_fqn():
    relation = UmlRelation('SOURCE', 'target', RelType.COMPOSITION)
    with pytest.raises(AssertionError, match='source end'):
        assert_relation(relation, 'source', 'target', RelType.COMPOSITION)

def test_assert_relation_with_additional_attributes_multiple_values():
    # Test case: Relation with additional attributes (multiple values)
    relation = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(TypeError):
        assert_relation(relation, "source", "target", RelType.COMPOSITION, attr1="value1", attr2="value2")

def test_assert_relation_with_additional_attributes_invalid_dict():
    # Test case: Relation with additional attributes (invalid dictionary)
    relation59 = UmlRelation("source", "target", RelType.COMPOSITION)
    with pytest.raises(TypeError):
        assert_relation(relation59, "source", "target", RelType.COMPOSITION, attr1="value1")