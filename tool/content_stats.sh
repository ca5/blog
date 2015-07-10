#!/bin/bash
echo "+++ categories +++"
grep Category:  content/*md| awk -F: '{print $3}' | sort | uniq -c
echo ""
echo "+++ tags +++"
grep Tags: content/*md | awk -F'[: ,]' '{for(i=4;i<=NF;i++){print $i}}' | grep -v '^$'| sort | uniq -c | sort -nr | xargs -L 1 -I% echo -n %"	"
