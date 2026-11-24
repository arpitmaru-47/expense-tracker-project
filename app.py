import os
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date

app = Flask(__name__)

def get_db_connections():
    os.makedirs("/app/data", exist_ok=True)

    conn = sqlite3.connect("/app/data/expenses.db")
    conn.row_factory = sqlite3.Row
    
    return conn 


def init_db():
    conn = get_db_connections()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = get_db_connections()

    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY id DESC"
    ).fetchall()

    result = conn.execute(
        "SELECT SUM(amount) AS total FROM expenses"
    ).fetchone()

    total = result["total"] or 0

    count = conn.execute(
        "SELECT COUNT(*) FROM expenses"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        count=count
    )

@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form["title"]
    amount = float(request.form["amount"])
    category = request.form["category"]
    expense_date = date.today().isoformat()

    conn = get_db_connections()

    conn.execute("""
        INSERT INTO expenses (title, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (title, amount, category, expense_date))

    conn.commit()
    conn.close()

    return redirect(url_for("home"))

#UPDATE EXPENSE
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_expense(id):

    conn = get_db_connections()

    expense = conn.execute(
        "SELECT * FROM expenses WHERE id = ?", (id,)
    ).fetchone()

    if expense is None:
        conn.close()
        return "Exponse not found", 404

    if request.method == "POST":

        title = request.form["title"]
        amount = float(request.form["amount"])
        category = request.form["category"]

        conn.execute("""
            UPDATE expenses
            SET title = ?, amount = ?, category = ?
            WHERE id = ?
        """, (title, amount, category, id))

        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    conn.close()

    return render_template("edit.html", expense=expense)

# DELETE EXPENSE
@app.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):

    conn = get_db_connections()

    conn.execute(
        "DELETE FROM expenses WHERE id = ?", (id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("home"))

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)