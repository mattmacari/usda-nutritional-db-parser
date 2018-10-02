from usda_parser.parser import (
    clean_record,
    parse_file,
    parse_data_files
)


def test_clean_record():
    rec = ['~test~', '~data~', '~value~']
    fields = ['col1', 'col2', 'col3']
    res = clean_record(rec, fields)
    expected_res = {
        'col1': 'test',
        'col2': 'data',
        'col3': 'value'
    }
    assert res == expected_res


def test_parse_file(sample_data_path):
    field_names = ['code', 'description']
    file_path = sample_data_path
    data = parse_file(file_path, field_names=field_names)
    assert isinstance(data, list)
    assert len(data) == 6


def test_parse_data_files(sample_data_path):
    # build file_mappings
    file_mappings = {
        'FD_GROUP': sample_data_path
    }
    res = parse_data_files(file_mappings)
    assert isinstance(res, dict)
    assert 'food_group' in res
    assert len(res.keys()) == 1
