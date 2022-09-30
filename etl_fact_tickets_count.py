from enum import auto
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float, DateTime, ForeignKey, Boolean, select, insert, text, ForeignKeyConstraint
import pre_etl

def count_tickets():
    """Count the number of tickets in the table "tickets"."""
    engine = pre_etl.create_sqlite_db()
    
    with engine.connect() as conn:
        result = conn.execute(text("SELECT users.id, COUNT(tickets.id) as total_ticket FROM tickets INNER JOIN users ON tickets.user_id = users.id GROUP BY users.id ORDER BY COUNT(tickets.id) DESC"))
        return [dict(row) for row in result]

def insert_data():
    """Insert the result of count_tickets() into table "tickets_count"."""
    engine = pre_etl.create_sqlite_db()
    ticket_counts = Table('ticket_counts', MetaData(),
                        autoload=True, autoload_with=engine)
    
    with engine.connect() as conn:
        data = count_tickets()
        conn.execute(insert(ticket_counts), [{"user_id": row["id"], "total_ticket": row["total_ticket"]} for row in data])
        conn.commit()
        
