import pytest


# test cases might be increasing, in every test case we r passing fixture name
# if there are n no. of test cases, for every file we r passing fixture, so we can optimize this
# If u wrap all these methods in class then u can just declare the fixture on class level so that
# it will be automatically applied to each and every method of that class.
# def test_fixtureDemo(setup):
#     print("I will execute steps in fixtureDemo method")
#
# def test_fixtureDemo1(setup):
#     print("I will execute steps in fixtureDemo1 method")
#
# def test_fixtureDemo2(setup):
#     print("I will execute steps in fixtureDemo2 method")
#
# def test_fixtureDemo3(setup):
#     print("I will execute steps in fixtureDemo3 method")

# If u want to run your fixture only once before the class but not before
# each and every test case and after all test execution completes once (teardown)
# For this goto conftest file and fixture argument and write scope="class"

import pytest
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")


