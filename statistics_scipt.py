import argparse
import logging
from home_task.statistics_calculator import calculate_statistics


min_postings_default = 5


def main():
    parser = argparse.ArgumentParser(description='My command line program')
    parser.add_argument(
        '-m',
        '--min-postings',
        type=int,
        default=min_postings_default,
        help="Minimum number of job postings for statistics to be saved"
    )
    args = parser.parse_args()

    try:
        calculated_records_count = calculate_statistics(min_posting_count=args.min_postings)
    except Exception as e:
        message = f"Exception appeared during script execution. message: {e}"
        logging.error(message)
        print(message)
    else:
        message = f"Script has been executed successfully.\n" +\
            f"updated: {calculated_records_count} records"
        logging.info(message)
        print(message)


if __name__ == '__main__':
    main()
