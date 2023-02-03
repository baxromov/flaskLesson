from main import app
from products.views.products import *
from products.views.category import *
from products.views.admin import *

# Product urls
app.add_url_rule('/product', view_func=product)
app.add_url_rule('/product/<name>', view_func=product_detail)
app.add_url_rule('/product/create', "request",view_func=product_create, methods=['POST'])

# Category
app.add_url_rule('/category', view_func=category)
app.add_url_rule('/category/<float:pk>', view_func=category_detail)

# Admin
app.add_url_rule('/admin', view_func=admin)
