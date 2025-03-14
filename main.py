import sqlite3

def create_table():
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author TEXT UNIQUE
            )
        ''')
        conn.commit()

def add_article(title, content, author):
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Articles (title, content, author) VALUES (?, ?, ?)", (title, content, author))
            conn.commit()
            print("Статтю успішно додано!")
        except sqlite3.IntegrityError:
            print("Помилка: автор має бути унікальним!")

def delete_article(article_id):
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Articles WHERE id = ?", (article_id,))
        conn.commit()
        print("Статтю видалено!")

def view_article(article_id):
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Articles WHERE id = ?", (article_id,))
        article = cursor.fetchone()
        if article:
            print(f"ID: {article[0]}\nЗаголовок: {article[1]}\nТекст: {article[2]}\nАвтор: {article[3]}")
        else:
            print("Стаття не знайдена!")

if __name__ == "__main__":
    create_table()
    add_article("Перша стаття", "Це текст першої статті.", "Автор 1")
    view_article(1)
    delete_article(1)
