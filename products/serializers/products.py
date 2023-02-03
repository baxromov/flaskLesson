from products.models.products import Product


def product_serializer(query: Product) -> list:
    data, datum = [], dict()

    if isinstance(query, list):
        for item in query:
            datum['id'] = item.id
            datum['name'] = item.name
            datum['city'] = item.city
            data.append(datum)
        return data
    datum['id'] = query.id
    datum['name'] = query.name
    datum['city'] = query.city
    return datum
