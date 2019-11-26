import os
import uuid
from flask import Blueprint, render_template, redirect, request, session
from werkzeug.utils import secure_filename
from db import DB
from form import ProductForm, ProductFilter

products = Blueprint('products', __name__, template_folder='templates', static_folder='static',
                     static_url_path='/Blueprint/products/static')

DB['products'] = []


@products.route('/add_product', methods=['GET', 'POST'])
def add_products():
    form = ProductForm()
    if form.validate_on_submit():
        form_data = {
            'id': str(uuid.uuid4()),
            'name': form.product_name.data,
            'description': form.product_description.data,
            'image': image_upload(),
            'price': str(form.product_price.data)
        }
        DB['products'].append(form_data)
        return redirect('/products')
    return render_template('add_product.html', form=form)


@products.route('/products', methods=['GET'])
def get_all_products():
    return render_template('all_products.html', products_list=DB['products'], form=ProductFilter())


@products.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    for item in DB['products']:
        if item['id'] == product_id:
            session[product_id] = 'True'
            return render_template('product.html',
                                   name=item['name'],
                                   description=item['description'],
                                   product_img=item['image'],
                                   product_price=item['price'])


@products.route('/products', methods=['GET', 'POST'])
def price_filter():
    form = ProductFilter()
    price_filtered_list = []
    if form.validate_on_submit():
        for item in DB['products']:
            if item['price'] == str(form.product_price.data):
                price_filtered_list.append(item)
    return render_template('all_products.html', form=form, price_filtered_list=price_filtered_list)


def image_upload():
    if request.files['product_img']:
        img = request.files['product_img']
        path = os.path.join('Blueprint/products/static', secure_filename(img.filename))
        img.save(path)
        return secure_filename(img.filename)
    return 'no-image-icon.png'

