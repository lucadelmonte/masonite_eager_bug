**Masoniteorm issue #777 (https://github.com/MasoniteFramework/orm/issues/777) POC**

run.sh results

    ./run.sh                                                                    
    (• _ •)Executing migrations...(• _ •)
    Nothing To Migrate!
    (• _ •)Executing query with eager loading...(• _ •)
    (• _ •)Executing query without eager loading... (• _ •)
    (• _ •)Comparing queries...(• _ •)
    Number of SELECT with eager loading: 12
    Number of SELECT without eager loading: 11
    (• _ •)diff between queries:
    12d11
    < Running query SELECT * FROM "address" WHERE "address"."user_id" IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Executed in 0.00ms
    (• _ •)Queries executed with eager loading:
    Running query SELECT * FROM "user", []. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [1]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [2]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [3]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [4]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [5]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [6]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [7]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [8]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [9]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" = ? LIMIT 1, [10]. Executed in 0.00ms
    Running query SELECT * FROM "address" WHERE "address"."user_id" IN (?, ?, ?, ?, ?, ?, ?, ?, ?, ?), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Executed in 0.00ms
