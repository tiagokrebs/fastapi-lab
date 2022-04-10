#!/bin/bash

curl http://localhost:8000/sync &
curl http://localhost:8000/async &

exit 0
