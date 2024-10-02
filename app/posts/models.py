import datetime

from sqlalchemy import Column, BigInteger, String, Text, Boolean, TIMESTAMP, insert, select, update, delete, ForeignKey


from app.base import Base

from app.database import async_session_maker
class Post(Base):
    __tablename__ = 'posts'
    id = Column(BigInteger, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now)
    likes_count = Column(BigInteger, nullable=True)




