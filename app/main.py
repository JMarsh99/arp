from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/',  methods=['GET'])
@login_required
def homepage():
    return render_template('homepage.html')
