#!/bin/bash
python -m pytest tests/test_diabetes.py --html=reports/test_report.html --self-contained-html

rm -r __pycache__/ .pytest_cache/

exit 0

