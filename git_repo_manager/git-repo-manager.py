# -*- coding: utf-8 -*-
from git_repo_manager import __version__ as Version
from git_repo_manager.classes import GitoriousRepository 
from optparse import OptionParser

import os
import sys

def validate(options):
    if not os.path.isdir(options.frm):
        print("{0} is not a dir.").format(options.frm)
        sys.exit(2)

    if not os.path.isdir(options.to):
        print("{0} is not a dir.").format(options.to)
        sys.exit(2)

    if not options.name:
        print("use -n to give your repo a name!")
        sys.exit(2)

    if not options.remote_url:
        print("use -u to provide remote url!")
        sys.exit(2)

    if options.extract_repo:
        if not options.frm or not options.to:
            print("usage: git-repo-manager.py -x -f /path/to/old/app -t /path/to/new/repo")
            sys.exit(2)

def main(argv):
    parser = OptionParser(version=Version)

    parser.add_option("-c", "--create-repo", dest="create_repo",
                      help="Task to create a new remote repo",
                      action="store_true")

    parser.add_option("-n", "--repo-name", dest="name",
                      help="Give your repo a name!",
                      metavar="NAME")

    parser.add_option("-f", "--from", dest="frm",
                      help="Path to migrate repo from",
                      metavar="FROM")

    parser.add_option("-t", "--to", dest="to",
                      help="Path do generate new repo",
                      metavar="TO")
    
    parser.add_option("-u", "--remote-url", dest="remote_url",
                      help="Remote URL",
                      metavar="URL")

    parser.add_option("-x", "--extract-repo", dest="extract_repo",
                      help="Task to extract a module and create a new repo",
                      action="store_true")
    
    (options, args) = parser.parse_args()
    
    validate(options)
    
    if options.extract_repo:
        #criar um factory para isso
        repo = GitoriousRepository(name=options.name)
        repo.remote_url = options.remote_url
        
        author = raw_input("Author: ")
        email = raw_input("Author email: ")
        version = raw_input("Version: ")
        description = raw_input("Short description: ")
        long_description = raw_input("Long description: ")
        keywords = raw_input("Keywords (comma separated): ")

        repo.description = description
        repo.long_description = long_description
        repo.keywords = keywords
        repo.author = author
        repo.email = email
        repo.version = version
        
        repo.extract_repo(frm=options.frm, to=options.to)

        ans = raw_input("Remove old files at {0}? [y] [n] ".format(options.frm))
        if ans == 'n' or ans == 'N':
            print("Old files not removed.")
            sys.exit(0)
        elif ans == 'y' or ans == 'Y':
            print("Removing files...'")

if __name__ == "__main__":
    main(sys.argv[1:])
