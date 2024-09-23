from flask import Blueprint, render_template, request, jsonify

from board.core.save_employee import save_employee
from board.core.get_employees import get_employees


bp = Blueprint("pages", __name__)

@bp.route("/", methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")

       _save_employee = save_employee(first_name, last_name)
       _save_employee.save_employee()

       _get_employees = get_employees(first_name)

       _df_employees = _get_employees.get_employees()

       print(_df_employees)

       _dict_employees = _df_employees.to_dict('records')

       return render_template("pages/list_of_employees.html", employees=_dict_employees)

    return render_template("pages/home.html")


@bp.route("/about", methods =["GET", "POST"])
def indexhh():
    print('Ciaoooo Ajax')
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        output = firstname + lastname

        print('Ciaoooo Ajax22222222222')

        _get_employees = get_employees(firstname)

        _df_employees = _get_employees.get_employees_by_name()

        print(_df_employees)

        _dict_employees = _df_employees.to_dict('records')

        print(_dict_employees)

        if firstname: # and lastname:
            return jsonify(_dict_employees) #jsonify({'output':'Your Name is ' + output + ', right?'})
        return jsonify({'error' : 'Error!'})
    return render_template('pages/about.html')


@bp.route("/search", methods =["GET", "POST"])
def search():
    if request.method == "POST":

        dataopen = [
            {
                'name': 'Audrinop',
                'place': 'kakaop',
                'mob': '7736op'
            },
            {
                'name': 'Stuvard',
                'place': 'Goa',
                'mob': '546464'
            }
        ]

        dataclose = [
            {
                'name': 'Audrincl',
                'place': 'kaka',
                'mob': '7736'
            },
            {
                'name': 'Stuvardcl',
                'place': 'Goa',
                'mob': '546464'
            }
        ]

        if "open" in request.form:
            print('Holaaaaa search open')
            return  render_template("pages/search.html", dataopen=dataopen)
        elif "close" in request.form:
            print('Holaaaaa search close')
            return  render_template("pages/search.html", dataopen=dataclose)

        print('Ciaoooo search')
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")

        _get_employees = get_employees(first_name)

        _df_employees = _get_employees.get_employees_by_name()

        print(_df_employees)

        _dict_employees = _df_employees.to_dict('records')

        return render_template("pages/search.html", employees=_dict_employees)

    return render_template("pages/search.html")


