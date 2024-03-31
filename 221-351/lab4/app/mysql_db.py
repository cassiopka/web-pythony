import mysql.connector
from flask import g

class MySql:
    def __init__(self, app) -> None:
        self.app = app
    
    def connection(self):
        if 'db' not in g:
            g.db = self.connect()
        return g.db
    
    def connect(self):
        return connector.connect(**self.config())
    
    def config(self):
        return {
            'user':self.app.config['MYSQL_USER'],
            'password':self.app.config['MYSQL_PASSWORD'],
            'host':self.app.config['MYSQL_HOST'],
            'database':self.app.config['MYSQL_DATABASE'],
        }
        
    def close_connection(self, e=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()