#!/bin/bash

cd `dirname $0`
source config.sh
python3 test.py "$SACLOUD_TOKEN" "$SACLOUD_SECRET"
