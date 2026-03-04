#!/bin/bash
PWD=$(pwd)
echo $PWD
source $PWD/venv/bin/activate

python3 $PWD/backend/main.py
