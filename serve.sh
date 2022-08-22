#!/bin/bash
source env/bin/activate
env/bin/python generate-indexs.py && mkdocs serve