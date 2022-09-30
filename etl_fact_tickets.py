from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float, DateTime, ForeignKey, Boolean, select, insert, text, ForeignKeyConstraint
import pre_etl
import csv

def insertData(table: Table, file, engine):
    with engine.connect() as conn:
        with open(file, 'r', encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            data = [{"id": row[0], "user_id": row[6], "status": row[5], "ticketFile":row[1], "created_at":row[7]} for row in csv_reader]
            conn.execute(insert(table), data)
            conn.commit()

def copy_tickets():
    """Copy all rows in table "tickets" from csv to SQLite."""
    engine = pre_etl.create_sqlite_db()

    users = Table('tickets', MetaData(),
                        autoload=True, autoload_with=engine)
    
    insertData(users, 'data_tickets.csv', engine)
