import subprocess
import threading

from logging import getLogger
from ...schemas.commands import CommandReq
from app.services.helper import get_os
from .factory import CommandFactory

logger = getLogger(__name__)
factory = CommandFactory(get_os())

shutdown_timer: threading.Timer | None = None


def sys_shutdown(req: CommandReq):
    global shutdown_timer
    action = req.name

    if not action:
        raise ValueError("Missing command in request")

    cmd = factory.get_system_command(action)
    logger.info("System is shutting down")

    shutdown_timer = threading.Timer(5.0, lambda: subprocess.run(cmd, shell=True))

    try:
        shutdown_timer.start()
    except RuntimeError as e:
        raise RuntimeError(f"Issue shutting down system ({cmd}): {e}") from e


def sys_sleep(req: CommandReq):
    action = req.name

    if not action:
        raise ValueError("Missing command in request")

    cmd = factory.get_system_command(action)
    logger.info("Sleep starting")

    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Sleep command '{cmd}' did not work: {e}") from e