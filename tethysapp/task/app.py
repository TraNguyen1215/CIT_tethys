from tethys_sdk.base import TethysAppBase # type: ignore


class Task(TethysAppBase):
    """
    Tethys app class for Task.
    """

    name = 'Task'
    description = ''
    package = 'task'  # WARNING: Do not change this value
    index = 'home'
    icon = f'{package}/images/icon.gif'
    root_url = 'task'
    color = '#192a56'
    tags = ''
    enable_feedback = False
    feedback_emails = []