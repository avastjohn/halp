import config
import bcrypt
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime, Text

from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

from flask.ext.login import UserMixin, login_user

engine = create_engine(config.DB_URI, echo=False) 
session = scoped_session(sessionmaker(bind=engine,
                         autocommit = False,
                         autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

class User(Base, UserMixin):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    salt = Column(String(64), nullable=False)
    role = Column(Integer, nullable=False)

    posts = relationship("Post", uselist=True)

    def set_password(self, password):
        self.salt = bcrypt.gensalt()
        password = password.encode("utf-8")
        self.password = bcrypt.hashpw(password, self.salt)

    def authenticate(self, password):
        password = password.encode("utf-8")
        return bcrypt.hashpw(password, self.salt.encode("utf-8")) == self.password



class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    location = Column(String(64), nullable=False)
    urgency = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")

    def nevermind(self):
        session.delete(self)
        session.commit()

def register(email, password, role):
    user = User(email=email, password=password, role=role, salt="random")
    user.set_password(password)
    session.add(user)
    session.commit()
    # login_user(user)
    return user

def create_tables():
    Base.metadata.create_all(engine)
    u = User(email="test@test.com", password="unicorn", role=1)
    u.set_password("unicorn")
    session.add(u)
    p = Post(title="This is a test post", location="In your butt", urgency=0)
    u.posts.append(p)
    session.commit()

if __name__ == "__main__":
    create_tables()
