import fastapi
from fastapi_chameleon import template
import fastapi_chameleon
from starlette import status
from starlette.requests import Request

from services import episode_service

#from viewmodels.episodes.all_episodes_list_viewmodel import AllEpisodesViewModel
#from viewmodels.episodes.episode_details_viewmodel import EpisodeDetailsViewModel
#from viewmodels.episodes.transcripts_viewmodel import TranscriptsViewModel

#from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


#### SHOW ALL EPISODES ####
@router.get("/episodes/all")
@template(template_file="episodes/all.pt")
async def all(request: Request):
    vm = AllEpisodesViewModel(request)
    await vm.load()

    return vm.to_dict()


#### EPISODE DETAIL TEMPLATE ####
@router.get("/episodes/{episode_number}")
@template(template_file="episodes/episode-detail.pt")
async def details(episode_number, request: Request):

    vm = EpisodeDetailsViewModel(episode_number, request)

    await vm.load(episode_number)

    if vm.episode_info is None:
        fastapi_chameleon.not_found()

    return vm.to_dict()


#### TRANSCRIPTS ####
@router.get("/episodes/{episode_number}/transcripts")
@template(template_file="episodes/transcripts/transcripts.pt")
async def transcripts(episode_number, request: Request):
    vm = TranscriptsViewModel(episode_number, request)
    await vm.load(episode_number)

    return vm.to_dict()


#### TEMP FILES UNTIL DONE ####
@router.get("/episodes/0/trailer")
@template(template_file="episodes/episode0-trailer.pt")
def all():
    return {}


@router.get("/episodes/0/transcripts/episode0-transcript")
@template(template_file="episodes/transcripts/episode0-transcript.pt")
def all():
    return {}
