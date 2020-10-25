from flask import Blueprint, redirect, url_for
from flask_login import logout_user

blueprint = Blueprint('logout', __name__)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.home'))
