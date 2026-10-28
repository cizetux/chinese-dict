from app.database import SessionLocal
from app.models import Word, Meaning, Example


db = SessionLocal()


words = [
    {
        "hanzi": "你好",
        "pinyin": "nǐ hǎo",
        "hsk_level": 1,
        "meanings": ["hello"],
        "examples": [
            {
                "hanzi": "你好！",
                "pinyin": "Nǐ hǎo!",
                "english": "Hello!"
            }
        ]
    },
    {
        "hanzi": "好",
        "pinyin": "hǎo",
        "hsk_level": 1,
        "meanings": ["good", "well", "fine"],
        "examples": [
            {
                "hanzi": "我很好。",
                "pinyin": "Wǒ hěn hǎo.",
                "english": "I am very well."
            }
        ]
    },
    {
        "hanzi": "你",
        "pinyin": "nǐ",
        "hsk_level": 1,
        "meanings": ["you"],
        "examples": [
            {
                "hanzi": "你好吗？",
                "pinyin": "Nǐ hǎo ma?",
                "english": "How are you?"
            }
        ]
    }
]


for data in words:
    word = (
        db.query(Word)
        .filter(Word.hanzi == data["hanzi"])
        .first()
    )

    if word is None:
        word = Word(
            hanzi=data["hanzi"],
            pinyin=data["pinyin"],
            hsk_level=data["hsk_level"]
        )
        db.add(word)
        print(f"New word: {data['hanzi']}")
    else:
        word.pinyin = data["pinyin"]
        word.hsk_level = data["hsk_level"]
        print(f"Updated word: {data['hanzi']}")

    existing_meanings = {
        meaning.english
        for meaning in word.meanings
    }

    for meaning in data["meanings"]:
        if meaning not in existing_meanings:
            word.meanings.append(
                Meaning(english=meaning)
            )

    existing_examples = {
        (
            example.hanzi,
            example.pinyin,
            example.english
        )
        for example in word.examples
    }

    for example in data["examples"]:
        example_key = (
            example["hanzi"],
            example["pinyin"],
            example["english"]
        )

        if example_key not in existing_examples:
            word.examples.append(
                Example(
                    hanzi=example["hanzi"],
                    pinyin=example["pinyin"],
                    english=example["english"]
                )
            )

db.commit()
print("Import completed successfully!")
db.close()