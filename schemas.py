from pydantic import BaseModel, Field
from typing import Optional, List, Dict

# ---------- Nested Sub-Schemas ----------

class BmbcChecksheet(BaseModel):
    adjustingTube: str
    cylinderBody: str
    pistonTrunnion: str
    plungerSpring: str

class BogieChecksheet(BaseModel):
    axleGuide: str
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str

class BogieDetails(BaseModel):
    bogieNo: str
    dateOfIOH: str
    deficitComponents: str
    incomingDivAndDate: str
    makerYearBuilt: str

# ---------- Request Model ----------

class BogieChecksheetInput(BaseModel):
    bmbcChecksheet: BmbcChecksheet
    bogieChecksheet: BogieChecksheet
    bogieDetails: BogieDetails
    formNumber: str
    inspectionBy: str
    inspectionDate: str

# ---------- Response Models ----------

class BogieChecksheetResponse(BaseModel):
    data: dict  # You could improve by defining exact structure, but this is okay for now
    message: str
    success: bool

# ---------- Wheel Spec Models ----------

class WheelSpecItem(BaseModel):
    fields: Dict[str, str]
    formNumber: str
    submittedBy: str
    submittedDate: str
    id: Optional[str] = Field(default=None, alias="_id")  # Better naming for compatibility

    class Config:
        allow_population_by_field_name = True  # Allows returning "_id" as "id" if needed
        arbitrary_types_allowed = True
        json_encoders = {
            # Optional: ObjectId handling if you import from bson
            # ObjectId: str
        }

class WheelSpecResponse(BaseModel):
    data: List[WheelSpecItem]
    message: str
    success: bool
