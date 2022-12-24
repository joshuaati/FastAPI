from datetime import datetime
import enum

from sqlalchemy import Emun, Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from ..db import Base
from .user import User
from .mixins import Timestamp

class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3

class Course(Timestamp, Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_by = relationship(User)







