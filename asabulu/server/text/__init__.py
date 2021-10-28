
from flask import Blueprint

blueprint = Blueprint('text', __name__)

# http://localhost:5000/text/create
# http://localhost:5000/text/create?value=kkk
from .create import create as _create
@blueprint.route('/create', methods=['GET', 'POST'])
def create():
    return _create(**locals())

# http://localhost:5000/text/read/1
from .read import read as _read
@blueprint.route('/read/<int:id>', methods=['GET', 'POST'])
def read(id):
    return _read(**locals())

# http://localhost:5000/text/findall
# http://localhost:5000/text/findall?page=2&size=1
from .findall import findall as _findall
@blueprint.route('/findall', methods=['GET', 'POST'])
def findall():
    return _findall(**locals())

# http://localhost:5000/text/find
# http://localhost:5000/text/find?count_lower=400&value_like=k
from .find import find as _find
@blueprint.route('/find', methods=['GET', 'POST'])
def find():
    return _find(**locals())

# http://localhost:5000/text/update/1?count=40
from .update import update as _update
@blueprint.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    return _update(**locals())

# http://localhost:5000/text/delete/2
from .delete import delete as _delete
@blueprint.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    return _delete(**locals())