Whenever starting a new project, do this:
1) Make a copy of skeleton directory. Name it after new project.
2) Rename (move) the NAME module to be the name of the new project's root module.
3) Edit `setup.py` to have all information for the new project.
4) Rename `tests/NAME_tests.py` to also have the new root module name.
5) Double check it is all working by running `nosetests` in the project's directory.
6) Start having fun!

P.S:
1) Use `sudo python setup.py install` to install the module.
2) Use `sudo pip unintall `module`` to uninstall the module.

For scripts:
1) include `#!/usr/bin/env python` at top of script file.
2) Script file goes in `bin` directory.
3) Use `chmod +x <script>.py` to change permissions so it's executable.
4) Add script patch to `setup.py` to have it insall.
