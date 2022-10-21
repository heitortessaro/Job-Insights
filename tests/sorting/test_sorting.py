import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs_list():
    return [
        {
            "job": "test1",
            "min_salary": 2,
            "max_salary": 10,
            "date_posted": "2022-01-01.",
        },
        {
            "job": "test2",
            "min_salary": 1,
            "max_salary": 8,
            "date_posted": "2022-02-02.",
        },
        {
            "job": "test3",
        },
    ]


@pytest.fixture
def jobs_list_by_min_salary():
    return [
        {
            "job": "test2",
            "min_salary": 1,
            "max_salary": 8,
            "date_posted": "2022-02-02.",
        },
        {
            "job": "test1",
            "min_salary": 2,
            "max_salary": 10,
            "date_posted": "2022-01-01.",
        },
        {
            "job": "test3",
        },
    ]


@pytest.fixture
def jobs_list_by_max_salary():
    return [
        {
            "job": "test1",
            "min_salary": 2,
            "max_salary": 10,
            "date_posted": "2022-01-01.",
        },
        {
            "job": "test2",
            "min_salary": 1,
            "max_salary": 8,
            "date_posted": "2022-02-02.",
        },
        {
            "job": "test3",
        },
    ]


@pytest.fixture
def jobs_list_by_date_posted():
    return [
        {
            "job": "test1",
            "min_salary": 2,
            "max_salary": 10,
            "date_posted": "2022-01-01.",
        },
        {
            "job": "test2",
            "min_salary": 1,
            "max_salary": 8,
            "date_posted": "2022-02-02.",
        },
        {
            "job": "test3",
        },
    ]


def test_sort_by_criteria(
    jobs_list,
    jobs_list_by_min_salary,
    jobs_list_by_max_salary,
    jobs_list_by_date_posted,
):
    job_list_test_min_salary = jobs_list.copy()
    sort_by(job_list_test_min_salary, "min_salary")
    assert job_list_test_min_salary == jobs_list_by_min_salary
    job_list_test_max_salary = jobs_list.copy()
    sort_by(job_list_test_max_salary, "max_salary")
    assert job_list_test_max_salary == jobs_list_by_max_salary
    job_list_test_date_posted = jobs_list.copy()
    sort_by(job_list_test_date_posted, "date_posted")
    assert job_list_test_date_posted == jobs_list_by_date_posted
