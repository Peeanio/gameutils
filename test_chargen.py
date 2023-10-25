import chargen

def test_rollDx():
    test_num = 3
    result = chargen.rollDx(test_num)
    if result >= 1 and result <= test_num:
        assert True
    else:
        assert False

def test_rollToX():
    test_num = 4
    result = chargen.rollToX(test_num)
    if result >= 0 and result <= test_num:
        assert True
    else:
        assert False
