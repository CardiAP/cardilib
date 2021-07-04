CardiAP
=======

Copyright © `2020-2021 ` `Velez Rueda, Garcia Smith, Sommese`

> Python library for performing biomedical images analysis. Cardilib allows users to easily work with images confocal microscopy, and obtain representative amplitude and kinetics data.


# Installation

```bash
# Create and active a virtual env
$ python3 -m venv .venv
$ source .venv/bin/activate
# install the project
$ pip install -e .
```

# Running tests

```bash
# install tox
$ pip install tox
# execute tox
$ tox
```


# Publishing project

```bash
# update package version in setup.cfg
# them run these command:
$ git tag <version>
$ git push origin HEAD --tags
# build the package
$ tox -e build
# publish to test.pypi
$ tox -e publish 
# publish to pypi
$ tox -e --publish -- --repository pypi
```


# Using cardilib on line

You can find a web server for using cardilib hosted in Binder. You can launch [CardiAP here](http://cardiap.herokuapp.com/)