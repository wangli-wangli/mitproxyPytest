import pytest
from py._xmlgen import html
from interface_parms import api_val
#在测试报告中添加接口信息
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item,call):
    '''
    在测试报告中添加接口信息
    :param item:
    :return:
    '''
    outcome=yield
    report=outcome.get_result()
    report.description = str(item.function.__doc__)

@pytest.mark.opionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("模块"))
    cells.insert(2, html.th("状态码"))
    cells.insert(3, html.th("url"))
    cells.insert(4, html.th("响应参数"))
    cells.insert(5, html.th("请求参数",class_='json'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.th(report.description))
    cells.insert(2,html.th(api_val.statue_code))
    cells.insert(3, html.th(api_val.url))
    cells.insert(4, html.th(api_val.reponse))
    cells.insert(5, html.th(api_val.request))



