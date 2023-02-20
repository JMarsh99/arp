class Config():
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/arp_db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
