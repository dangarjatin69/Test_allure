# test_simple_allure.py

import pytest
import allure

@allure.feature("Example Feature")
@allure.story("Simple arithmetic validation")
def test_addition():
    with allure.step("Compute 1 + 1"):
        result = 1 + 1

    with allure.step("Verify the result is 2"):
        assert result == 2

print("Hello World Testing")
