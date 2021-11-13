#!/bin/bash

problems=$(ls -l | grep "^d" | wc -l)
echo "Total number of problems: ${problems}"
python=$(find ./ -name "*.py" | wc -l)
echo "Python: ${python}"
java=$(find ./ -name "*.java" | wc -l)
echo "Java: ${java}"
go=$(find ./ -name "*.go" | wc -l)
echo "Go: ${go}"
cpp=$(find ./ -name "*.cpp" | wc -l)
echo "C++: ${cpp}"
javascript=$(find ./ -name "*.js" | wc -l)
echo "Javascript: ${javascript}"
ruby=$(find ./ -name "*.rb" | wc -l)
echo "Ruby: ${ruby}"
sql=$(find ./ -name "*sql" | wc -l)
echo "SQL: ${sql}"
