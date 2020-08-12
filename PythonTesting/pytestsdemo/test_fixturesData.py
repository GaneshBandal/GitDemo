
import pytest

from PythonTesting.pytestsdemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def editProfile(self,dataLoad):
        log=self.getLogger()
        #error bcoz if u want to return data to the specific test then u have to add parameter
        log.info(dataLoad[0])
