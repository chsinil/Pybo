from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from pybo.navermovieapi import navermovie
from ..forms import NavermovieForm

bp = Blueprint('Navermovie', __name__, url_prefix='/Navermovie')

@bp.route('/navermovie/', methods=('GET','POST'))
def Navermovie():
    form = NavermovieForm()

    if request.method == "POST" and form.validate_on_submit():
        result = navermovie(form.search.data)
        print(result)
        return render_template('naver/navermovie.html', movieinfo_list=result['items'],form=form)

    return render_template('naver/navermovie.html',form=form)
