import os
import random
import zipfile
from string import ascii_letters

import pytest

NUM_OF_FILES = 4


@pytest.fixture
def test_file_names():
    return (
    'hello.txt',
    'world.txt',
)


@pytest.fixture
def temp_dir(tmpdir):
    return str(tmpdir.mkdir('usda_test'))


@pytest.fixture
def test_archive(temp_dir, test_file_names):
    """
    Creates a test archive, and returns the file path.
    """
    test_files = dict()

    tmp_file_path = os.path.join(temp_dir, 'test.zip')

    for fname in test_file_names:
        buf = '~'.join([''.join(random.choices(ascii_letters, k=random.randint(3,20)))
                  for _ in range(random.randint(3, 9))])
        test_files.update({fname: buf})

    with zipfile.ZipFile(tmp_file_path, 'w',  zipfile.ZIP_STORED, False) as zf:
        for f_name, val in test_files.items():
            zf.writestr(f_name, val)

    return tmp_file_path