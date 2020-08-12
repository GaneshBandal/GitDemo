# Will try assertions here

# If u want run test based on smoke or regression, suppose u want to identify some test cases as smoke
# and you want to run only those test cases, for that in pytest there is a concept called mark where u can
# mark the set of test cases and u can tell cmd to run only mark related test cases
# If I want to run only those test cases which are marked as smoke use keyword called -m py.test -m smoke -v -s

# Now if we want to skip a test, @pytest.mark.skip
# suppose u r skipping test case but it is prerequisite of some operation then u can skip reporting that test case
# @pytest.mark.xfail = > the test case will run but u wont be able to see in o/p as pass or fail

import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    msg="Hello"
    assert msg=="Hi","Test failed bcoz no string match"


def test_SecondCreditCard():
    a=4
    b=6
    assert a+2==6,"Addition is not matching"
# If u want to run specific file give that file name only
# If u work with cucumber framework or TestNG, there is a concept called tagging or group
# From multiple files if u want to run selected test cases
# If we want to run one testcase from one file and another test case from another file
# Testcase name in pytest means method name only
# Run the method name having CreditCard text only  py.test -k CreditCard -v -s
# -k stands for method names execution, -s logs in o/p, -v stands for more info.


#Fixture

# @pytest.fixture()
# def setup():
#     print("I will be executing first")
#     yield
#     print("I will be executed last")

# Now we will create one more new test, this test does not have idea about setup method
# u can give connection to the fixture by passing method name as an argument
# when we run this method and when it come across the setup method
# In selenium,fixtures are used for opening a browser,setting up some db instances or
# creating some configuration properties, environment variables
def test_fixtureDemo(setup):
    print("I will execute steps in fixturedemo method")

# Now if u want to run after ur test case execution is done, no need to create
# another fixture post execution, u can write in setup fixture only
# yield keyword, whatever written after yield will be executed after ur test execution completed called teardown methods