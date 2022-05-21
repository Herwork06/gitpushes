import git 
import os

print("Gitpushes\n{0}".format('='*100))

print("\nGetting Git Repo\n{0}".format('='*100))

repo_dir = os.path.dirname(os.path.abspath(__file__))

print(repo_dir)

repo = git.Repo(repo_dir)
r = git.Repo.init(repo_dir)

repo.git.add(all=True)



print("\nAdded files\n{0}".format('='*100))

r.index.commit("initial commit")
