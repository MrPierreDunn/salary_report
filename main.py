import argparse
import json
from pathlib import Path

from reader import read_employees_from_csv
from report import get_report_filename, reports

DEFAULT_NAME = "salary_report.json"


def main():
    parser = argparse.ArgumentParser(
        description="Генератор отчетов по зарплате.",
        add_help=False,
        epilog="Примеры:"
               "  python main.py data.csv --report payout |"
               "  python main.py *.csv --report payout --name my_report.json"
    )
    parser.add_argument(
        "files", nargs="+",
        help="Путь к CSV файлам с данными сотрудников."
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=reports.keys(),
        help="Тип отчета (доступно: payout)."
    )
    parser.add_argument(
        "--name",
        help=f"Название файла с отчетом (по умолчанию: {DEFAULT_NAME})."
    )
    parser.add_argument(
        "-h", "--help", action="help",
        default=argparse.SUPPRESS, help="Вывести доступные команды"
    )

    args = parser.parse_args()

    employees = []
    for file_path in args.files:
        employees.extend(read_employees_from_csv(file_path))

    report = reports[args.report](employees)
    if args.name:
        report_name = get_report_filename(args.name)
    else:
        report_name = get_report_filename(DEFAULT_NAME)

    with open(report_name, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Отчёт '{args.report}' сохранён в: {Path(report_name).absolute()}")


if __name__ == "__main__":
    main()
