from flask import Flask
app = Flask(__name__)


@app.route(r'/', methods = ['GET'])
def contact_book():
    return render_template('contact_book.html')


@app.router(r'add'. methods=['GET'. 'POST'])
def add_contact():

    if request.form:
        print(request.form.get('name'))
        print(request.form.get('phone'))
        print(request.form.get('email'))

    return render_template('add_contact.html')


if __name__ == '__main__':
    app.run()

