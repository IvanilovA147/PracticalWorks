import sqlite3

def execute_query(query, params=(), fetch=False):
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.execute(query, params)
        return cursor.fetchall() if fetch else None

def create_table():
    execute_query('''CREATE TABLE IF NOT EXISTS Articles (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        author TEXT UNIQUE)''')

def add_article(title, content, author):
    try:
        execute_query("INSERT INTO Articles (title, content, author) VALUES (?, ?, ?)", (title, content, author))
        print("Статтю успішно додано!")
    except sqlite3.IntegrityError:
        print("Помилка: автор має бути унікальним!")

def delete_article(article_id):
    execute_query("DELETE FROM Articles WHERE id = ?", (article_id,))
    print("🗑️ Статтю видалено!")

def view_article(article_id):
    article = execute_query("SELECT * FROM Articles WHERE id = ?", (article_id,), fetch=True)
    if article:
        print(f" ID: {article[0][0]}\n Заголовок: {article[0][1]}\n📖 Текст: {article[0][2]}\n️ Автор: {article[0][3]}")
    else:
        print("⚠️ Стаття не знайдена!")

if __name__ == "__main__":
    create_table()
    add_article("Перша стаття", "Це текст першої статті.", "Автор 1")
    view_article(1)
    delete_article(1)