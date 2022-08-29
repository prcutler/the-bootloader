from pathlib import Path

import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from data import db_session
from views import account, home, episodes, admin

from pydantic import BaseModel

app = fastapi.FastAPI()


def main():
    configure()
    # :uvicorn.run(app, host="127.0.01", port=8000, log_level="info")


def configure():
    configure_templates()
    configure_routes()
    configure_db(dev_mode=True)

    
def  configure_db(dev_mode: bool):
    file = (Path(__file__).parent / 'db' / 'podcast2.sqlite').absolute()
    db_session.global_init(file.as_posix())


def configure_templates():
    fastapi_chameleon.global_init("templates")


def configure_routes():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(episodes.router)
    app.include_router(account.router)
    app.include_router(admin.router)


if __name__ == "__main__":
    main()
    uvicorn.run(app, port=7300, host="127.0.0.1")
else:
    configure()
