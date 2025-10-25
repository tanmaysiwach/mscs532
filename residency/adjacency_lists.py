import time 
import pandas as pd

df = pd.read_csv("follows_data.csv", dtype=str)
adjacency_list = {}
for _, row in df.iterrows():    
    follower = row['follower_id']
    followed = row['followed_id']
    if follower not in adjacency_list:
        adjacency_list[follower] = []
    adjacency_list[follower].append(followed)

for key, value in adjacency_list.items():
    print(f"{key}: {value}")
    break

start_time = time.time()
print("Who A follows:", adjacency_list.get('A', []))
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
start_time = time.time()
print("Who follows A:" , [k for k, v in adjacency_list.items() if 'A' in v])
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
start_time = time.time()
mutuals = [user for user in adjacency_list.get('A', []) if 'A' in adjacency_list.get(user, [])]
print("Mutual follows with A:", mutuals)
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
start_time = time.time()
a_one_way = [user for user in adjacency_list.get('A', []) if 'A' not in adjacency_list.get(user, [])]
print("A follows but not followed back:", a_one_way)
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
start_time = time.time()
follows_a_only = [k for k, v in adjacency_list.items() if 'A' in v and k not in adjacency_list.get('A', [])]
print("Follows A but not followed back:", follows_a_only)
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")