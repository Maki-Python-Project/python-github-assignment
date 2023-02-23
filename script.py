from github import Github

from service import get_all_pull_requests


git = Github()

repo = git.get_repo("opencv/opencv")


if __name__ == "__main__":
    print(get_all_pull_requests(repo))
