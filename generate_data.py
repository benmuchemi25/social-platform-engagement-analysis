import psycopg2
from faker import Faker
import random 

fake = Faker ()

conn = psycopg2.connect(
    dbname="social_platform",
    user="postgres",
    password="Busia2009$",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

categories = [
    ("Technology", "Posts about software, hardware, and tech news"),
    ("Science", "Discussions on scientific discoveries and research"),
    ("Gaming", "Video games, reviews, and gaming culture"),
    ("Sports", "News and discussions about sports"),
    ("Music", "Artists, albumbs, and music discussions"),
    ("Movies", "Film reviews and discssions"),
    ("Politics", "Political news and debates"),
    ("Food", "Recipes, restaurants, and food culture"),
    ("Travel", "Destinations, tips, and travel stories"),
    ("Health", "Fitness, mental health, and wellness")
]

for name, desc in categories:
    cur.execute("INSERT INTO Categories (Name, Description) VALUES (%s, %s) ON CONFLICT DO NOTHING", (name, desc))


user_ids = []

for _ in range(500):
    username = fake.unique.user_name()
    email = fake.unique.email()
    password_hash = fake.sha256()
    join_date = fake.date_time_between(start_date="-2y", end_date="now")
    cur.execute(
        "INSERT INTO Users (Username, Email, PasswordHash, JoinDate) VALUES (%s, %s, %s, %s) RETURNING UserID",
        (username, email, password_hash, join_date)
    )
    user_ids.append(cur.fetchone()[0])

post_ids = []

for _ in range (2000):
    user_id = random.choice(user_ids)
    category_id = random.randint(1,10)
    title = fake.sentence(nb_words=8)
    body = fake.paragraph(nb_sentences=5)
    timestamp = fake.date_time_between(start_date="-1y", end_date="now")
    cur.execute(
        "INSERT INTO Posts (UserID, CategoryID, Title, Body, Timestamp) VALUES (%s, %s, %s, %s, %s) RETURNING PostID",
        (user_id, category_id, title, body, timestamp)
    )
    post_ids.append(cur.fetchone()[0])

for _ in range (10000):
    post_id = random.choice(post_ids)
    user_id = random.choice(user_ids)  
    body = fake.paragraph(nb_sentences=2)
    timestamp = fake.date_time_between(start_date="-1y", end_date="now")
    cur.execute(
        "INSERT INTO Comments (PostID, UserID, Body, Timestamp) VALUES (%s, %s, %s, %s)",
        (post_id, user_id, body, timestamp)
    )

for _ in range (15000):
    user_id = random.choice(user_ids)
    post_id = random.choice(post_ids)
    vote_type = random.choice([1, -1])
    timestamp = fake.date_time_between(start_date="-1y", end_date="now")
    cur.execute(
        "INSERT INTO Votes (UserID, PostID, VoteType, Timestamp) VALUES (%s, %s, %s, %s)",
        (user_id, post_id, vote_type, timestamp)
    )

for category_id in range (1, 11):
    mod_user = random.choice(user_ids)
    cur.execute(
        "INSERT INTO Moderators (UserID, CategoryID) VALUES (%s, %s)",
        (mod_user, category_id)
    )

for _ in range (500):
    user_id = random.choice(user_ids)
    post_id = random.choice(post_ids)
    reason = random.choice(["Spam", "Hate speech", "Misinformation", "Harassment", "Off topic"]) 
    cur.execute(
        "INSERT INTO Reports (UserID, PostID, Reason) VALUES (%s, %s, %s)",
        (user_id, post_id, reason)
    )

for _ in range(3000):
    sender_id = random.choice(user_ids)
    receiver_id = random.choice(user_ids)
    if sender_id != receiver_id:
        body = fake.sentence()
        timestamp = fake.date_time_between(start_date="-1y", end_date="now")
        cur.execute(
            "INSERT INTO Messages (SenderID, ReceiverID, Body, Timestamp) VALUES (%s, %s, %s, %s)",
            (sender_id, receiver_id, body, timestamp)
        )

for _ in range(5000):
    follower_id = random.choice(user_ids)
    followed_id = random.choice(user_ids)
    if follower_id != followed_id:
        cur.execute(
            "INSERT INTO Followers (FollowerUserID, FollowedUserID) VALUES (%s, %s)",
            (follower_id, followed_id)
        )        

for _ in range(8000):
    user_id = random.choice(user_ids)
    message = random.choice([
        "Someone commented on your post",
        "Your post received an upvote",
        "You have a new follower",
        "Someone mentioned you in a comment",
        "Your report was reviewed"
    ])
    is_read = random.choice([True, False])
    cur.execute(
        "INSERT INTO Notifications (UserID, Message, IsRead) VALUES (%s, %s, %s)",
        (user_id, message, is_read)
    )

conn.commit()
cur.close()
conn.close()
print("Data generation complete!")