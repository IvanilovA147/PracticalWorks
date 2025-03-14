import sqlite3

def zapit(query, params=(),fetch=False):
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.execute(query, params)
        return cursor.fetchall() if fetch else None

def create():
    zapit('''CREATE TABLE IF NOT EXISTS Articles (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL,
                            author TEXT UNIQUE)''')

def add(title, content, author):
    try:
        zapit("INSERT INTO Articles (title, content, author) VALUES (?, ?, ?)", (title, content, author))
        print("Статтю успішно додано!")
    except sqlite3.IntegrityError:
        print("Помилка: автор має бути унікальним!")

def delete(tipa_id):
    zapit("DELETE FROM Articles WHERE id = ?", (tipa_id,))
    print("🗑️ Статтю видалено!")


def view(tipa_id):
    article = zapit("SELECT * FROM Articles WHERE id = ?", (tipa_id,), fetch=True)
    if article:
        print(f" ID: {article[0][0]}\n Заголовок: {article[0][1]}\n📖 Текст: {article[0][2]}\n️ Автор: {article[0][3]}")
    else:
        print("⚠️ Стаття не знайдена!")



if __name__ == "__main__":
    create()
    add("Перша стаття", "Це текст першої статті.", "Автор 1")
    view(1)
    delete(1)