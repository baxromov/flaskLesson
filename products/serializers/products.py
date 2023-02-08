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
select * from product limit 10 offset 50
"""
