import pytest

from reader import detect_rate_collumn, read_employees_from_csv


def test_detect_rate_column():
    assert detect_rate_collumn(["id", "hourly_rate"]) == "hourly_rate"
    assert detect_rate_collumn(["name", "rate"]) == "rate"
    assert detect_rate_collumn(["salary", "hours"]) == "salary"
    assert detect_rate_collumn(["id", "name"]) is None


def test_read_csv_with_different_rate_columns(tmp_path):
    csv_data = "id,name,hourly_rate\n1,Alice,50"
    file_path = tmp_path / "test1.csv"
    file_path.write_text(csv_data)
    employees = read_employees_from_csv(file_path)
    assert employees[0]["rate_key"] == "hourly_rate"

    csv_data = "id,name,rate\n2,Bob,40"
    file_path.write_text(csv_data)
    employees = read_employees_from_csv(file_path)
    assert employees[0]["rate_key"] == "rate"


def test_read_csv_missing_rate_column(tmp_path):
    csv_data = "id,name,hours\n1,Alice,160"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_data)
    with pytest.raises(ValueError):
        read_employees_from_csv(file_path)
