from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Define the database connection
engine = create_engine('sqlite:///example.db', echo=True)  # Use echo=True for logging SQL statements
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the Post class and map it to a table
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(255), nullable=False)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, onupdate=datetime.now)

# Create the table in the database
Base.metadata.create_all(engine)

# Creating a new post
new_post = Post(title='Sample Post', content='This is a sample post content.')
session = Session()
session.add(new_post)
session.commit()

# Querying all posts
all_posts = session.query(Post).all()
for post in all_posts:
    print(f"Post ID: {post.id}, Title: {post.title}, Content: {post.content}")

# Updating a post
post_to_update = session.query(Post).filter_by(id=1).first()
post_to_update.title = 'Updated Post Title'
session.commit()

# Deleting a post
post_to_delete = session.query(Post).filter_by(id=1).first()
session.delete(post_to_delete)
session.commit()

session.close()
