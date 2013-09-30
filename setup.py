# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from git_repo_manager import __version__ as Version

setup(
    name=u'git-repo-manager',
    version=Version,
    description=u"A simple library that helps you manage your git repos",
    long_description=u'''
    git_repo_manager allows users to create new git repositories based on a well defined template.

    Repositories can be managed directly via git-repo-manager.py script or by developer himself. In this last case, developer just have to import simple_manage as a python module.

    It also create a Jenkins Job for this new born repo.
    ''',
    keywords='git gitorius github manager repo repository repositories',
    author=u'Victor Pantoja',
    author_email='victor.pantoja@gmail.com',
    url='https://github.com/victorpantoja/git-repo-manager',
    license='MIT',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python'],
    packages=find_packages(),
    package_dir={"git_repo_manager": "git_repo_manager"},
    include_package_data=True,
    scripts=['git_repo_manager/git-repo-manager.py'],

    install_requires=[
        "simple-dependencies-manager==0.5.0",
        "python-jenkins==0.2.1"
    ]
)
