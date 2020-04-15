from flask import Flask,request,redirect,render_template,url_for
import data_manager

app = Flask(__name__)


@app.route("/")
def all_questions():
    questions = data_manager.read_data('questions')
    return render_template("all_questions.html", questions=questions)


@app.route('/question/<question_id>')
def question(question_id):
    file_data = data_manager.read_data('questions', question_id)
    answers = data_manager.read_data("answers",question_id)
    return render_template('question.html', id=question_id, data=file_data, answers=answers)


@app.route('/question/<question_id>/new_answer', methods=["GET", "POST"])
def post_new_answer(question_id):
    new_id = data_manager.new_id()
    # if request.method == 'GET':

    if request.method == 'POST':
        new_answer = {
            "id": new_id,
            "submission_time": request.form.get('submission_time'),
            "vote_number": request.form.get('vote_number'),
            "question_id": request.form.get('question_id'),
            "message": request.form.get('business_value'),
            "image": request.form.get('image')}
        data_manager.write_data(new_answer)
        return redirect('/question/<question_id>')
    return render_template('new_answer.html', id=question_id)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )