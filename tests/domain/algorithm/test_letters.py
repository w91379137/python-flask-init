
# pytest -s tests/domain/algorithm/test_letters.py

import pytest
from asabulu.domain.algorithm.letters import column_id_to_int, int_to_column_id, ALPHABET

def test_int_to_column_id():

    # test_large_input
    assert int_to_column_id(256094574536617744129141650397448476) == ALPHABET
    
    # test_every_int
    for i in range(100000):
        assert column_id_to_int(int_to_column_id(i)) == i

    # test_lower_case_input
    assert column_id_to_int("abc") == column_id_to_int("ABC")

    # test_incorrect_input
    with pytest.raises(ValueError):
        column_id_to_int("T3ST")
    with pytest.raises(Exception):
        column_id_to_int(1234)

def test_column_id_to_int():
    
    # test_common_ints
    assert int_to_column_id(0) == ""
    assert int_to_column_id(1) == "A"
    assert int_to_column_id(26) == "Z"
    assert int_to_column_id(27) == "AA"
    assert int_to_column_id(702) == "ZZ"
    assert int_to_column_id(18252) == "ZYZ"

    # test_large_input
    assert column_id_to_int(ALPHABET) == 256094574536617744129141650397448476

    # test_incorrect_input
    with pytest.raises(ValueError):
        int_to_column_id(-1234)
    with pytest.raises(TypeError):
        int_to_column_id("Wrong")