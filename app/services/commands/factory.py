import json
import platform
from pathlib import Path
from functools import lru_cache

_commands_dir = Path(__file__).parent.parent.parent/"commands"

@lru_cache(maxsize=3)
def _load_file(os_name: str) -> dict:
    files = {
        "Windows" : "windows.json",
        "Darwin" : "darwin.json",
        "Linux" : "linux.json"
    }

    if os_name not in files:
        raise NotImplementedError (
            f"OS {os_name} not yet supported"
        )

    path = _commands_dir / files[os_name]

    with open (path , "r", encoding="utf-8") as file:
            return json.load(file)

class CommandFactory:
    def __init__(self,os_name:str):
        self.os_name = os_name
        self.file = _load_file(os_name)

    def get_system_command(self,cmd:str) -> str:
        """Get the system command for a given command name."""
        if cmd not in self.file["system"]:
            raise ValueError (f"The Command {cmd} is not found")
        return self.file["system"][cmd]["command"]

    def get_apps(self, app_name:str) -> dict:
        if app_name not in self.file["apps"]:
            raise ValueError (f"The app {app_name} was not found ")
        return self.file["apps"][app_name]

    def get_app_command(self,app_name:str) -> str:
        return self.get_apps(app_name)["command"]

    def get_process_name(self,app_name:str) -> str:
        return self.get_apps(app_name)["process_name"]
