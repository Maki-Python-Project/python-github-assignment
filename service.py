import datetime
import requests

from typing import List
from github import Repository


def get_open_time(created_at: datetime) -> str:
    now = datetime.datetime.now()
    open_time = now - created_at

    return f"{open_time.days} days {open_time.seconds} seconds {open_time.microseconds} microseconds"


def get_commits(commits_url: str) -> List[tuple]:
    commits = []
    response = requests.get(commits_url)

    for commit in response.json():
        commits.append(
            (
                commit["sha"],
                commit["commit"]["committer"]["name"],
                commit["commit"]["author"]["name"],
                commit["commit"]["message"],
            )
        )

    return commits


def get_comments(comments_url: str) -> List[tuple]:
    comments = []
    response = requests.get(comments_url)

    for comment in response.json():
        comments.append(
            (
                comment["user"]["login"],
                comment["created_at"],
                comment["updated_at"],
                comment["updated_at"],
                comment["body"],
            )
        )

    return comments


def get_all_pull_requests(repo: Repository) -> List[tuple]:
    all_pull_requests = []

    for pull in repo.get_pulls():
        requested_reviewers = [
            (
                reviewer.login,
                reviewer.type,
            )
            for reviewer in pull.requested_reviewers
        ]

        all_pull_requests.append(
            (
                pull.number,
                pull.title,
                str(pull.created_at),
                get_open_time(pull.created_at),
                pull.user.login,
                get_commits(pull.commits_url),
                get_comments(pull.comments_url),
                requested_reviewers,
            )
        )

    return all_pull_requests
