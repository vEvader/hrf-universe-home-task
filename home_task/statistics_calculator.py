from statistics_service import get_country_codes, get_standard_job_ids, update_record, get_calculated_statistics



# def _calculate_statistics(statistics_values):
#     min_days_to_hire = int(np.percentile(statistics_values, 10))
#     max_days_to_hire = int(np.percentile(statistics_values, 90))
#     avg_days_to_hire = np.mean(statistics_values[(len(statistics_values)*10//100):(len(statistics_values)*90//100)])
#     num_postings = len(statistics_values)
#     return min_days_to_hire, max_days_to_hire, avg_days_to_hire, num_postings

def calculate_statistics_by_country_code(min_posting_count: int):
    country_codes = get_country_codes()

    for country_code in country_codes:
        if not country_code:
            continue
    
        # statistics_values = get_statistics_values_by_country_code(country_code=country_code)
        # if not statistics_values or len(statistics_values) < min_posting_count:
        #     continue
        
        min_days_to_hire, max_days_to_hire, avg_days_to_hire, num_postings = get_calculated_statistics(country_code=country_code)

        if num_postings > min_posting_count:
            update_record(
                country_code=country_code,
                standard_job_id=None,
                min_days_to_hire=min_days_to_hire,
                max_days_to_hire=max_days_to_hire,
                avg_days_to_hire=avg_days_to_hire,
                num_postings=num_postings
            )


def calculate_statistics_by_standard_job_id(min_posting_count: int):
    standard_job_ids = get_standard_job_ids()

    for standard_job_id in standard_job_ids:
        if not standard_job_id:
            continue

        # statistics_values = get_statistics_values_by_standard_job_id(standard_job_id=standard_job_id)
        # if not statistics_values or len(statistics_values) < min_posting_count:
        #     continue
        # min_days_to_hire, max_days_to_hire, avg_days_to_hire, num_postings = _calculate_statistics(statistics_values=statistics_values)

        min_days_to_hire, max_days_to_hire, avg_days_to_hire, num_postings = get_calculated_statistics(standard_job_id=standard_job_id)

        if num_postings > min_posting_count:
            update_record(
                country_code=None,
                standard_job_id=standard_job_id,
                min_days_to_hire=min_days_to_hire,
                max_days_to_hire=max_days_to_hire,
                avg_days_to_hire=avg_days_to_hire,
                num_postings=num_postings
            )