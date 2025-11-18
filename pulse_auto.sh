#!/usr/bin/env bash

# Example cron entry
# 0 * * * * /usr/bin/bash /path/to/pulse_auto.sh

for i in {1..3}; do
    echo "[$(date)] Pulse Check" >> pulse_history.log
    echo "Commits: $(git log --oneline | wc -l)" >> pulse_history.log
    echo "Files Tracked: $(git ls-files | wc -l)" >> pulse_history.log
    echo "----" >> pulse_history.log
    sleep 10
done
