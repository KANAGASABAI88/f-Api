from fastapi import FastAPI

app = FastAPI()


user_db = {
    'jack': {'username': 'jack', 'date_joined': '2021-12-01', 'location': 'New York', 'age': 28},
    'jill': {'username': 'jill', 'date_joined': '2021-12-02', 'location': 'Los Angeles', 'age': 19},
    'jane': {'username': 'jane', 'date_joined': '2021-12-03', 'location': 'Toronto', 'age': 52}
}


@app.get('/users')
def get_users_query(limit: int = 2):
    users_list = list(user_db.values())
    return users_list[:limit]


@app.get('/users/{username}')
def get_users_path(username: str = 'jack'):
    return user_db[username]
