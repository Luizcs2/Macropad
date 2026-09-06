from fastapi import APIRouter, HTTPException

from ..schemas.commands import CommandReq
from ..services.commands.apps import open_app
from ..services.commands.sys import sys_command

router = APIRouter(tags=["commands"], prefix="/commands")


@router.post("/app/open")
def app_start(req: CommandReq):
    try:
        open_app(req)
        return {"status": "Completed"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.post("/system")
def system_command(req: CommandReq):
    try:
        sys_command(req)
        return {"status": "Completed"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except RuntimeError as e: 
        raise HTTPException(status_code=500, detail=str(e)) from e


