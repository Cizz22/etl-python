from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float, DateTime, ForeignKey, Boolean, select, insert, text, ForeignKeyConstraint
import pre_etl
import csv

def getData(table: Table, engine):
    with engine.connect() as conn:
        result = [dict(row) for row in conn.execute(select(table))]
    return result


def insertData(table: Table, file, engine):
    with engine.connect() as conn:
        with open(file, 'r', encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            data = [{"id": row[0], "name": row[1], "email": row[2], "whatsapp":row[3]} for row in csv_reader]
            conn.execute(insert(table), data)
            conn.commit()

def copy_users():
    """Copy all rows in table "users" from csv to SQLite."""
    engine = pre_etl.create_sqlite_db()

    users = Table('users', MetaData(),
                        autoload=True, autoload_with=engine)
    
    insertData(users, 'data_users.csv', engine)
