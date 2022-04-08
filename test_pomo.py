import pomodoro

def test_get_data_from_remote():
    try:
        pomodoro.get_data()
        assert True
    except:
        assert False

def test_test():
    assert True
