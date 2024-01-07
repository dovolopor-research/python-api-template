from pydantic import BaseModel


class BaseRes(BaseModel):
    success: bool = True
    message: str = ""


class VersionRes(BaseRes):
    version: str = "1.0.0"


class DataReq(BaseModel):
    data: str


class DataRes(BaseRes):
    data: str
