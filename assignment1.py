import io
import sys

import pytest
from unittest import mock

from libs import get_data, get_data_list, DATA1


# write unittest for this function
def show_square():
    return_data = get_data()
    if not return_data:
        return False

    data_list_data = get_data_list()
    for data_object in data_list_data:
        print(data_object.get('number') ** 2)
        if data_object.get('number') == 1:
            print("Found")
    return True


@pytest.mark.parametrize(['case', 'data', 'output_params', 'expect'], DATA1)
def test_show_square(case, data, output_params, expect):
    mock.patch('assignment1.get_data', return_value=data.get('output')).start()
    mock.patch('assignment1.get_data_list', return_value=data.get('input')).start()
    output = io.StringIO()
    sys.stdout = output
    return_value = show_square()
    sys.stdout = sys.__stdout__
    # print(return_value)
    print(output_params)
    if len(data.get('output')) != 0:
        assert output.getvalue() == output_params
        assert return_value == expect
    else:
        assert return_value == expect
