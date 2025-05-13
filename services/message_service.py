from db.connection import get_connection

def save_message(text):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (text) VALUES (%s);", (text,))
    conn.commit()
    cur.close()
    conn.close()

def get_all_messages():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, text FROM messages ORDER BY id DESC;")
    messages = cur.fetchall()
    cur.close()
    conn.close()
    return messages


def delete_message(message_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM messages WHERE id = %s;", (message_id,))
    conn.commit()
    cur.close()
    conn.close()
