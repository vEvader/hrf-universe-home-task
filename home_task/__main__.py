import argparse
from statistics_calculator import calculate_statistics_by_country_code, calculate_statistics_by_standard_job_id


min_postings_default = 5



def main():
    parser = argparse.ArgumentParser(description='My command line program')
    parser.add_argument('-m', '--min-postings', type=int, default=min_postings_default, help="Minimum number of job postings for statistics to be saved")
    args = parser.parse_args()
    
    calculate_statistics_by_country_code(min_posting_count=args.min_postings)
    calculate_statistics_by_standard_job_id(min_posting_count=args.min_postings)


if __name__ == '__main__':
   main()