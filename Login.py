def login(credentials, username, password):
    user = credentials.get(username, "empty")
    if user != "empty":
        if user == password:
            return "Welcome user"

    else:
        return "check your credentials"
