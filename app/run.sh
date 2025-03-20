#!/bin/bash
echo "Running Sample-1 ..."
python ./sample-1.py
python ./transform-log.py './logs/sample-1.log'

echo "Running Sample-2 ..."
python ./sample-2.py
python ./transform-log.py './logs/sample-2.log'