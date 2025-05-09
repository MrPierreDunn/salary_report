from datetime import datetime

from report import generate_payout_report, get_report_filename


def test_generate_payout_report():
    employees = [
        {"name": "Alice", "department": "Marketing", "hours_worked": "160", "rate_key": "rate", "rate": "50"},
        {"name": "Bob", "department": "Design", "hours_worked": "150", "rate_key": "rate", "rate": "40"}
    ]
    report = generate_payout_report(employees)
    assert "Marketing" in report
    assert report["Marketing"][0]["payout"] == 8000


def test_generate_filename():
    today = datetime.now().strftime("%m.%d")
    name = "test_salary.json"
    test_name = get_report_filename(name)
    assert test_name == f"test_salary_{today}.json"
