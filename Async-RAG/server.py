from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.worker import process_query

app= FastAPI()


@app.get("/")
def root():
    return {"status": 'Server is up and running'}


@app.post("/chat")
def chat(
    query: str = Query(..., description="The user query to be processed and answered based on the retrieved context.")
):
    job = queue.enqueue(process_query, query)
    return {"status": "queued", "job_id": job.id}


@app.get("/job-status")
def get_result(
    job_id: str = Query(..., description="The ID of the job to retrieve the result for")
):
    job = queue.fetch_job(job_id=job_id)
    if job is None:
        return {"status": "error", "message": "Job not found"}

    if job.is_finished:
        return {"status": "finished", "result": job.result}

    if job.is_failed:
        return {"status": "failed", "message": str(job.exc_info)}

    return {"status": job.get_status(), "result": None}




