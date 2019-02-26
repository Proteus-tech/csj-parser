from csj_parser.csj import Csj


class TestConvertCsjToDict():
    
    def test_convert_csj_to_dict(self):
        csj_string = '"key1","key2","key3","key4"\n"value1","value2","value3","value4"\n'
        list_of_dicts = [{
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
            "key4": "value4"
        }]
        result_dict = Csj.to_dict(csj_string)
        assert result_dict == list_of_dicts

    def test_convert_csj_to_dict_multiple_row(self):
        csj_string = '"key1","key2","key3","key4"\n"value1","value2","value3","value4"\n"value1","value2","value3","value4"\n'
        list_of_dicts = [
            {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4"
            },
            {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4"
            }
        ]
        result_dict = Csj.to_dict(csj_string)
        assert result_dict == list_of_dicts

    def test_convert_csj_to_dict_contain_object(self):
        csj_string = ''' "key1","key2","key3","key4"\n"value1",{}"key": "value"{},"value3",{}"key": "value"{}\n '''.format('{', '}', '{', '}')
        list_of_dicts = [
            {
                "key1": "value1",
                "key2": {"key": "value"},
                "key3": "value3",
                "key4": {"key": "value"}
            }
        ]

        result_dict = Csj.to_dict(csj_string)
        assert result_dict == list_of_dicts

    def test_convert_csj_to_dict_multiple_row_and_contain_object(self):
        csj_string = ''' "key1","key2","key3","key4"\n"value1",{}"key": "value"{},"value3",{}"key": "value"{}\n"value1","value2","value3","value4"\n '''.format('{', '}', '{', '}')
        list_of_dicts = [
            {
                "key1": "value1",
                "key2": {"key": "value"},
                "key3": "value3",
                "key4": {"key": "value"}
            },
            {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4"
            }
        ]
        result_dict = Csj.to_dict(csj_string)
        assert result_dict == list_of_dicts

    def test_convert_csj_to_dict_with_no_row(self):
        csj_string = '"key1","key2","key3","key4"\n'
        list_of_dicts = []
        result_dict = Csj.to_dict(csj_string)
        assert result_dict == list_of_dicts


class TestConvertDictToCsj():

    def test_convert_dict_to_csj(self):
        list_of_dicts = [
            {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4"
            },
            {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4"
            }
        ]
        csj_string = '"key1","key2","key3","key4"\n"value1","value2","value3","value4"\n"value1","value2","value3","value4"\n'
        result_csj_string = Csj.from_dicts(list_of_dicts)
        assert result_csj_string == csj_string
    
    def test_convert_dict_to_csj_multiple_row_and_contain_object(self):
        list_of_dicts = [
            {
                "key1": "value1",
                "key2": {"key": "value"},
                "key3": "value3",
                "key4": {"key": "value"}
            },
            {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4"
            }
        ]
        csj_string = '''"key1","key2","key3","key4"\n"value1",{}"key":"value"{},"value3",{}"key":"value"{}\n"value1","value2","value3","value4"\n'''.format('{', '}', '{', '}')
        result_csj_string = Csj.from_dicts(list_of_dicts)
        assert result_csj_string == csj_string
