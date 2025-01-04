#!/bin/bash
source .venv/bin/activate
.venv/bin/python generate-indexs.py && 
mkdocs serve