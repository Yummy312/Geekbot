import sqlite3
from sqlite3 import Error
from config import bot
from random import choice


def create_bot_db():
    try:
        global db, cursor
        db = sqlite3.connect(r"mentors_data.db")
        cursor = db.cursor()
        cursor.execute(r"CREATE TABLE IF NOT EXISTS mentors("
                       r"id_mentor INTEGER PRIMARY KEY AUTOINCREMENT,"
                       r"name_mentor TEXT,"
                       r"direct_mentor TEXT,"
                       r"age_mentor INTEGER,"
                       r"group_mentor TEXT)")

        db.commit()

    except Error as e:
        print(e)


async def command_insert_sql(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors(id_mentor,name_mentor,direct_mentor,age_mentor,group_mentor) VALUES(?,?,"
                       "?,?,?)",
                       tuple(data.values()))
        print(data.values())
        db.commit()


async def command_all_mentors_sql():
    res = cursor.execute('SELECT*FROM mentors')
    mentors = res.fetchall()
    return mentors


async def random_choice_mentor(message):
    res = cursor.execute('SELECT*FROM mentors')
    mentors = res.fetchall()
    mentor = choice(mentors)
    await message.answer(f"id: {mentor[0]}\nname: {mentor[1]}\ndirect: {mentor[2]}\n"
                         f"age: {mentor[3]}\ngroup: {mentor[4]}")


async def command_delete_sql(id):
    cursor.execute("DELETE FROM mentors WHERE id_mentor = ?", (id,))
    db.commit()
