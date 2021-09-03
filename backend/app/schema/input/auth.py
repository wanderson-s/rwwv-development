from pydantic import BaseModel, Field


class BaseLogin(BaseModel):
    email: str = Field(..., regex="^[a-z0-9.]+@taimin\.com\.br")
    password: str  # = Field(..., regex="^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")
