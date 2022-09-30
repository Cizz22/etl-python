from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Float, ForeignKey, text


def dropTable(table: str, engine):
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS {}".format(table)))

def create_sqlite_db():
    """Create a SQLite database with the name of database.db"""
    engine = create_engine('sqlite:///database.db', future=True)
    
    with engine.connect() as conn:
        return engine

def create_table_users():
    metadata = MetaData()
    engine = create_sqlite_db()

    users = Table('users', metadata,
                  Column('id', String, primary_key=True),
                  Column('name', String, nullable=False),
                  Column('email', String, nullable=False),
                  Column('whatsapp', String, nullable=False),
                  )
    dropTable('users', engine)
    users.create(engine)


def create_table_tickets():
    metadata = MetaData()

    engine = create_sqlite_db()

    users = Table('users', MetaData(),
                       autoload=True, autoload_with=engine)

    videos = Table("tickets",  metadata,
                   Column("id", String, primary_key=True),
                   Column("user_id", String, ForeignKey(users.c.id)),
                   Column("status", String),
                   Column("ticketFile", String, nullable=False),
                   Column("created_at", String, nullable=False),
                   )

    dropTable('tickets', engine)
    videos.create(engine)
    
    
def create_table_total_tickets():
    metadata = MetaData()
    engine = create_sqlite_db()

    users = Table('users', MetaData(),
                  autoload=True, autoload_with=engine)

    ticket_counts = Table("ticket_counts", metadata,
                  Column("id", Integer, primary_key=True),
                  Column("user_id", String, ForeignKey(users.c.id)),
                  Column("total_ticket", String, default=0),
                  )

    dropTable('ticket_counts', engine)
    ticket_counts.create(engine)

def main():
    create_table_users()
    create_table_tickets()
    create_table_total_tickets()