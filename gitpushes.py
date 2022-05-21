import git 
import os

print("Gitpushes\n{0}".format('='*100))

print("\nGetting Git Repo\n{0}".format('='*100))

repo_dir = "{0}\.git".format(os.path.dirname(os.path.abspath(__file__)))

repo = git.Repo(repo_dir)

try:
    repo.git.add(update=True)
    print("\nAdded {1} files\n{0}".format('='*100, "null"))
except Exception as e:
    print("\nUnable to add all updated files.\n{0}\n{1}".format('='*100, e))

commit_msg = input("\nPlease input your commit message\n{0}\n".format('='*100))


try:
    commit = repo.index.commit(commit_msg)
    print("\nCommited {2} files with msg: {1}\n{0}".format('='*100, commit_msg, commit.stats.total['files']))
except Exception as e:
    print("\nUnable to commit.\n{0}\n{1}".format('='*100, e))

try:
    origin = repo.remote(name="origin")
    push = origin.push()
    print("\nPushed the files to {1}\n{0}".format('='*100, repo.active_branch))

except Exception as e:
    print("\nUnable to push the commit.\n{0}\n{1}".format('='*100, e))

