# Any pytest file should start with test_ or end with _tests
#all tests must be in function
# Whenever you declare a function, pytest require test method name and should start with test_
import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

# There r different ways of running the program, u can use commands through cmd to run this test
# or u can depend upon testrunner available in pycharm, go to edit configuration and select pytest
# you can pass the python script path as well

# Running Pytests from Terminal with different command flags
# first go to the specific path till pytestsdemo as cd C:\Users\gbandal\gitstuff\PythonTesting\pytestsdemo
# suppose there r 100 testcases inside the package and you want to run all at a time give command as py.test
#but enough info. is not seen, to see that py.test -v  =>verbose means provides the test logs as well
# u r printing hello but not showing, by default console logs not defined in the o/p so for it => py.test -v -s



def test_crossBrowser(crossBrowser):
    # Attach the testcase to the specific fixture so have to pass fixturename as argument
    print(crossBrowser)

