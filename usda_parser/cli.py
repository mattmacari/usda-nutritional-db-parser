# -*- coding: utf-8 -*-

"""Console script for usda_parser."""
import sys
import logging
import os

import click

from usda_parser import extract

logger = logging.getLogger(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


@click.command()
@click.option('--output-dir', help='archive download directory', default=lambda: os.getcwd())
@click.option('--decompress/--no-decompress', default=True)
def download_archive(output_dir, decompress):
    logger.info(f' downloading file using {output_dir} as target')
    archive_path = extract.download_db_archive(output_dir=output_dir)
    if decompress:
        click.echo(f' decompressing archive {archive_path} to {output_dir}')
        extract.extract_db_archive(archive_file_path=archive_path)
    return 0
