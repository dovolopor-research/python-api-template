from sanic import Sanic
from sanic.response import text, json

from util.conf import get_conf
from util.data_model import Data
from util.db import get_mongo_client

conf = get_conf()
NAME = conf["server"]["name"]
VERSION = conf["server"]["version"]
app = Sanic(NAME)
mongo = get_mongo_client(conf)


@app.get("/")
async def index(_):
    return text(f"Hello from {NAME}: {VERSION}")


@app.get("/version")
async def version(_):
    return json({
        "name": NAME,
        "version": VERSION
    })


@app.post("/test")
def test(request):
    try:
        data = Data(**request.json)
        res = mongo["test"]["test"].find_one(data.json())
        if res:
            del res["_id"]

        result = {
            "status": 1,
            "message": "success",
            "data": res
        }

    except Exception as e:
        result = {
            "status": 0,
            "message": str(e)
        }
    return json(result)


if __name__ == "__main__":
    server_conf = conf["server"]
    app.run(
        host=server_conf["host"],
        port=server_conf["port"],
        debug=server_conf["debug"],
        auto_reload=server_conf["auto_reload"]
    )
