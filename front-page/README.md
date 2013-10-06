### requirements.txt
`requirements.txt`, along with virtualenv and pip, ensure that everything uses the same Python setup.

---

##### To use, first install pip and virtualenv using the following shell commands:

```bash
sudo easy_install pip
```
pip is a Python package manager, the successor to easy_install.


```bash
sudo pip install virtualenv
```
virtualenv creates isolated Python environments, separate from your system's default installation.

---

##### Then, create and activate a virtual environment:

```bash
virtualenv ENV
```

This creates a new virtual environment in the current working directory called ENV.

```bash
source ENV/bin/activate
```

Self-explanitory. `deactivate` (no `source` required) returns you to your normal Python installation.

---

##### Finally, initialize your new virtual environment:
```bash
pip install -r front-page/requirements.txt
```

This automatically installs all required Python modules, as listed in `front-page/requirements.txt`.

---

#### Your Python virtual environment is ready to use!
