import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile is being created")
    # from here u can pass ur data to the test
    # u can send this data at run time which needs it
    return ["abcd","efgh","abcdefgh.com"]
# now go to the fixtureDemo class


#@pytest.fixture(params=["chrome","firefox","IE"])
@pytest.fixture(params=[("chrome","abcd","abcdefgh.com"),("firefox","abcd"),"IE"])  # multiple values in one single run
# first it will give chrome to the test case and ur test case will run
# now send this data
def crossBrowser(request):
    # first time the chrome will be picked and it is sent
    # and now take it into fixturesData
    return request.param



