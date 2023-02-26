import db
import models

values = [
    models.User(name="Пирожков Артур"),
    models.User(name="Никита Никитов"),
    models.User(name="Адрей Андреев"),
]

for value in values:
    try:
        session = db.SessionLocal()
        session.add(value)
        session.commit()
    except Exception as e:
        pass
