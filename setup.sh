# This sets default values for the versions of the Python
# libraries we are installing. If we wish to override this
# (say, during VM or container setup), we do so by
# exporting these variables into the shell environment before
# sourcing this script. If these variables exist before this
# script is sourced, then the pre-existing values will be used.

# Check for virtualenv
command -v virtualenv >/dev/null 2>&1 || { 
  echo >&2 "I require 'virtualenv' but it's not installed.  Aborting."; 
  exit 1;
 }

 # Check for pip
command -v pip >/dev/null 2>&1 || { 
 echo >&2 "I require 'pip' but it's not installed.  Aborting."; 
 exit 1;
}


# If there is a virtual environment, destroy it.
if [ -d venv ]; then
  echo "Deactivating and removing old virtualenv"
  deactivate 2>&1 /dev/null
  rm -rf venv
fi

# Create and activate a clean virtual environment.
virtualenv venv
. venv/bin/activate

# Create a data directory
# We will want this if it is a new project.
mkdir -p data

# Upgrade pip before continuing; avoids warnings.
# This should not affect application behavior.
pip install --upgrade pip

# Install specific versions of libraries to avoid
# different behaviors of applications over time.

pip install -U "Flask"
# http://flask.pocoo.org/

pip install -U "peewee"
# http://docs.peewee-orm.com/en/latest/

pip install -U "pyyaml"
# http://pyyaml.org/

pip install -U "flask_peewee"
# http://docs.peewee-orm.com/projects/flask-peewee/en/latest/

pip install -U "flask_security"
# https://pythonhosted.org/Flask-Security/

pip install -U "flask_admin"
# https://flask-admin.readthedocs.io/en/latest/

pip install -U "hurry.filesize"
# https://flask-admin.readthedocs.io/en/latest/

pip install -U "mtgsdk"
# https://github.com/MagicTheGathering/mtg-sdk-python