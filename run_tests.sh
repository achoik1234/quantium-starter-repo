#!/bin/bash


set -e

if [ -d "venv" ]; then
    source venv/Scripts/activate 
    
else
    echo "Virtual environment not found!"
    exit 1
fi


pytest -v

TEST_RESULT=$?


if [ $TEST_RESULT -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
