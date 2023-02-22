from github import Github


git = Github()

repo = git.get_repo("Maki-Python-Project/url-shortner-api")
print(repo.subscribers_count)
