import subprocess
import matplotlib.pyplot as plt
files = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
extensions = [f.split('.')[-1] for f in files if '.' in f]
from collections import Counter

ext_counts = Counter(extensions)


# Sample data for now – we’ll customize it next!
labels = ["Commits", "Files"]
values = [1, 1]  # placeholder
file_types = list(ext_counts.keys())
counts = list(ext_counts.values())


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

ax1.bar(labels, values, color="#2563eb")
ax1.set_title("Project Activity")

ax2.pie(counts, labels=file_types, autopct="%1.1f%%",
        colors=["#16a34a", "#3b82f6", "#facc15"])
ax2.set_title("File Type Breakdown")

fig.suptitle("Pulse Dashboard", fontsize=14)
plt.tight_layout()
plt.savefig("pulse_dashboard.png")
print("pulse_dashboard.png created")
