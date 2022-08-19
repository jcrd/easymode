#!/bin/sh

export EASYMODE_CONFIG=../test/config
export FLASK_APP=main

npm run watch &

pushd app
flask run
popd
