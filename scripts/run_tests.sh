#!/bin/bash
python -m pytest tests/ --html=reports/test_report.html --self-contained-html

rm -r __pycache__/ .pytest_cache/ tests/__pycache__

exit 0

