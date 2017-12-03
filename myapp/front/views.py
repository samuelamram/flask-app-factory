from flask import Blueprint, jsonify

bp = Blueprint('bp', __name__)


@bp.route('/')
def index():
    return jsonify({'test': 'test'})
