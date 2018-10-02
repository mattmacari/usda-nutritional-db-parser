import os

from usda_parser.extract import download_db_archive, extract_db_archive


def test_download_db_archive(temp_dir, mocker):
    mocker.patch('requests.get')
    ret_value = download_db_archive(output_dir=temp_dir)

    assert isinstance(ret_value, str)
    assert ret_value == os.path.join(temp_dir, 'sr28asc.zip')


def test_extract_db_archive(temp_dir, test_archive, test_file_names):
    extracts = extract_db_archive(test_archive)
    for key, val in extracts.items():
        assert key in test_file_names
        assert os.path.exists(val)
