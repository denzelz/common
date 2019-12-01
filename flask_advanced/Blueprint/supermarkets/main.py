import os
import uuid
from flask import Blueprint, render_template, redirect, request, session
from werkzeug.utils import secure_filename
from db import DB
from form import SupermarketFilter, SupermarketForm

supermarkets = Blueprint('supermarkets', __name__, template_folder='templates', static_folder='static',
                         static_url_path='/Blueprint/supermarkets/static')

DB['supermarkets'] = []


@supermarkets.route('/add_supermarkets', methods=['GET', 'POST'])
def add_supermarkets():
    form = SupermarketForm()
    if form.validate_on_submit():
        form_data = {
            'id': str(uuid.uuid4()),
            'name': form.name.data,
            'location': form.location.data,
            'image': image_upload()
        }
        DB['supermarkets'].append(form_data)
        return redirect('/supermarkets')
    return render_template('add_supermarkets.html', form=form)


@supermarkets.route('/supermarkets', methods=['GET'])
def get_all_supermarkets():
    return render_template('all_supermarkets.html', supermarkets_list=DB['supermarkets'], form=SupermarketFilter())


@supermarkets.route('/supermarkets/<supermarket_id>', methods=['GET'])
def get_supermarket(supermarket_id):
    for item in DB['supermarkets']:
        if item['id'] == supermarket_id:
            session[supermarket_id] = 'True'
            return render_template('supermarket.html',
                                   name=item['name'],
                                   location=item['location'],
                                   sup_img=item['image'])


@supermarkets.route('/supermarkets', methods=['GET', 'POST'])
def location_filter():
    form = SupermarketFilter()
    location_list = []
    if form.validate_on_submit():
        for item in DB['supermarkets']:
            if item['location'] == str(form.location.data):
                location_list.append(item)
    return render_template('all_supermarkets.html', form=form, location_list=location_list)


def image_upload():
    if request.files['sup_img']:
        img = request.files['sup_img']
        path = os.path.join('Blueprint/supermarkets/static', secure_filename(img.filename))
        img.save(path)
        return secure_filename(img.filename)
    return 'no-image-icon.png'
