from uvicorn import run
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from util.data_model import BaseRes, VersionRes, DataReq, DataRes
from util.conf import get_conf
from util.log import get_logger


logger = get_logger("server.main")
conf = get_conf()
NAME = conf["server"]["name"]
VERSION = conf["server"]["version"]
app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(_, exc):
    return JSONResponse(BaseRes(success=False, message=str(exc)).model_dump())


@app.get("/")
def api_home() -> BaseRes:
    url = "http://" + conf["server"]["run"]["host"] + ":" + str(conf["server"]["run"]["port"]) + "/docs"
    return BaseRes(success=True, message=f"welcome {NAME}, docs in {url}")


@app.get("/version")
def api_version() -> VersionRes:
    return VersionRes(version=VERSION, success=True, message="")


@app.get("/test/{data}")
def api_get_data(data: str) -> DataRes:
    logger.info(data)
    try:
        res = DataRes.model_validate({
            "success": True,
            "message": "",
            "data": data
        })
    except Exception as e:
        logger.error(e)
        res = DataRes(success=False, message=str(e))
    logger.info(res)
    return res


@app.post("/test")
def api_post_test(msg_req: DataReq) -> DataRes:
    logger.info(msg_req)
    try:
        res = DataRes.model_validate({
            "success": True,
            "message": "",
            "data": msg_req.data
        })
    except Exception as e:
        logger.error(e)
        res = DataRes(success=False, message=str(e))
    logger.info(res)
    return res


if __name__ == "__main__":
    run("server.main:app", **conf["server"]["run"])
