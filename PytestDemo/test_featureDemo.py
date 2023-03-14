import pytest

'''
@pytest.mark.usefixtures()
class TestDemo:
    def test_demo1(self, loadData):
        print(loadData[0])
        print(loadData[2])
'''


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
