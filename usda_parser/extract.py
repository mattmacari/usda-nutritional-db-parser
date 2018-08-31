import os
import tempfile
import logging
import zipfile

import requests as r

from .config import USDA_URL

logger = logging.getLogger(__name__)


def download_db_archive(url: str=USDA_URL, output_dir: str=None) -> str:
    """
    Downloads database archive from the default `USDA_URL`, or user specified
    location. The archive is downloaded to either the directory specified by
    `output_dir` or to a temporary file location determined and returned at
    runtime.

    :param str url: URL where the USDA database is contained.
    :return: Absolute path for the downloaded archive.
    :rtype: str
    """
    resp = r.get(url, stream=True)
    file_name = url.split('/')[-1]
    output_dir = output_dir if output_dir else tempfile.gettempdir()
    output_path = os.path.join(output_dir, file_name)
    logger.info('fetching {} and writing to {}'.format(url, output_path))
    with open(output_path, 'wb+') as f:
        for chunk in resp.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return output_path


def extract_db_archive(archive_file_path: str) -> dict:
    """
    Extracts the downloaded archive into the current working directory.

    :param str archive_file_path: path of archive to extract.
    :return: dictionary of file name and absolute path to the file.
    :rtype: dict
    """
    file_mapping = dict()
    o_path = os.path.dirname(archive_file_path)
    with zipfile.ZipFile(archive_file_path, mode='r') as zf:
        for file in zf.filelist:
            f_name = zf.extract(file.orig_filename, path=o_path)
            file_mapping[file.orig_filename] = f_name
    return file_mapping
