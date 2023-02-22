import datetime

from typing import List
from github import Repository


def get_open_time(created_at: datetime) -> str:
    now = datetime.datetime.now()
    open_time = now - created_at

    return f"{open_time.days} days {open_time.seconds} seconds {open_time.microseconds} microseconds"


def get_all_pull_requests(repo: Repository) -> List[str]:
    all_pull_requests = []

    for pull in repo.get_pulls():
        all_pull_requests.append(
            (
                pull.number,
                pull.title,
                str(pull.created_at),
                get_open_time(pull.created_at),
                pull.user.login,
            )
        )

    return all_pull_requests
