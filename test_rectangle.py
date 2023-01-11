from rectangle import Rectangle
import pytest
import sys


@pytest.fixture
def helper_file():
    '''
    Create helper file in current working dir. If file exists overwrite it.

    Returns: file object
    '''
    file_name = 'temp.txt'
    fh = open(file_name, 'w')
    fh.write('Helper file created.\n')

    return fh

#fixture的使用可以简化代码，定义函数中的内容为重复性内容
@pytest.fixture()
def my_rect():
    rect = Rectangle(30, 15)
    return rect


#pytest.mark定义在函数前面，给用例打标签，可以分类或者筛选
#在使用之前需要创建一个pytest.ini在当前项目，并将标签名进行注册
@pytest.mark.blue

@pytest.mark.white
#@pytest.mark.skip(reason = "no longer testable")
def test_area(my_rect):
    assert my_rect.area() == 450



@pytest.mark.yellow
#@pytest.mark.skipif(sys.platform == 'win32', reason="unsuitable for this platform")
def test_perimeter(my_rect):
    assert my_rect.perimeter() == 90



@pytest.mark.black
@pytest.mark.parametrize("arg1, arg2", [(30, 10)])
def test_area(arg1, arg2, helper_file):
    helper_file.write('the size of the rectangle is 30*10')
    rect = Rectangle(arg1, arg2)
    assert rect.area() == 300