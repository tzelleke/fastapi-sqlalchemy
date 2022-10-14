from fastapi import (
    FastAPI,
    Request,
)
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api import router as api_router
from app.core.config import (
    API_VERSION,
    DEBUG,
    PROJECT_NAME,
    ROOT_PATH,
)

app = FastAPI(
    root_path=ROOT_PATH, title=f"{PROJECT_NAME} API", version=API_VERSION, debug=DEBUG,
)
app.include_router(api_router, prefix=f"/api")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(*, request: Request):
    return templates.TemplateResponse("index.html", {
        'request': request,
        'name': 'Friends',
    })
