# Flask

---

# Python installed?

```sh
# python --version
Python 3.7.3
```

🎉🥳

# Ok lets go 🎬

# new git repo 📜

```sh
git init myapp
wget -O .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
```

# virutalenv 📦

```sh
python -m venv env

# enable
. env/bin/activate

# disable
deactivate
```

# setup.py

```python
#!/usr/bin/env python
import setuptools
setuptools.setup()
```

# setup.cfg

```ini
[metadata]
name = myapp
author = foosinn
version = 0.1.0
license = Apache 2.0
long_description = file: README.md
requires-python = >=3.6

[options]
include_package_data = True
packages = find:
install_requires =
  flask

```

# install ⏩

```
pip install -e .
```

# workshop

live coding

# cool python stuff

* generators
* decorators
* with statements

# readups

* Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* Flasks Docs: https://flask.palletsprojects.com/en/1.1.x/
* Pythons Docs: https://docs.python.org/3/
