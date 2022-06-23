#!/bin/bash
rm -rf build dist chiral_db_grpc_client.egg-info
python3 setup.py sdist
python3 setup.py bdist_wheel
twine upload dist/*
rm -rf build dist chiral_db_grpc_client.egg-info