import pytest


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


def test_one(helper_file):
    helper_file.write('Using helper file in test_one')