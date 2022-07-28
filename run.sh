#!/bin/bash

echo "(• _ •)Executing migrations...(• _ •)"
masonite-orm migrate --no-interaction --directory migrations --force

echo  "(• _ •)Executing query with eager loading...(• _ •)"
python3.10 main.py eager > /tmp/queries_eager.log
echo  "(• _ •)Executing query without eager loading... (• _ •)"
python3.10 main.py > /tmp/queries.log

echo "(• _ •)Comparing queries...(• _ •)"
echo "Number of SELECT with eager loading: $(wc -l < /tmp/queries_eager.log)"
echo "Number of SELECT without eager loading: $(wc -l < /tmp/queries.log)"

echo "(• _ •)diff between queries:"
diff /tmp/queries_eager.log /tmp/queries.log

echo "(• _ •)Queries executed with eager loading:"
cat /tmp/queries_eager.log
