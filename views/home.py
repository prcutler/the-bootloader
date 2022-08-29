import fastapi
from fastapi_chameleon import template
from starlette import status
from starlette.requests import Request

from viewmodels.home.indexviewmodel import IndexViewModel

router = fastapi.APIRouter()


@router.get("/")
@template()
async def index(request: Request):
    vm = IndexViewModel(request)
    await vm.load()
    return vm.to_dict()


@router.get("/about")
@template(template_file="home/about.pt")
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/support")
@template(template_file="home/support.pt")
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


