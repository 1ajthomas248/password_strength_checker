from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from password_checker import check

app = FastAPI(
    title="Password Strength Checker API",
    description="API that analyzes password strength",
    version="1.0.0"
)

class PasswordRequest(BaseModel):
    password: str

class PasswordResponse(BaseModel):
    strength: str
    score: int
    is_common: bool
    has_digit: bool
    has_upper: bool
    has_lower: bool
    has_special: bool
    has_length: bool
    suggestions: list[str]

@app.post("/check", response_model=PasswordResponse)
def check_password(payload: PasswordRequest):
    if payload.password is None or payload.password == "":
        raise HTTPException(status_code=400, detail="Password can not be empty")
    
    result = check(payload.password)

    response = PasswordResponse(
        strength=result["strength"],
        score=result["score"],
        is_common=result["is_common"],
        has_digit=result["has_digit"],
        has_upper=result["has_upper"],
        has_lower=result["has_lower"],
        has_special=result["has_special"],
        has_length=result["has_length"],
        suggestions=result["suggestions"]
    )

    return response