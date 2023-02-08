from main import model


class Product(model.Model):
    id = model.Column('id', model.Integer, primary_key=True)
    name = model.Column(model.String(100))
    city = model.Column(model.String(50))

    def __init__(self, name, city):
        self.name = name
        self.city = city
