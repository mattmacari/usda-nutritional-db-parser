# usda-nutritional-db-parser

[![Documentation Status](https://readthedocs.org/projects/usda-nutritional-db-parser/badge/?version=latest)](https://usda-nutritional-db-parser.readthedocs.io/en/latest/?badge=latest) [![Updates](https://pyup.io/repos/github/mattmacari/usda-nutritional-db-parser/shield.svg)](https://pyup.io/repos/github/mattmacari/usda-nutritional-db-parser/) [![Build Status](https://travis-ci.org/mattmacari/usda-nutritional-db-parser.svg?branch=master)](https://travis-ci.org/mattmacari/usda-nutritional-db-parser)

USDA National Nutrient Database Parser


## Quickstart

To get started with this repo:

```sh
    git clone git@github.com:mattmacari/usda-nutritional-db-parser.git
    cd usda-nutritional-db-parser
    python -m  venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install -r prod.txt
```

To get started developing with the repo:

```sh
    git clone git@github.com:mattmacari/usda-nutritional-db-parser.git
    cd usda-nutritional-db-parser
    python -m  venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install -r dev.txt
```

To run the test suite:

```sh
    git clone git@github.com:mattmacari/usda-nutritional-db-parser.git
    cd usda-nutritional-db-parser
    python -m  venv env
    source env/bin/activate
    python setup.py test
```

### Common Tasks

To download the USDA's nutritional database in ASCII and decompress it:

```sh
    # Make sure your virtual env is active.
    download --output-dir {directory} --decompress
```

## TODO

    * Get documentation working.
