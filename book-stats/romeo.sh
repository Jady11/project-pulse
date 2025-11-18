#!/usr/bin/env bash

# Example: Book Stat's Dashboard
# Step 1: Download the text
echo "Downloading Romeo and Juliet..."
curl -s "https://www.gutenberg.org/cache/epub/1513/pg1513.txt" -o romeo.txt

# Step 2: Run the Python analysis and visualization
python3 analyze_romeo.py
