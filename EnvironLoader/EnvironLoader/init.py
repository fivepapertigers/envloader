from .db import create_db, create_tables

def main():
    print "Creating DB..."
    create_db()
    print "DB created"
    print "Creating tables..."
    create_tables()
    print "Tables created"
    print "Setup complete"
