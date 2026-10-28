from app.database import SessionLocal
from app.models import Word, Meaning, Example


db = SessionLocal()


words = [
        {
        "hanzi": "我",
        "pinyin": "wǒ",
        "hsk_level": 1,
        "meanings": ["I", "me"],
        "examples": [
            {
                "hanzi": "我是学生。",
                "pinyin": "Wǒ shì xuésheng.",
                "english": "I am a student."
            }
        ]
    },
    {
        "hanzi": "是",
        "pinyin": "shì",
        "hsk_level": 1,
        "meanings": ["to be", "is", "am", "are"],
        "examples": [
            {
                "hanzi": "我是法国人。",
                "pinyin": "Wǒ shì Fǎguó rén.",
                "english": "I am French."
            }
        ]
    },
    {
        "hanzi": "不",
        "pinyin": "bù",
        "hsk_level": 1,
        "meanings": ["not", "no"],
        "examples": [
            {
                "hanzi": "我不去。",
                "pinyin": "Wǒ bú qù.",
                "english": "I am not going."
            }
        ]
    },
    {
        "hanzi": "吗",
        "pinyin": "ma",
        "hsk_level": 1,
        "meanings": ["question particle"],
        "examples": [
            {
                "hanzi": "你好吗？",
                "pinyin": "Nǐ hǎo ma?",
                "english": "How are you?"
            }
        ]
    },
    {
        "hanzi": "谢谢",
        "pinyin": "xièxie",
        "hsk_level": 1,
        "meanings": ["thank you", "thanks"],
        "examples": [
            {
                "hanzi": "谢谢你！",
                "pinyin": "Xièxie nǐ!",
                "english": "Thank you!"
            }
        ]
    },
    {
        "hanzi": "再见",
        "pinyin": "zàijiàn",
        "hsk_level": 1,
        "meanings": ["goodbye", "see you again"],
        "examples": [
            {
                "hanzi": "明天见！",
                "pinyin": "Míngtiān jiàn!",
                "english": "See you tomorrow!"
            }
        ]
    },
    {
        "hanzi": "他",
        "pinyin": "tā",
        "hsk_level": 1,
        "meanings": ["he", "him"],
        "examples": [
            {
                "hanzi": "他是学生。",
                "pinyin": "Tā shì xuésheng.",
                "english": "He is a student."
            }
        ]
    },
    {
        "hanzi": "她",
        "pinyin": "tā",
        "hsk_level": 1,
        "meanings": ["she", "her"],
        "examples": [
            {
                "hanzi": "她很好。",
                "pinyin": "Tā hěn hǎo.",
                "english": "She is very well."
            }
        ]
    },
    {
        "hanzi": "人",
        "pinyin": "rén",
        "hsk_level": 1,
        "meanings": ["person", "people"],
        "examples": [
            {
                "hanzi": "中国人",
                "pinyin": "Zhōngguó rén",
                "english": "Chinese person"
            }
        ]
    },
    {
        "hanzi": "中国",
        "pinyin": "Zhōngguó",
        "hsk_level": 1,
        "meanings": ["China"],
        "examples": [
            {
                "hanzi": "我去中国。",
                "pinyin": "Wǒ qù Zhōngguó.",
                "english": "I am going to China."
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