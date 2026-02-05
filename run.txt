@echo off
cd /d %~dp0

echo Running from:
cd

if not exist reports (
    mkdir reports
)

python -m pytest test_cases -v --browser chrome --html=reports/test_report.html --self-contained-html

pause
