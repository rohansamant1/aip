from fastapi import FastAPI, Query
from schemas import BogieChecksheetInput, BogieChecksheetResponse, WheelSpecResponse
from crud import submit_bogie_checksheet, get_filtered_wheel_specs

app = FastAPI()

@app.post("/api/bogie-checksheet", response_model=BogieChecksheetResponse, status_code=201)
async def create_bogie_checksheet(payload: BogieChecksheetInput):
    return await submit_bogie_checksheet(payload)

@app.get("/api/wheel-specification", response_model=WheelSpecResponse)
async def get_wheel_specifications(
    formNumber: str = Query(None),
    submittedBy: str = Query(None),
    submittedDate: str = Query(None)
):
    return await get_filtered_wheel_specs(formNumber, submittedBy, submittedDate)
