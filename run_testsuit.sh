#!/bin/bash
source ./venv/Scripts/activate
pytest testsuit.py
TEST_EXIT_CODE=$?
deactivate
if [ $TEST_EXIT_CODE -eq 0 ]; then
  exit 0
else
  exit 1
fi
