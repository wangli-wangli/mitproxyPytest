import pytest
import os
if __name__ == '__main__':
    pytest.main()
    adb1="cd pytest_test"
    adb2="allure generate allure-results/ -o allure-report --clean"
    os.system(adb1)
    os.system(adb2)
    # adb3="allure serve allure allure-results"
    # #adb3="allure open -h 127.0.0.1 -p 8083 allure-report"
    # os.system(adb3)


