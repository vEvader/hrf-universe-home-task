import db
import datetime
import uuid
from sqlalchemy import func
from models import JobPosting, HireStatistics


session = db.get_session()


def _get_statistics_values(column, column_value: str):
    days_to_hire_values = session.query(JobPosting.days_to_hire).\
        filter(column == column_value).\
        filter(JobPosting.days_to_hire != None).\
        all()
    values = [days_val[0] for days_val in days_to_hire_values]
    return values


def get_country_codes():
    country_code_rows = session.query(JobPosting.country_code.distinct()).all()
    country_codes = [country_code_row[0] for country_code_row in country_code_rows if country_code_row and country_code_row[0]]
    return country_codes


def get_standard_job_ids():
    standard_job_id_rows = session.query(JobPosting.standard_job_id.distinct()).all()
    standard_job_ids = [standard_job_id_row[0] for standard_job_id_row in standard_job_id_rows if standard_job_id_row and standard_job_id_row[0]]
    return standard_job_ids


def get_statistics_values_by_country_code(country_code: str):
    return _get_statistics_values(JobPosting.country_code, country_code)


def get_statistics_values_by_standard_job_id(standard_job_id: str):
    return _get_statistics_values(JobPosting.standard_job_id, standard_job_id)


def get_calculated_statistics(country_code = None, standard_job_id = None):
    q = session.query(
        func.percentile_cont(0.1).within_group(JobPosting.days_to_hire),
        func.percentile_cont(0.9).within_group(JobPosting.days_to_hire),
        func.avg(JobPosting.days_to_hire)
    )
    num_query = session.query(JobPosting)
    if country_code:
        q = q.filter(JobPosting.country_code == country_code)
        num_query = num_query.filter(JobPosting.country_code == country_code)
    elif standard_job_id:
        q = q.filter(JobPosting.standard_job_id == standard_job_id)
        num_query = num_query.filter(JobPosting.standard_job_id == standard_job_id)
    else:
        return None, None
    result = q.one()
    percentile_10 = result[0]
    percentile_90 = result[1]
    average = result[2]
    num_postings = num_query.filter(JobPosting.days_to_hire > percentile_10).filter(JobPosting.days_to_hire < percentile_90).count()
    return percentile_10, percentile_90, average, num_postings


def update_record(country_code: str, standard_job_id: str, min_days_to_hire: int, max_days_to_hire: int, avg_days_to_hire: int, num_postings: int) -> None:
    if country_code:
        statistics_record = session.query(HireStatistics).filter(HireStatistics.country_code == country_code).first()
    elif standard_job_id:
        statistics_record = session.query(HireStatistics).filter(HireStatistics.standard_job_id == standard_job_id).first()

    if statistics_record:
        statistics_record.min_days_to_hire = min_days_to_hire
        statistics_record.max_days_to_hire = max_days_to_hire
        statistics_record.avg_days_to_hire = avg_days_to_hire
        statistics_record.num_postings = num_postings
        statistics_record.calculation_date = datetime.datetime.now()
    else:
        statistics_record = HireStatistics(
            id=str(uuid.uuid4()),
            standard_job_id=standard_job_id,
            country_code=country_code,
            min_days_to_hire=min_days_to_hire,
            max_days_to_hire=max_days_to_hire,
            avg_days_to_hire=avg_days_to_hire,
            num_postings=num_postings,
            calculation_date=datetime.datetime.now()
        )
        session.add(statistics_record)
    session.commit()    
