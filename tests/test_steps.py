# content of test_step.py
import pytest

@pytest.mark.incremental
class TestUserHandling:
    def test_login(self):
        x = "abc"
        assert 'a' in x
        pass
    def test_modification(self):
        assert 1
    def test_deletion(self):
        pass
def test_normal():
    assert 1
