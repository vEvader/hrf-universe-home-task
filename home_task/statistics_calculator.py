from .statistics_service import (
    get_country_codes,
    get_standard_job_ids,
    update_record,
    get_calculated_statistics
)


def _update_statistics(min_posting_count: int, country_code: str, standard_job_id: str):
    is_record_updated = False
    min_days_to_hire, max_days_to_hire, avg_days_to_hire, num_postings =\
        get_calculated_statistics(country_code=country_code, standard_job_id=standard_job_id)

    if num_postings > min_posting_count:
        update_record(
            country_code=country_code,
            standard_job_id=standard_job_id,
            min_days_to_hire=min_days_to_hire,
            max_days_to_hire=max_days_to_hire,
            avg_days_to_hire=avg_days_to_hire,
            num_postings=num_postings
        )
        is_record_updated = True
    return is_record_updated


def calculate_statistics(min_posting_count: int):
    country_codes = get_country_codes()
    standard_job_ids = get_standard_job_ids()
    calculated_records_count = 0

    for country_code in country_codes:
        for standard_job_id in standard_job_ids:
            is_record_updated = _update_statistics(
                min_posting_count=min_posting_count,
                country_code=country_code,
                standard_job_id=standard_job_id
            )
            if is_record_updated:
                calculated_records_count += 1
    return calculated_records_count
