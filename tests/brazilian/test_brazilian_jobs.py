from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs_list = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    job_keys_in_english = jobs_list[0].keys()
    assert "title" in job_keys_in_english
    assert "salary" in job_keys_in_english
    assert "type" in job_keys_in_english
