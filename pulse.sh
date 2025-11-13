#!/usr/bin/env bash


git log --oneline | wc -l > pulse.txt
curl -s "http://worldclockapi.com/api/json/utc/now" \
  | sed -n 's/.*"currentDateTime":"\([^"]*\)".*/\1/p' >> pulse.txt
echo "" >> pulse.txt
git ls-files | wc -l >> pulse.txt
cat pulse.txt
echo "✅ Data written to pulse.txt"
