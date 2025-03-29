class UserNotFoundError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class UserAuth:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError(f"Użytkownik '{username}' nie istnieje.")
        if self.users[username] != password:
            raise WrongPasswordError("Nieprawidłowe hasło.")

        print(f"Użytkownik '{username}' zalogowany pomyślnie!")


auth = UserAuth({"admin": "1234", "user": "abcd"})

try:
    auth.login("admin", "1234")
    auth.login("unknown", "pass")
    auth.login("user", "wrongpass")
except Exception as e:
    print(f"Błąd: {e}")