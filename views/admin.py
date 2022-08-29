import fastapi
from fastapi_chameleon import template
from starlette import status
from starlette.requests import Request

from services import episode_service
from services import transcripts_service
from services import shownotes_service

from viewmodels.shared.viewmodel import ViewModelBase
from viewmodels.admin.admin_viewmodel import AdminViewModel

from viewmodels.admin.add_episode import EpisodeAddViewModel
from viewmodels.admin.add_show_notes_viewmodel import ShowNotesAddViewModel

from viewmodels.admin.edit_episode_viewmodel import EditEpisodeViewModel
from viewmodels.admin.edit_show_notes_viewmodel import EditShowNotesViewModel

router = fastapi.APIRouter()


# ##########  ADMIN HOMEPAGE ##############
# ### GET EPISODE LIST TO DISPLAY FOR EDIT ####
@router.get("/admin/index")
@template(template_file="admin/index.pt")
async def index(request: Request):
    vm = AdminViewModel(request)

    await vm.load()

    if vm.login_status is False:
        response = fastapi.responses.RedirectResponse(
            url="/", status_code=status.HTTP_302_FOUND
        )
        return response
    else:
        return vm.to_dict()


@router.post("/admin/index", include_in_schema=False)
@template()
async def edit_post(request: Request):
    vm = AdminViewModel(request)
    await vm.load()

    episode_number = vm.episode_number

    # Redirect to Admin homepage on post
    response = fastapi.responses.RedirectResponse(
        url=f"/admin/edit-episode/{episode_number}", status_code=status.HTTP_302_FOUND
    )

    return response


# ##########  ADD EPISODE ##############
@router.get("/admin/add-episode", include_in_schema=False)
@template(template_file="admin/add-episode.pt")
def register(request: Request):
    vm = EpisodeAddViewModel(request)

    if vm.login_status is False:
        response = fastapi.responses.RedirectResponse(
            url="/", status_code=status.HTTP_302_FOUND
        )
        return response
    else:
        return vm.to_dict()


@router.post("/admin/add-episode", include_in_schema=False)
@template()
async def register(request: Request):
    vm = EpisodeAddViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    # Add the episode
    episode = await episode_service.create_episode(
        vm.season,
        vm.episode_number,
        vm.episode_title,
        vm.youtube_url,
        vm.guest_firstname,
        vm.guest_lastname,
        vm.topic,
        vm.record_date,
        vm.record_date_converted,
        vm.publish_date,
        vm.publish_date_converted,
        vm.guest_image,
        vm.guest_bio_1,
        vm.guest_bio_2,
        vm.sponsor_1,
        vm.sponsor_2,
        vm.published,
        vm.episode_length,
        vm.episode_length_string,
        vm.captivate_url,
    )

    # Redirect to the episode page
    response = fastapi.responses.RedirectResponse(
        url="/admin/add-show-notes", status_code=status.HTTP_302_FOUND
    )

    return response


# ### EDIT EPISODE DETAIL TEMPLATE ####
@router.get("/admin/edit-episode/{episode_number}")
@template(template_file="admin/edit-episode.pt")
async def edit_details(episode_number, request: Request):
    vm = EditEpisodeViewModel(episode_number, request)
    await vm.load()

    if vm.login_status is False:
        response = fastapi.responses.RedirectResponse(
            url="/", status_code=status.HTTP_302_FOUND
        )
        return response
    else:
        episode_number = vm.episode_number
        return vm.to_dict()


@router.post("/admin/edit-episode/{episode_number}", include_in_schema=False)
@template()
async def edit_episode_post(episode_number, request: Request):
    vm = EditEpisodeViewModel(episode_number, request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    # Edit the episode
    episode = await episode_service.edit_episode(
        vm.season,
        vm.episode_number,
        vm.episode_title,
        vm.youtube_url,
        vm.guest_firstname,
        vm.guest_lastname,
        vm.topic,
        vm.record_date,
        vm.record_date_converted,
        vm.publish_date,
        vm.publish_date_converted,
        vm.guest_image,
        vm.guest_bio_1,
        vm.guest_bio_2,
        vm.sponsor_1,
        vm.sponsor_2,
        vm.published,
        vm.episode_length,
        vm.episode_length_string,
        vm.captivate_url,
    )

    # Redirect to the admin page
    response = fastapi.responses.RedirectResponse(
        url="/admin/index", status_code=status.HTTP_302_FOUND
    )

    return response


# ##########  ADD SHOWNOTES ##############
@router.get("/admin/add-show-notes", include_in_schema=False)
@template("admin/add-show-notes.pt")
def add_show_notes(request: Request):
    vm = ShowNotesAddViewModel(request)

    if vm.login_status is False:
        response = fastapi.responses.RedirectResponse(
            url="/", status_code=status.HTTP_302_FOUND
        )

        return response

    else:
        return vm.to_dict()


@router.post("/admin/add-show-notes", include_in_schema=False)
@template("admin/add-show-notes.pt")
async def add_show_notes(request: Request):
    vm = ShowNotesAddViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    # Add the show notes
    show_notes = await shownotes_service.create_show_notes(
        vm.season,
        vm.episode,
        vm.published,
        vm.timestamp_1,
        vm.notes_1,
        vm.link_1,
        vm.link_text_1,
        vm.timestamp_2,
        vm.notes_2,
        vm.link_2,
        vm.link_text_2,
        vm.timestamp_3,
        vm.notes_3,
        vm.link_3,
        vm.link_text_3,
        vm.timestamp_4,
        vm.notes_4,
        vm.link_4,
        vm.link_text_4,
        vm.timestamp_5,
        vm.notes_5,
        vm.link_5,
        vm.link_text_5,
        vm.timestamp_6,
        vm.notes_6,
        vm.link_6,
        vm.link_text_6,
        vm.timestamp_7,
        vm.notes_7,
        vm.link_7,
        vm.link_text_7,
        vm.timestamp_8,
        vm.notes_8,
        vm.link_8,
        vm.link_text_8,
        vm.timestamp_9,
        vm.notes_9,
        vm.link_9,
        vm.link_text_9,
        vm.timestamp_10,
        vm.notes_10,
        vm.link_10,
        vm.link_text_10,
    )

    # Redirect to the admin page
    response = fastapi.responses.RedirectResponse(
        url="/admin/index", status_code=status.HTTP_302_FOUND
    )

    return response


# ### EDIT SHOW NOTES ####
@router.get("/admin/edit-shownotes/{episode_number}")
@template(template_file="admin/edit-shownotes.pt")
async def edit_show_notes_get(episode_number, request: Request):
    vm = EditShowNotesViewModel(episode_number, request)
    await vm.load()

    if vm.login_status is False:
        response = fastapi.responses.RedirectResponse(
            url="/", status_code=status.HTTP_302_FOUND
        )
        return response
    else:
        episode_number = vm.episode_number
        return vm.to_dict()


@router.post("/admin/edit-shownotes/{episode_number}", include_in_schema=False)
@template("admin/edit-shownotes.pt{episode_number}")
async def edit_show_notes_post(episode_number, request: Request):
    vm = EditShowNotesViewModel(episode_number, request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    # Edit the show notes
    show_notes = await shownotes_service.edit_show_notes(
        vm.season,
        vm.episode_number,
        vm.timestamp_1,
        vm.notes_1,
        vm.link_1,
        vm.link_text_1,
        vm.timestamp_2,
        vm.notes_2,
        vm.link_2,
        vm.link_text_2,
        vm.timestamp_3,
        vm.notes_3,
        vm.link_3,
        vm.link_text_3,
        vm.timestamp_4,
        vm.notes_4,
        vm.link_4,
        vm.link_text_4,
        vm.timestamp_5,
        vm.notes_5,
        vm.link_5,
        vm.link_text_5,
        vm.timestamp_6,
        vm.notes_6,
        vm.link_6,
        vm.link_text_6,
        vm.timestamp_7,
        vm.notes_7,
        vm.link_7,
        vm.link_text_7,
        vm.timestamp_8,
        vm.notes_8,
        vm.link_8,
        vm.link_text_8,
        vm.timestamp_9,
        vm.notes_9,
        vm.link_9,
        vm.link_text_9,
        vm.timestamp_10,
        vm.notes_10,
        vm.link_10,
        vm.link_text_10,
    )

    # Redirect to the admin page
    response = fastapi.responses.RedirectResponse(
        url="/admin/index", status_code=status.HTTP_302_FOUND
    )

    return response




