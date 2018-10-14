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

cp /home/pi/local/Snips-260d0449fd87.json . test.json

pip install -r requirements.txt