#!/bin/sh

npm run watch &

export FLASK_APP=main
pushd app
flask run
popd
