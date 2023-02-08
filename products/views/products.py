from werkzeug import Response

from main import model
from products.models.products import Product
from flask import jsonify, request
import json

from products.serializers.products import product_serializer, paginator


@paginator(limit=3)
def product(q=request):
    query = Product.query.all()
    serializer = product_serializer(query)
    return jsonify(serializer)


def product_detail(name):
    """
    Products View
    :return: str
    """
    return "Product %s" % name


def product_create(request=request):
    """
    Products View
    :return: str
    """
    data = json.loads(request.data)
    product = Product(name=data['name'], city=data['city'])
    model.session.add(product)
    model.session.commit()
    serializer = product_serializer(product)
    return jsonify(serializer)
