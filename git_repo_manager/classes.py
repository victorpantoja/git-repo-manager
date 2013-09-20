# -*- coding: utf-8 -*-
from simple_manager.utils import git_clone
from shutil import copytree

import git_repo_manager
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

    def commit_changes(self):
        print("Commiting changes to {0}").format(self.remote_url)

    def extract_repo(self, frm, to):
        pkg_name = frm.split('/')[-1]
        path = os.path.join(to, self.name, pkg_name)

        git_clone(self.name, self.remote_url, to)

        print("Extracting code from {0} to {1}").format(frm, path)

        copytree(src=frm, dst=path)

        print("Generating necessary files do create a dist")
        print("  ... setup.py")

        with open(os.path.join(git_repo_manager.__path__[0],
                               "templates/README.md.conf"), 'r') as setup_tmpl:
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

        with open(os.path.join(git_repo_manager.__path__[0],
                   "templates/setup.py"), 'w') as setup_file:
            setup_file.write(content)

        print("  ... README.md")
        with open(os.path.join(git_repo_manager.__path__[0],
                               "templates/README.md.conf"), 'r') as rdm_tmpl:
            content = rdm_tmpl.read()

        content = content.replace("$name", self.name)
        content = content.replace("$description", self.author)

        with open(os.path.join(git_repo_manager.__path__[0],
                   "templates/README.md"), 'w') as rdm_file:
            rdm_file.write(content)

        self.commit_changes()


class GitoriousRepository(Repository):
    pass
