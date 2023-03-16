from fastapi import FastAPI
from home_task import statistics_service


app = FastAPI()


@app.get("/stats/")
async def get_stats(standard_job_id: str = None, country_code: str = None):
    stats = statistics_service.get_record(country_code, standard_job_id)
    if not stats:
        return {"message": "No data found for the specified parameters."}
    return stats
