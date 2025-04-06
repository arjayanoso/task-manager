from . import database

def add_task(title, description="", due_date=None, conn=None):
    """Add a new task to the database."""
    if conn is None:
        conn = database.get_connection()
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, description, due_date, done)
        VALUES (?, ?, ?, 0)
    """, (title, description, due_date))
    conn.commit()
    task_id = cursor.lastrowid

    if close_conn:
        conn.close()
    return task_id

def list_tasks(conn=None):
    """Return a list of all tasks."""
    if conn is None:
        conn = database.get_connection()
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if close_conn:
        conn.close()
    return tasks

def mark_task_done(task_id, conn=None):
    """Mark a task as completed."""
    if conn is None:
        conn = database.get_connection()
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    updated = cursor.rowcount

    if close_conn:
        conn.close()
    return updated

def delete_task(task_id, conn=None):
    """Delete a task from the database."""
    if conn is None:
        conn = database.get_connection()
        close_conn = True
    else:
        close_conn = False

    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    deleted = cursor.rowcount

    if close_conn:
        conn.close()
    return deleted
