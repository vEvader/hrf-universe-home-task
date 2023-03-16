from fastapi import FastAPI
from home_task import statistics_service


app = FastAPI()


@app.get("/stats/")
async def get_stats(standard_job_id: str = None, country_code: str = None):
    stats = statistics_service.get_record(country_code, standard_job_id)
    if not stats:
        return {"message": "No data found for the specified parameters."}
    result = {
        "standard_job_id": stats.standard_job_id,
        "country_code": stats.country_code,
        "min_days": stats.min_days_to_hire,
        "avg_days": stats.avg_days_to_hire,
        "max_days": stats.max_days_to_hire,
        "job_postings_number": stats.num_postings,
    }
    return result
