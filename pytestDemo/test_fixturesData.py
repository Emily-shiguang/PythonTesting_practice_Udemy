import pytest
from pytestDemo.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])  # the info will be printed in emily@Chriss-MacBook-Pro pytestDemo % py.test --html=report1.html
        log.info(dataLoad[2])
        # print(dataLoad)
        print(dataLoad[2])
