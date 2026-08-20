from logging import getLogger

logger = getLogger(__name__)

def get_os() -> str:
    import platform

    logger.info(f"Detected OS: {platform.system()}")

    return platform.system()
