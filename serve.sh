#!/bin/bash
source env/bin/activate
env/bin/python nav-generate.py && mkdocs serve