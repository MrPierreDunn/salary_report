from typing import Dict, List


def read_employees_from_csv(file_path: str) -> List[Dict[str, str]]:
    """Функция для прочтения CSV-файла."""
    employees = []
    with open(file_path, mode='r') as f:
        headers = [header.strip() for header in f.readline().split(',')]
        rate_key = detect_rate_collumn(headers)
        if not rate_key:
            raise ValueError(f"В файле {file_path} не найден столбец с "
                             "hourly rate (ожидаемые названия: "
                             "hourly_rate, rate, salary)")

        for line in f:
            if not line.strip():
                continue
            values = [v.strip() for v in line.split(',')]
            employee = dict(zip(headers, values))
            employee["rate_key"] = rate_key
            employees.append(employee)
    return employees


def detect_rate_collumn(headers: List[str]):
    """Функция для обнаружения колонки с hourly rate."""
    other_names = ("hourly_rate", "rate", "salary")
    for header in headers:
        if header in other_names:
            return header
    return None
