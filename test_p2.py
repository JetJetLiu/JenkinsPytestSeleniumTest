import pytest

from base.box import CsvHelper


class TestP2(object):

    csv_data = CsvHelper().read_data('data/1.csv')
    # csv_data = CsvHelper().read_data_as_dict('data/1.csv')

    @pytest.mark.parametrize('name,age',csv_data)
    def test_1(self,name,age):
        print(name,age)
        assert '张三' == name


