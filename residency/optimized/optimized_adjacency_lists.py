import time
import pandas as pd
from collections import defaultdict

# ============================================================
# Load and build both adjacency maps
# ============================================================
df = pd.read_csv("follows_data_scaled.csv", dtype=str)
print("Loaded dataframe with", len(df), "rows.")
df = df.head(10000000)

follows_map = defaultdict(list)
followers_map = defaultdict(list)

start_build = time.time()
for follower, followed in zip(df['follower_id'], df['followed_id']):
    follows_map[follower].append(followed)
    followers_map[followed].append(follower)
end_build = time.time()
print(f"Built dual adjacency maps in {end_build - start_build:.2f}s")

# ============================================================
# Optimized queries
# ============================================================
user = 'A'

start = time.time()
who_a_follows = follows_map.get(user, [])
print("Who A follows:")
print(f"Query time: {time.time() - start:.6f}s")

start = time.time()
who_follows_a = followers_map.get(user, [])
print("Who follows A:")
print(f"Query time: {time.time() - start:.6f}s")

start = time.time()
mutuals = [u for u in who_a_follows if user in follows_map.get(u, [])]
print("Mutual follows with A:")
print(f"Query time: {time.time() - start:.6f}s")

start = time.time()
a_one_way = [u for u in who_a_follows if user not in follows_map.get(u, [])]
print("A follows but not followed back:")
print(f"Query time: {time.time() - start:.6f}s")

start = time.time()
follows_a_only = [u for u in who_follows_a if u not in who_a_follows]
print("Follows A but not followed back:")
print(f"Query time: {time.time() - start:.6f}s")
