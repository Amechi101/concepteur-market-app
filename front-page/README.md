`requirements.txt`, along with virtualenv and pip, ensure that everything uses the same Python setup.


To use, first install pip and virtualenv using the following shell commands:

`sudo easy_install pip`
pip is a Python package manager, more up-to-date than easy_install.

`sudo pip install virtualenv`
virtualenv creates isolated Python environments, separate from your system's default installation.


Then, create a virtual environment:

`virtualenv ENV`
This creates a new virtual environment in the current working directory called ENV.

`source ENV/bin/activate`
Self-explanitory. `deactivate` (no `source` required) returns you to your normal Python installation.

`pip install -r front-page/requirements.txt`
This automatically installs all required Python modules, as listed in `front-page/requirements.txt`.


After that, your Python environment is ready!
