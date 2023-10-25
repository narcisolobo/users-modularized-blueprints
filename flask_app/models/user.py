from flask_app.config.mysql_connection import connect_to_mysql

DB = "users_db"


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, form_data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
        """
        user_id = connect_to_mysql(DB).query_db(query, form_data)
        return user_id

    @classmethod
    def find_by_id(cls, id):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """
        data = {"id": id}
        results = connect_to_mysql(DB).query_db(query, data)

        if len(results) == 0:
            return None

        user = User(results[0])
        return user

    @classmethod
    def find_all(cls):
        query = """
        SELECT * from users;
        """
        results = connect_to_mysql(DB).query_db(query)

        users = []
        for result in results:
            users.append(User(result))
            print(type(User(result).created_at))

        return users

    @classmethod
    def update(cls, form_data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(id)s;
        """
        connect_to_mysql(DB).query_db(query, form_data)
        return

    @classmethod
    def delete(cls, id):
        query = """
        DELETE FROM users WHERE id = %(id)s;
        """
        data = {"id": id}
        connect_to_mysql(DB).query_db(query, data)
        return

    def full_name(self):
        """Returns the user's full name."""
        return f"{self.first_name} {self.last_name}"
