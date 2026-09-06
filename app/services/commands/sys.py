import subprocess
import threading

from logging import getLogger
from ...schemas.commands import CommandReq
from app.services.helpers import _OS
from .factory import CommandFactory

logger = getLogger(__name__)
factory = CommandFactory(_OS)

def sys_command(req: CommandReq):
    action = req.name.strip().lower()

    if not action:
        raise ValueError("Missing command in request")
    
    if action == "shutdown":
        
        global shutdown_timer
        shutdown_timer = threading.Timer(5.0, lambda: subprocess.run(factory.get_system_command("shutdown"), shell=True))
        
        try:
            shutdown_timer.start()
        except RuntimeError as e:
            raise RuntimeError(f"Issue shutting down system ({factory.get_system_command('shutdown')}): {e}") from e
        
    if action == "sleep":
        global sleep_timer
        sleep_timer = threading.Timer(5.0, lambda: subprocess.run(factory.get_system_command("sleep"), shell=True))
        
        try:
            sleep_timer.start()
        except RuntimeError as e:
            raise RuntimeError(f"Issue putting system to sleep ({factory.get_system_command('sleep')}): {e}") from e

    cmd = factory.get_system_command(action)

    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"System command '{cmd}' did not work: {e}") from e
