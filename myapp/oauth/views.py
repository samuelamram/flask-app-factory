from flask import Blueprint, jsonify

oauth_bp = Blueprint('oauth', __name__)


@oauth_bp.route('/')
def oauth_index():
    return jsonify({'test': 'oauth'})
