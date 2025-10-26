import pandas as pd
import networkx as nx
import time

df = pd.read_csv("follows_data_scaled.csv", dtype=str)
G = nx.from_pandas_edgelist(df, source='follower_id', target='followed_id', create_using=nx.DiGraph())

def who_person_follows(G, person):
    """Return users that 'person' follows."""
    # Directly access adjacency dict for successors (faster than G.successors)
    if person in G._succ:
        return list(G._succ[person].keys())
    return []

def who_follows_person(G, person):
    """Return users that follow 'person'."""
    if person in G._pred:
        return list(G._pred[person].keys())
    return []

def mutual_follows(G, person):
    """Users who both follow and are followed by 'person'."""
    if person not in G._succ or person not in G._pred:
        return []
    following = G._succ[person]
    followers = G._pred[person]
    # Use dictionary key sets for intersection — avoids extra list/set conversion
    return [u for u in following if u in followers]

def follows_but_not_followed_back(G, person):
    """Users that 'person' follows but who don't follow back."""
    if person not in G._succ:
        return []
    following = G._succ[person]
    followers = G._pred.get(person, {})
    return [u for u in following if u not in followers]

def followed_but_not_following_back(G, person):
    """Users who follow 'person' but are not followed back."""
    if person not in G._pred:
        return []
    followers = G._pred[person]
    following = G._succ.get(person, {})
    return [u for u in followers if u not in following]

person = 'A' 
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
