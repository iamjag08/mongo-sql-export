#!/bin/zsh
docker exec db mongoexport --db LibraryDB --collection Books --out ./Books.json
docker cp db:/Books.json .
mysqlsh root@localhost:33060/LibraryDB --import Books.json Books jsondata --convertBsonTypes --ignoreRegex --schema=LibraryDB
mysql -u root -p LibraryDB<update_table.sql
