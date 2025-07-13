from database import db
from schemas import BogieChecksheetInput
from bson import ObjectId
from typing import Optional

# --- Submit Bogie Checksheet ---
async def submit_bogie_checksheet(payload: BogieChecksheetInput):
    try:
        doc = payload.dict()
        await db.bogie_checksheet.insert_one(doc)
        return {
            "data": {
                "formNumber": payload.formNumber,
                "inspectionBy": payload.inspectionBy,
                "inspectionDate": payload.inspectionDate,
                "status": "Saved"
            },
            "message": "Bogie checksheet submitted successfully.",
            "success": True
        }
    except Exception as e:
        return {
            "data": {},
            "message": f"Error submitting checksheet: {str(e)}",
            "success": False
        }

# --- Get Filtered Wheel Specs ---
async def get_filtered_wheel_specs(
    formNumber: Optional[str] = None,
    submittedBy: Optional[str] = None,
    submittedDate: Optional[str] = None
):
    try:
        filters = {}
        if formNumber:
            filters["formNumber"] = formNumber
        if submittedBy:
            filters["submittedBy"] = submittedBy
        if submittedDate:
            filters["submittedDate"] = submittedDate

        cursor = db.wheel_spec.find(filters)
        results = []

        async for doc in cursor:
            results.append({
                "fields": doc.get("fields", {}),
                "formNumber": doc.get("formNumber", ""),
                "submittedBy": doc.get("submittedBy", ""),
                "submittedDate": doc.get("submittedDate", ""),
                "_id": str(doc.get("_id", ""))
            })

        return {
            "data": results,
            "message": "Filtered wheel specification forms fetched successfully.",
            "success": True
        }

    except Exception as e:
        return {
            "data": [],
            "message": f"Error fetching data: {str(e)}",
            "success": False
        }
