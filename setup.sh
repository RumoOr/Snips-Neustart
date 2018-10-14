#!/usr/bin/env bash -e

VENV=venv

if [ ! -d "$VENV" ]
then

    PYTHON=`which python2`

    if [ ! -f $PYTHON ]
    then
        echo "could not find python"
    fi
    virtualenv -p $PYTHON $VENV

fi

. $VENV/bin/activate

cp -r /home/pi/local/Snips-260d0449fd87.json gca.json

echo "Reading config...." >&2
. config.ini
echo "Config for the username: $wolfram_api_key" >&2

pip install -r requirements.txt