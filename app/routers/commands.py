from fastapi import APIRouter, HTTPException

from ..schemas.commands import CommandReq
from ..services.commands.apps import open_app
from ..services.commands.sys import sys_sleep,sys_shutdown

router = APIRouter(tags=["commands"], prefix="/commands")

@router.post("/app/open")
def app_start(req:CommandReq):
    try:
        open_app(req)
        return {"status": "ok"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=(e)) from e
    except RuntimeError as e:
        raise HTTPException ( status_code=500, detail=(e)) from e

@router.post("/system/sleep")
def Sleep_system(req:CommandReq):
    try:
        sys_sleep(req)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=(e)) from e
    except RuntimeError as e:
        raise HTTPException(status_code=500 , detail=(e)) from e


