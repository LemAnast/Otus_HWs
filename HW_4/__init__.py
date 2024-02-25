import os

def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


BOOKS_CSV = get_path('books.csv')
USERS_JSON = get_path('users.json')


RESULT_JSON_W = get_path('result.json')
