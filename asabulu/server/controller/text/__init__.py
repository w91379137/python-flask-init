
from flask import Blueprint

api = Blueprint('text', __name__)

from .create import create as _create
@api.route('/create', methods=['GET', 'POST'])
def create():
    return _create(**locals())

from .read import read as _read
@api.route('/read/<int:id>', methods=['GET', 'POST'])
def read(id):
    return _read(**locals())

from .findall import findall as _findall
@api.route('/findall', methods=['GET', 'POST'])
def findall():
    return _findall(**locals())

from .find import find as _find
@api.route('/find', methods=['GET', 'POST'])
def find():
    return _find(**locals())

from .update import update as _update
@api.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    return _update(**locals())

from .delete import delete as _delete
@api.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    return _delete(**locals())