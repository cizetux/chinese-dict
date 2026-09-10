from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    hanzi = Column(String, nullable=False)
    pinyin = Column(String, nullable=False)
    hsk_level = Column(Integer)

    meanings = relationship("Meaning", back_populates="word")
    examples = relationship("Example", back_populates="word")


class Meaning(Base):
    __tablename__ = "meanings"

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer, ForeignKey("words.id"))
    english = Column(String, nullable=False)

    word = relationship("Word", back_populates="meanings")


class Example(Base):
    __tablename__ = "examples"

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer, ForeignKey("words.id"))
    hanzi = Column(String)
    pinyin = Column(String)
    english = Column(String)

    word = relationship("Word", back_populates="examples")