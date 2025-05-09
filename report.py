from datetime import datetime
from typing import Dict, List


def get_report_filename(base_name: str) -> str:
    """Функция для создания имени файла с текущей датой."""
    today = datetime.now().strftime("%m.%d")
    name, ext = base_name.split('.')
    return f"{name}_{today}.{ext}"


def generate_payout_report(employees: List[Dict[str, str]]) -> Dict[str, List[Dict]]:
    """Функция для создания отчета по зарплатам."""
    report = {}
    for employee in employees:
        dept = employee["department"]
        hours = int(employee["hours_worked"])
        rate = int(employee[employee["rate_key"]])
        payout = hours * rate

        if dept not in report:
            report[dept] = []
        report[dept].append({
            "name": employee["name"],
            "hours": hours,
            "rate": rate,
            "payout": payout
        })

    for dept in report:
        total_hours = sum(emp["hours"] for emp in report[dept])
        total_payout = sum(emp["payout"] for emp in report[dept])
        report[dept].append({
            "totals": {"hours": total_hours, "payout": total_payout}
        })
    return report


reports = {
    "payout": generate_payout_report,
}
