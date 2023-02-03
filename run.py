from main import app, model

if __name__ == '__main__':
    model.create_all()
    app.run(debug=True, port=8000)
