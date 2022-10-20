from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them"""
    jobs_info = read(path)
    jobs_types = {
        row["job_type"] for row in jobs_info if len(row["job_type"]) > 0
    }
    return list(jobs_types)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type"""


# python3 -c 'from insights import get_unique_industries;
#  get_unique_industries("jobs.csv")'
def get_unique_industries(path):
    """Checks all different industries and returns a list of them"""
    jobs_info = read(path)
    industry_types = {
        row["industry"] for row in jobs_info if len(row["industry"]) > 0
    }
    return list(industry_types)


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_info = read(path)
    max_salaries = [
        int(row["max_salary"], base=10)
        for row in jobs_info
        if (len(row["max_salary"]) > 0 and row["max_salary"].isdigit())
    ]
    return max(max_salaries)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_info = read(path)
    min_salaries = [
        int(row["min_salary"], base=10)
        for row in jobs_info
        if (len(row["min_salary"]) > 0 and row["min_salary"].isdigit())
    ]
    return min(min_salaries)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
