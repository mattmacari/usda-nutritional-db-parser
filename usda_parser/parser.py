"""
usda_parser.parser
~~~~~~~~~~~~~~~~~

This module handles parsing the structured text files into lists of
dictionaries.

"""
import logging
import json
import os

from usda_parser import models

logger = logging.getLogger(__name__)


def clean_record(rec: list, field_names: list) -> dict:
    """
    Parses the record supplied by the calling function and returns a dictionary
    that can be transformed into a database record.

    :param rec: record extracted from file
    :ptype rec: list
    :param field_names: field names for the record
    :ptype field_names: list
    :rtype: Dictionary of cleaned elements.
    """
    return dict(zip(field_names, [elem.strip('~') for elem in rec]))


def parse_file(file_name: str, field_names: list) -> list:
    """
    Parses the file passed into as `file_name` and returns  a list of records
    based on the field_names provided.

    :param file_name: The name of the file to be parsed either as an absolute
                      or relative path.
    :ptype file_name: str
    :param field_names: The list of field names
    :ptype field_names: list
    :rtype: List of cleaned records from a given file.
    """
    with open(file_name, 'rU', encoding='windows-1252') as f:
        return [clean_record(row.strip('\n').split('^'), field_names)
                for row in f]


def parse_data_files(file_mappings: dict) -> dict:
    """
    Parses the list of files contained in the mapping and returns a dictionary
    of records.

    :param file_mappings: Dictionary of file mappings provided
        by :py:meth:`usda_parser.extract.extract_db_archive`
    :ptype file_mappings: dict

    :rtype: dictionary of mapped models.

    """
    ret_models = {}
    for model_name, file_name in file_mappings.items():
        logger.debug(f'Starting to parse {model_name} at {file_name}')
        model_def = getattr(models, model_name.split('.')[0])
        ret_models[model_def['table']] = parse_file(
            file_name=file_name,
            field_names=model_def['fields']
        )
    return ret_models


def write_parsed_data(data: list, output_dir: str) -> None:
    """
    Writes the parsed data sets out to the target JSON files.

    :param data: JSON list of data to be written out to individual files.
    :ptype data: list
    :param output_dir: output directory where files should be written.
    :ptype output_dir: str
    """
    for doc_name, doc in data.items():
        target_file = os.path.join(output_dir, '{}.json'.format(doc_name))
        logger.debug('Writing {} data out to {}.'.format(
            doc_name,
            target_file)
        )
        with open(target_file, 'w') as f:
            json.dump(doc, f, indent=4, sort_keys=True)
