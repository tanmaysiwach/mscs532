import sqlite3
import random
import string
import time
import pandas as pd
# ==============================================================
# 1. Create SQLite in-memory database and table
# ==============================================================

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS follows (
    follower_id TEXT,
    followed_id TEXT,
    PRIMARY KEY (follower_id, followed_id)
)
""")
cur.execute("CREATE INDEX IF NOT EXISTS idx_follower_id ON follows(follower_id)")
cur.execute("CREATE INDEX IF NOT EXISTS idx_followed_id ON follows(followed_id)")

# ==============================================================
# 2. Generate random follow relationships for users A–Z
# ==============================================================

users = list(string.ascii_uppercase)  # ['A', 'B', ..., 'Z']
double_letters = [a + b for a in string.ascii_uppercase for b in string.ascii_uppercase]
triple_letters = [a + b + c for a in string.ascii_uppercase for b in string.ascii_uppercase for c in string.ascii_uppercase]
users = users + double_letters + triple_letters

for user in users:
    num_follows = random.randint(1, 18278)  # Each user follows between 1 and 18278 people
    followed_users = random.sample(users, num_follows)

    # Ensure a user does not follow themselves
    if user in followed_users:
        followed_users.remove(user)

    # Insert relationships into the database
    for followed in followed_users:
        try:
            cur.execute("INSERT INTO follows VALUES (?, ?)", (user, followed))
        except sqlite3.IntegrityError:
            # Ignore duplicates if they occur
            pass

conn.commit()

# ==============================================================
# 3. Helper function to display query results
# ==============================================================

def fetch_list(query, params=()):
    cur.execute(query, params)
    return [r[0] for r in cur.fetchall()]

# ==============================================================
# 4. Demonstration Queries for person 'A'
# ==============================================================

person = 'A'
# ==============================================================
# 5. Print results
# ==============================================================

print("\n========== RANDOM SOCIAL GRAPH (A–Z) ==========")
all_relationships = cur.execute("SELECT * FROM follows").fetchall()
df = pd.DataFrame(all_relationships, columns=["follower_id", "followed_id"])
df.to_csv("follows_data_scaled.csv", index=False)
print("Total follow relationships:", cur.execute("SELECT COUNT(*) FROM follows").fetchone()[0])
print("===============================================")
start_time = time.time()
# 1. Who A follows
query1 = "SELECT followed_id FROM follows WHERE follower_id=?"
who_a_follows = fetch_list(query1, (person,))
print(f"1. {person} follows:")
end_time = time.time()
print(f"Query executed in: {end_time - start_time:.6f}s")
start_time = time.time()
# 2. Who follows A
query2 = "SELECT follower_id FROM follows WHERE followed_id=?"
who_follows_a = fetch_list(query2, (person,))
print(f"2. Who follows {person}:")
end_time = time.time()
print(f"Query executed in: {end_time - start_time:.6f}s")
start_time = time.time()
# 3. Who A follows that follows them back (mutual)
query3 = """
SELECT f1.followed_id
FROM follows f1
JOIN follows f2 ON f1.followed_id = f2.follower_id
WHERE f1.follower_id=? AND f2.followed_id=?
"""
mutuals = fetch_list(query3, (person, person))
print(f"3. Mutual follows with {person}:")
end_time = time.time()
print(f"Query executed in: {end_time - start_time:.6f}s")
start_time = time.time()
# 4. Who A follows that does not follow them back
query4 = """
SELECT followed_id
FROM follows f1
WHERE f1.follower_id=?
AND followed_id NOT IN (
    SELECT follower_id FROM follows WHERE followed_id=?
)
"""
a_one_way = fetch_list(query4, (person, person))
print(f"4. {person} follows but not followed back:")
end_time = time.time()
print(f"Query executed in: {end_time - start_time:.6f}s")
start_time = time.time()
# 5. Who follows A that A does not follow back
query5 = """
SELECT follower_id
FROM follows f1
WHERE f1.followed_id=?
AND follower_id NOT IN (
    SELECT followed_id FROM follows WHERE follower_id=?
)
"""
follows_a_only = fetch_list(query5, (person, person))
print(f"5. Follows {person} but {person} doesn’t follow back:")
end_time = time.time()
print(f"Query executed in: {end_time - start_time:.6f}s")

# ==============================================================
# 6. (Optional) Display sample of the entire follows table
# ==============================================================

print("\n--- SAMPLE FOLLOWS DATA (first 30 rows) ---")
for row in cur.execute("SELECT * FROM follows LIMIT 30"):
    print(row)

conn.close()