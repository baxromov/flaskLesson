from flask import jsonify, request

from products.models.products import Product
from products.serializers.products import product_serializer, paginator
from sqlalchemy import text


@paginator(limit=1)
def search():
    q = request.args.get('q')
    if q:
        query = Product.query.filter(Product.name.icontains(q)).all()
        serializer = product_serializer(query)
        return jsonify(serializer)
    query = Product.query.all()
    serializer = product_serializer(query)
    return jsonify(serializer)
