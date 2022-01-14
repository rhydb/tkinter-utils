import sqlite3 as sql


class Database:
    def __init__(self, file):
        self.con = sql.connect(file)
        self.cur = self.con.cursor()

    def query(self, statement, data=()):
        self.cur.execute(statement, data)
        self.con.commit()
        return self.cur

    def select(self, table, where, fields, condition="AND"):
        field_str = ','.join(fields)
        if len(where) == 0:
            statement = f'''SELECT {field_str} FROM {table}'''
            return self.query(statement)
        where_arr, where_vals = self.parse_dict(where)
        where_str = condition.join(where_arr)
        statement = f'''SELECT {field_str} FROM {table} WHERE {where_str}'''
        return self.query(statement, where_vals)

    def fetch(self, table, where, fields=["*"], condition="AND"):
        return self.select(table, where, fields, condition).fetchone()

    def fetch_all(self, table, where, fields=["*"], condition="AND"):
        return self.select(table, where, fields, condition).fetchall()

    def insert(self, table, data):
        fields = ','.join(data)
        q_str = ','.join(['?'] * len(data))
        statement = f'''INSERT INTO {table} ({fields}) VALUES ({q_str})'''
        return self.query(statement, tuple(data.values()))

    def update(self, table, data, where, condition="AND"):
        data_arr, data_vals = self.parse_dict(data)
        data_str = ','.join(data_arr)
        where_arr, where_vals = self.parse_dict(where)
        where_str = condition.join(where_arr)
        statement = f'''UPDATE {table} SET {data_str} WHERE {where_str}'''
        return self.query(statement, data_vals + where_vals)

    def delete(self, table, where, condition="AND"):
        where_arr, where_vals = self.parse_dict(where)
        where_str = condition.join(where_arr)
        statement = f'''DELETE FROM {table} WHERE {where_str}'''
        return self.query(statement, where_vals)

    def parse_dict(self, data):
        vals = list(data.values())
        keys = []
        for i in data:
            keys.append(f"{i} = ?")
        return (keys, vals)

    def quit(self):
        self.con.close()

    def create(self):
        statement = f'''
        CREATE TABLE IF NOT EXISTS test ( `fname` VARCHAR(50) NOT NULL , `lname` VARCHAR(50) NOT NULL , `dob` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP);
        '''
        return self.query(statement)
