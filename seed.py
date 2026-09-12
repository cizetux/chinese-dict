from app.database import SessionLocal
from app.models import Word, Meaning, Example


db = SessionLocal()


word = Word(
    hanzi="好",
    pinyin="hǎo",
    hsk_level=1
)

word.meanings = [
    Meaning(english="good"),
    Meaning(english="well"),
    Meaning(english="fine")
]

word.examples = [
    Example(
        hanzi="我很好。",
        pinyin="Wǒ hěn hǎo.",
        english="I am very well."
    )
]

db.add(word)
db.commit()

print("Word added successfully!")

db.close()