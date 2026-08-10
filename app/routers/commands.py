from fastapi import APIRouter, logger

from ..schemas.commands import Command
from ..services.commands.appStartup import open_app

router = APIRouter(tags=["commands"], prefix="/commands")

@router.post("/open")
def app_start(command:Command):
    try:
        open_app(command)
        return {"status": "ok"}
    except ValueError as e:
        raise ValueError(f"Failed to open app {command.name}.")