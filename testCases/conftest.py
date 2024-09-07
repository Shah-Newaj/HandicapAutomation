import pytest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver
