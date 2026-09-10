from fastapi import APIRouter
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Word, Meaning, Example
import unicodedata

router = APIRouter()

def normalize_pinyin(text: str):
    text = unicodedata.normalize("NFD", text)
    text = "".join(
        char for char in text
        if unicodedata.category(char) != "Mn"
    )
    return text.lower()


# =========================
# WORDS
# =========================

@router.post("/words")
def create_word(
    hanzi: str,
    pinyin: str,
    hsk_level: int | None = None
):
    db: Session = SessionLocal()

    word = Word(
        hanzi=hanzi,
        pinyin=pinyin,
        hsk_level=hsk_level
    )

    db.add(word)
    db.commit()
    db.refresh(word)
    db.close()

    return word


@router.get("/words")
def get_words():
    db: Session = SessionLocal()

    words = db.query(Word).all()

    result = []

    for word in words:
        result.append({
            "id": word.id,
            "hanzi": word.hanzi,
            "pinyin": word.pinyin,
            "hsk_level": word.hsk_level,
            "meanings": [
                meaning.english
                for meaning in word.meanings
            ],
            "examples": [
                {
                    "hanzi": example.hanzi,
                    "pinyin": example.pinyin,
                    "english": example.english
                }
                for example in word.examples
            ]
        })

    db.close()

    return result


# =========================
# MEANINGS
# =========================

@router.post("/meanings")
def create_meaning(
    word_id: int,
    english: str
):
    db: Session = SessionLocal()

    meaning = Meaning(
        word_id=word_id,
        english=english
    )

    db.add(meaning)
    db.commit()
    db.refresh(meaning)
    db.close()

    return meaning


# =========================
# EXAMPLES
# =========================

@router.post("/examples")
def create_example(
    word_id: int,
    hanzi: str,
    pinyin: str,
    english: str
):
    db: Session = SessionLocal()

    example = Example(
        word_id=word_id,
        hanzi=hanzi,
        pinyin=pinyin,
        english=english
    )

    db.add(example)
    db.commit()
    db.refresh(example)
    db.close()

    return example


# =========================
# SEARCH
# =========================

@router.get("/search")
def search_words(q: str):
    db: Session = SessionLocal()

    words = db.query(Word).all()

    q_normalized = normalize_pinyin(q)

    result = []

    for word in words:
        pinyin_normalized = normalize_pinyin(word.pinyin)

        matches = (
            q.lower() in word.hanzi.lower()
            or q_normalized in pinyin_normalized
            or any(q.lower() in meaning.english.lower()
                   for meaning in word.meanings)
        )

        if matches:
            result.append({
                "id": word.id,
                "hanzi": word.hanzi,
                "pinyin": word.pinyin,
                "hsk_level": word.hsk_level,
                "meanings": [
                    meaning.english
                    for meaning in word.meanings
                ],
                "examples": [
                    {
                        "hanzi": example.hanzi,
                        "pinyin": example.pinyin,
                        "english": example.english
                    }
                    for example in word.examples
                ]
            })

    db.close()

    return result