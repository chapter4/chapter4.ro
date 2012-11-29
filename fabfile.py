from fabric.api import *


@task
def devel():
    local('jekyll --server --auto --url http://localhost:4000')
