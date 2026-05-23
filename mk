#!/opt/local/bin/bash

set -e

pushd ../yagui
npm install
webpack

popd
npm install
webpack

#     "yagui": "git+https://github.com/mvaranda/yagui.git#mv-images",

