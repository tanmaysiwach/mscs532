import pandas as pd
import networkx as nx
import time
import matplotlib.pyplot as plt

df = pd.read_csv("follows_data.csv", dtype=str)
G = nx.from_pandas_edgelist(df, source='follower_id', target='followed_id', create_using=nx.DiGraph())

def who_person_follows(G, person):
    """Return list of users that 'person' follows."""
    return list(G.successors(person))

def who_follows_person(G, person):
    """Return list of users that follow 'person'."""
    return list(G.predecessors(person))

def mutual_follows(G, person):
    """Return list of users who both follow and are followed by 'person'."""
    return list(set(G.successors(person)) & set(G.predecessors(person)))

def follows_but_not_followed_back(G, person):
    """Return list of users that 'person' follows but who don't follow back."""
    return list(set(G.successors(person)) - set(G.predecessors(person)))

def followed_but_not_following_back(G, person):
    """Return list of users who follow 'person' but are not followed back."""
    return list(set(G.predecessors(person)) - set(G.successors(person)))

person = 'A' 
plt.figure(figsize=(1, 1))
df_snippet = df.head(500)
g_snippet = nx.from_pandas_edgelist(df_snippet, source='follower_id', target='followed_id', create_using=nx.DiGraph())
nx.draw_networkx(g_snippet, with_labels=True, node_color='lightblue', arrows=True)
plt.title("Social Network Graph")
plt.show()

print(f"\n--- NetworkX Graph Analysis for {person} ---")

start_time = time.time()
print("1️⃣ Who", person, "follows:", who_person_follows(G, person))
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
start_time = time.time()
print("2️⃣ Who follows", person + ":", who_follows_person(G, person))
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
start_time = time.time()
print("3️⃣ Mutual follows:", mutual_follows(G, person))
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
start_time = time.time()
print("4️⃣ Follows but not followed back:", follows_but_not_followed_back(G, person))
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
start_time = time.time()
print("5️⃣ Followed by but doesn’t follow back:", followed_but_not_following_back(G, person))
end_time = time.time()
print(f"Query time: {end_time - start_time:.6f}s")
