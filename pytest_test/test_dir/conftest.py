import pytest
@pytest.fixture(scope='module')#在用例执行前调用此函数
#autouse：如果True，则为所有测试用例不需要传参也会调用这个fixture。如果为False则需要显示的调用fixture。
def delete_project():
    '''删除计划'''
    pass
