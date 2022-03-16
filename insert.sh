#!/bin/zsh
mysqlsh root@localhost:33060/LibraryDB --import NewBook.json Books jsondata --convertBsonTypes --ignoreRegex --schema=LibraryDB
