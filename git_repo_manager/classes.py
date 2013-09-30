# -*- coding: utf-8 -*-
from jenkins import Jenkins
from simple_manager.utils import git_add
from simple_manager.utils import git_clone
from simple_manager.utils import git_commit
from simple_manager.utils import git_push_branch
from simple_manager.utils import git_push_tag
from simple_manager.utils import git_tag
from shutil import copytree

import os


class Repository():

    def __init__(self, name, remote_url=None, description=None,
                 long_description=None, keywords=None,
                 author=None, email=None, version=None):
        self.name = name
        self.remote_url = remote_url
        self.description = description
        self.long_description = long_description
        self.keywords = keywords
        self.author = author
        self.email = email
        self.version = version

    def commit_changes(self, workspace):
        git_add(self.name, workspace)
        git_commit(workspace, self.name)
        git_push_branch(workspace, self.name, "master")

    def tag(self, workspace, project, version):
        git_tag(workspace, project, version, "Migration package to a new respository.")
        git_push_tag(workspace, project)

    def extract_repo(self, frm, to):
        import git_repo_manager
        pkg_name = frm.split('/')[-1]
        path = os.path.join(to, self.name, pkg_name)

        git_clone(self.name, self.remote_url, to)

        print("Extracting code from {0} to {1}").format(frm, path)

        copytree(src=frm, dst=path)

        print("Generating necessary files do create a dist")
        print("  ... setup.py")

        with open(os.path.join(git_repo_manager.__path__[0],
                               "templates/setup.py.conf"), 'r') as setup_tmpl:
            content = setup_tmpl.read()

        content = content.replace("$name", self.name)
        content = content.replace("$version", self.version)
        content = content.replace("$description", self.author)
        content = content.replace("$long_description", self.long_description)
        content = content.replace("$keywords", self.keywords)
        content = content.replace("$author", self.author)
        content = content.replace("$email", self.email)
        content = content.replace("$url", self.remote_url)
        content = content.replace("$pkg_dir", pkg_name)

        with open(os.path.join(to, self.name, "setup.py"),
                  'w') as setup_file:
            setup_file.write(content)

        print("  ... README.md")
        with open(os.path.join(git_repo_manager.__path__[0],
                               "templates/README.md.conf"), 'r') as rdm_tmpl:
            content = rdm_tmpl.read()

        content = content.replace("$name", self.name)
        content = content.replace("$description", self.author)

        with open(os.path.join(to, self.name, "README.md"),
                  'w') as rdm_file:
            rdm_file.write(content)

        self.commit_changes(to)
        self.tag(to, self.name, self.version)

    def config_jenkins(self, jenkins_url, jenkins_config_file, job_name):
        ci = Jenkins(url=jenkins_url)

        config = ""
        with open(jenkins_config_file, "r") as config_file:
            config = config_file.read()

        config_file.close()
        ci.create_job(job_name, config)


class GitoriousRepository(Repository):
    pass
