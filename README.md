git-repo-manager
================

A manager to administrate git repositories.

git_repo_manager allows users to create new git repositories based on a well defined template.

Repositories can be managed directly via git-repo-manager.py script or by developer himself. In this last case, developer just have to import simple_manage as a python module.

It also create a Jenkins Job for this new born repo.

With git-repo-manager, you can easily create a new project automatically at github and gitorius and, also, have it ready to test at Jenkins or to distribute in pypi.

Available commands:
-------------------
1. Extract code from some old project and create a new repository

    python git-repo-manager.py -x -f ~/path/to/current/project -t ~/path/to/workspace -n <project-name> -u <remote_url>
  
