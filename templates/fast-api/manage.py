import subprocess

import uvicorn
from dotenv import load_dotenv
from loguru import logger
from typer import Typer

app = Typer()


@app.command()
def runstyle() -> None:
    subprocess.run(["pycodestyle", "./"])


@app.command()
def runtests() -> None:
    subprocess.run(["pytest", "-v"])


@app.command()
def runserver() -> None:
    logger.info("Server has been started")
    uvicorn.run('app.main:api',
                host=ApiConfig.host,
                port=ApiConfig.port,
                reload=True,
                reload_delay=1)


if __name__ == '__main__':
    load_dotenv()
    from config import ApiConfig, LoggerConfig
    logger.add(f"log/{ApiConfig.title}.log",
               backtrace=True,
               diagnose=True,
               level=LoggerConfig.level,
               rotation="1 week",
               compression="zip")
    app()
