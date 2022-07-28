#!/bin/bash

masonite-orm migrate --no-interaction --directory migrations --force

python3.10 main.py eager > /tmp/queries_eager.log
python3.10 main.py > /tmp/queries.log

wc -l /tmp/queries_eager.log #12
wc -l /tmp/queries.log #11

diff /tmp/queries_eager.log /tmp/queries.log

cat /tmp/queries_eager.log
