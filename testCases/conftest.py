import pytest
from selenium import webdriver
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser ..............")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser ..............")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser ..............")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to the setup method
    return request.config.getoption("--browser")


#############################   Pytest HTML Report  ############################################

# Its is hook for Adding Environment Info to the HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Handicap Automation'
#     config._metadata['Module Name'] = 'Login Test Automation'
#     config._metadata['Tester'] = 'Shah Newaj'


# Its is hook for delete/Modify Environment Info to the HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
