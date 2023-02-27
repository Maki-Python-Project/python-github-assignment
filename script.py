from github import Github

from service import get_all_pull_requests, print_info_about_pull_requests


git = Github()

repo = git.get_repo("vovalaz/python-github-assignment")


if __name__ == "__main__":
    print_info_about_pull_requests(get_all_pull_requests(repo))
