import subprocess
import psutil
from logging import getLogger
from ...schemas.commands import CommandReq
from app.services.helpers import _OS
from .factory import CommandFactory

logger = getLogger(__name__)

factory = CommandFactory(_OS)

def is_running(process_name: str) -> bool:
    for proc in psutil.process_iter(["name"]):
        try:
            name = proc.info["name"]
            if name and name.lower() == process_name.lower():
                logger.info("Found running process: %s", name)
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

def open_app(req: CommandReq):
    """Open an app based on the command provided."""
    app = req.name

    if not app:
        raise ValueError("Missing app name in command")

    process_name = factory.get_process_name(app)
    if is_running(process_name):
        logger.info(f"App {app} is already running.")
        raise ValueError(f"App {app} is already running.")

    cmd = factory.get_app_command(app)   # raises ValueError if app unsupported

    logger.info(f"Opening {app}")

    try:
        subprocess.run(cmd, shell=True)
    except RuntimeError as e:
        raise RuntimeError(f"Issue opening app ({cmd}): {e}") from e

    logger.info(f"Opened app {app} successfully.")