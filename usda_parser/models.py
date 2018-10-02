"""
usda_parser.models
~~~~~~~~~~~~~~~~~~

Contains a dictionary that maps the file name to the associated record
structure. This was not implemented using an ORM since the parser's
end point is not always a  database.

"""

DATA_SRC = {
    'table': 'data_src',
    'fields': [
        'data_src_id',
        'authors',
        'title',
        'year',
        'journal',
        'vol_city',
        'issue_state',
        'start_page',
        'end_page'
    ]
}

DATSRCLN = {
    'table': 'data_source_links',
    'fields': [
        'nbd_no',
        'nutr_no',
        'data_src_id'
    ]
}

DERIV_CD = {
    'table': 'data_derivation_cd',
    'fields': [
        'deriv_cd',
        'deriv_descr'
    ]
}


FD_GROUP = {
    'table': 'food_group',
    'fields': [
        'code',
        'description'
    ]
}

FOOD_DES = {
    'table': 'food_descr',
    'fields': [
        'ndb_nbr',
        'food_group_cd',
        'long_descr',
        'short_descr',
        'common_name',
        'manufacturer_name',
        'survey_ind',
        'refuse_descr',
        'scientific_name',
        'n_factor',
        'pro_factor',
        'fat_factor',
        'carb_factor'
    ]
}

FOOTNOTE = {
    'table': 'footnote',
    'fields': [
        'nbd_no',
        'footnt_nbr',
        'footnt_type',
        'nutr_no',
        'footnt_txt'
    ]
}

LANGDESC = {
    'table': 'langual_descr',
    'fields': [
        'factor_code',
        'description'
    ]
}

LANGUAL = {
    'table': 'langual_thes',
    'fields': [
        'nbd_no',
        'factor_code'
    ]
}

NUT_DATA = {
    'table': 'nutrient_data',
    'fields': [
        'nbd_nbr',
        'nutr_nbr',
        'nutr_value',
        'num_data_pts',
        'std_err',
        'src_cd',
        'deriv_cd',
        'ref_nbd_no',
        'add_nutr_flag',
        'nbr_studies',
        'min_value',
        'max_value',
        'deg_fdm',
        'low_eb',
        'upper_eb',
        'stats_cmts',
        'add_mod_dt',
        'cc'
    ]
}

NUTR_DEF = {
    'table': 'nutrient_def',
    'fields': [
        'nutr_nbr',
        'units',
        'tag_name',
        'nutr_descr',
        'nbr_decimal',
        'sort_order'
    ]
}

SRC_CD = {
    'table': 'source_code',
    'fields': [
        'src_cd',
        'src_cd_descr'
    ]
}

WEIGHT = {
    'table': 'weight',
    'fields': [
        'nbd_no',
        'seq',
        'amount',
        'msre_desc',
        'gm_weight',
        'num_data_pts',
        'std_dev'
    ]
}

