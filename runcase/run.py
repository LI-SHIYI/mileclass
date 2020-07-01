import pytest
import warnings

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    # pytest.main(['../testcase/common_case/', '--html=../report/html/2.html', '-v'])
    # pytest.main(['../testcase/common_case/test_login.py', '--html=../report/html/1.html', '-v'])
    pytest.main(['../testcase/', '--html=../report/testcase.html', '--alluredir=../report/pre'])
