'''
This file sets up the virtual environment. 
Run "source setup.sh" each time you want to run the app. 
'''

mkdir -p data

if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

sudo pip install Flask  --upgrade
sudo pip install peewee --upgrade
sudo pip install pyyaml --upgrade