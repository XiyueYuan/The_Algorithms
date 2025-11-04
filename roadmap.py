import pandas as pd
import matplotlib.pyplot as plt

date = {
    'date': ['2025-09-01', '2025-09-15', '2025-10-01', '2025-10-15', '2025-11-01'], 
    'count': [0, 99, 163, 229, 275]
}
df = pd.DataFrame(date)
df['date'] = pd.to_datetime(df['date'])
plt.xkcd()
plt.plot(df["date"], df["count"], marker='o', label="Problems Solved")
plt.title("My Algorithms Journey")
plt.xlabel("Date")
plt.ylabel("Problems Solved")
plt.xticks(rotation=45)
plt.grid(True)
plt.xticks(df["date"])
plt.tight_layout()
plt.show()