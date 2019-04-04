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

    def test_convert_csj_to_dict_on_null(self):
        csj_string = '''"slug","title","released","length_minutes","created","tags","watched_last","watched_times"\n"t2","Terminator2: JudgementDay","1991-07-01",94,"2016-06-1108:54:12.895416+00",["adventure","action","dystopian","robots","time-travel","sci-fi"],null,null\n'''.format('{', '}', '{', '}')
        list_of_dicts = [
            {
                "slug": "t2",
                "title": "Terminator2: JudgementDay",
                "released": "1991-07-01",
                "length_minutes": 94,
                "created": "2016-06-1108:54:12.895416+00",
                "tags": ["adventure","action","dystopian","robots","time-travel","sci-fi"],
                "watched_last": None,
                "watched_times": None
            }
        ]
        result_dict = Csj.to_dict(csj_string)
        print(result_dict)
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
        print(result_csj_string)
        assert result_csj_string == csj_string

    def test_convert_dict_to_csj_on_null(self):
        list_of_dicts = [
            {
                "slug": "t2",
                "title": "Terminator 2: Judgement Day",
                "released": "1991-07-01",
                "length_minutes": 94,
                "created": "2016-06-11 08:54:12.895416+00",
                "tags": ["adventure","action","dystopian","robots","time-travel","sci-fi"],
                "watched_last": None,
                "watched_times": None
            }
        ]
        csj_string = '''"slug","title","released","length_minutes","created","tags","watched_last","watched_times"\n"t2","Terminator 2: Judgement Day","1991-07-01",94,"2016-06-11 08:54:12.895416+00",["adventure","action","dystopian","robots","time-travel","sci-fi"],null,null\n'''.format('{', '}', '{', '}')
        result_csj_string = Csj.from_dicts(list_of_dicts)
        assert result_csj_string == csj_string