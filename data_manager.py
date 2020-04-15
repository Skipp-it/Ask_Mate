import connection
import os

ANSWER_PATH = os.getenv('ANSWER_PATH') if 'ANSWER_PATH' in os.environ else 'answer.csv'
QUESTIONS_PATH = os.getenv('QUESTIONS_PATH') if 'QUESTIONS_PATH' in os.environ else 'question.csv'

DATA_HEADER_ANSWER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
DATA_HEADER_QUESTIONS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message','image']


def write_data(new_data,action):
    if action == "answers":
        connection.add_in_csv(ANSWER_PATH, new_data, DATA_HEADER_ANSWER)


def read_data(file, id=None):
    if file == "answers":
        question_answers = []
        for answer in connection.get_data(ANSWER_PATH):
            if answer['question_id']== id:
                question_answers.append(answer)
        return question_answers

    elif file == "questions":
        return connection.get_data(QUESTIONS_PATH, id)
    else:
        print("esti prost ai gresit comanda de fisier")    # de sters la final




def update_question(question_id, update_dict):
    connection.update_in_csv(question_id, update_dict, QUESTIONS_PATH, DATA_HEADER_QUESTIONS)
    return "Done"

update_dicti = {'id': '1', 'submission_time': '1493368154', 'view_number': '29', 'vote_number': '7', 'title': 'How to make lists in Python?', 'message': 'I am totally new to this, any hints?', 'image': ''}
update_question('1', update_dicti)

