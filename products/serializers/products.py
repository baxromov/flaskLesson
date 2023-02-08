from flask import jsonify
from functools import wraps

from products.models.products import Product


def product_serializer(query: Product) -> list:
    if isinstance(query, list):
        return [{"id": i.id, "name": i.name, "city": i.city} for i in query]
    return {"id": query.id, "name": query.name, "city": query.city}


def paginator(**_kwargs):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            data = func(*args, **kwargs).json
            return jsonify([i for i in data[:_kwargs['limit'] if _kwargs.get('limit') else 5]])
        return inner
    return wrapper


"""
select * from product limit 3 offset 6

1 2 3 4 5 6 7 8 9 10
"""
