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

    word = Word(
        hanzi=data["hanzi"],
        pinyin=data["pinyin"],
        hsk_level=data["hsk_level"]
    )

    word.meanings = [
        Meaning(english=meaning)
        for meaning in data["meanings"]
    ]

    word.examples = [
        Example(
            hanzi=example["hanzi"],
            pinyin=example["pinyin"],
            english=example["english"]
        )
        for example in data["examples"]
    ]

    db.add(word)


db.commit()

print("Words imported successfully!")

db.close()