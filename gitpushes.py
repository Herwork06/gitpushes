import git 
import os

print("Gitpushes\n{0}".format('='*100))

print("\nGetting Git Repo\n{0}".format('='*100))

repo_dir = os.path.dirname(os.path.abspath(__file__))

print(repo_dir)

repo = git.Repo(repo_dir)

repo.git.add(update=True)



print("\nAdded files\n{0}".format('='*100))

repo.index.commit("first commit")

origin = repo.remote(name="origin")
origin.push

