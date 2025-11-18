import re
from collections import Counter
import matplotlib.pyplot as plt

# Step 1: Load and clean the text
with open("romeo.txt", encoding="utf-8") as f:
    text = f.read().lower()

# Step 2: Tokenize and count words
words = re.findall(r"\b[a-z']+\b", text)
counts = Counter(words)
common = counts.most_common(10)

# Step 3: Print summary
print("Romeo and Juliet Analysis Complete!")
print(f"Total words: {len(words):,}")
print(f"Unique words: {len(counts):,}\n")
print("Top 10 words:")
for word, count in common:
    print(f"{word:>10} : {count}")

# Step 4: Visualize with Matplotlib
labels, values = zip(*common)
plt.bar(labels, values, color="#2563eb")
plt.title("Top 10 Words in Romeo and Juliet")
plt.ylabel("Frequency")
plt.xlabel("Word")
plt.tight_layout()
plt.savefig("romeo_chart.png")
print("\nChart saved as romeo_chart.png")
