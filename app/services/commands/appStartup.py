import subprocess
from ...schemas.commands import Command
from logging import getLogger

logger = getLogger(__name__)

mapper = {
    "chrome": "chrome.exe",
    "discord": "discord.exe"
}
    
def get_os():
    import platform
    
    logger.info(f"Detected OS: {platform.system()}")
    
    return platform.system()

def os_commands():
    """ Return a dictionary of commands to open apps based on the OS."""
    apps = {
        "chrome": "",
        "discord": "",
    }

    os = get_os()

    if os == "Windows":
        for app_name in apps:
            apps[app_name] = f"start {app_name}"

    elif os == "Linux":
        for app_name in apps:
            apps[app_name] = app_name

    elif os == "Darwin":  
        for app_name in apps:
            apps[app_name] = f"open -a {app_name}"

    else:
        raise NotImplementedError(
            f"OS {os} is not supported yet."
        )

    return apps


def is_running(app_name: str) -> bool:
    """ Check if an app is already running based on the command provided."""
    import psutil

    process_name = mapper.get(app_name)

    logger.info("Looking for process: %s", process_name)
    

    for proc in psutil.process_iter(["name"]):
        print(proc.info["name"])
        try:
            name = proc.info["name"]
            logger.info("Found process: %s", name)

            if name.lower() == process_name.lower():
                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return False

def open_app(command:Command):
    """ Open an app based on the command provided."""
    
    apps = os_commands()
    
    if not command.name:
        raise ValueError(f"Missing app name in command: {command}")
    if command.name not in apps:
        raise ValueError(f"App {command.name} is not supported yet.")
    
    if is_running(command.name):
        logger.info(f"App {command.name} is already running.")
        raise ValueError(f"App {command.name} is already running.")
    
    subprocess.run(
        apps[command.name], 
        shell=True
    )
    
    logger.info(f"Opened app {command.name} successfully.")
    