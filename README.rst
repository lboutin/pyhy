====
pyhy
====


Add a short description here!


Description
===========

A longer description of your project goes here...

Step 0) activate conda environment "fews"
Step 1) create your project using PyScaffold like this: >\:  putup "My_Project" -u "GitHub URL"
Step 2) within the folder that was created, install the project: >\: python setup.py install
Step 3) test unittest: >\: python setup.py test
Step 4) deploy for development: >\: python setup.py develop
Step 5) deploy for distribution: >\: python setup.py bdist_wheel

In the python console>

from pyhy.base import hydrograph as hg
MyClass = hg(123.7777)
result = MyClass.run()

Alternatively, if used from command prompt, in the same directorry as the python file:

python base.py --help
python base.py --input 123.8888
or
python base.py


Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
