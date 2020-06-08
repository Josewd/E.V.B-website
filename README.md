# Budget web application for

# a local delivery company

### Layout-page:
---

This web application is an idea for a local delivery company call E.V.B.

On this web page companys that want to contract E.V.B services can fill a budget form,

for that them can check first the prices for kilometers on this page containing a table of prices:
![prices_page.jpg](https://www.dropbox.com/s/qyake43wb1jo96y/prices_page.jpg?dl=0&raw=1)


and the budget form look like this:
![budget_page.jpg](https://www.dropbox.com/s/3bx6m4wc6ehqsmb/budget_page.jpg?dl=0&raw=1)

On clicking on the button send the budget form the company information will be saved

on a SQL database file where the information can be visualized either directly accessing

to the database file or on the page '/history' and searching the information by the name of the company:
![history_page.jpg](https://www.dropbox.com/s/mji4j2tjcio3xyq/history_page.jpg?dl=0&raw=1)
### code used:
---

To get data from the page and send to a SQL database file first on a application.py its import a SQL module from cs50 library and declared a variable called db that will receive our database file:

```
from cs50 import SQL

db = SQL('sqlite:///database.db')
```

using a Flask framework together with SQL module in python we can get information from the web page with this code:
```
@app.route('/orcamento', methods=["GET", "POST"])
def orcamento():

    session.clear()

    if request.method == "POST":
        if not request.form.get("company_name"):
            return render_template('apology.html')
        elif not request.form.get("email"):
            return render_template('apology.html')
        elif not request.form.get('collector'):
            return render_template('apology.html')
        elif not request.form.get("delivery"):
            return render_template('apology.html')
        elif not request.form.get("km"):
            return render_template('apology.html')


        new_user = db.execute("INSERT INTO companys (company,email, collect_adress, delivery_adress, price, km) VALUES (:company_name,:email,:collector,:delivery,:price, :km)", company_name=request.form.get("company_name"), email=request.form.get("email"), collector=request.form.get("collector"), delivery=request.form.get("delivery"),price=request.form.get("price"), km=request.form.get("km"))

        session['user_id'] = new_user



        return redirect("/")
    else:
        return render_template('orcamento.html')
```
and to access information from the database we follow the same logic:

```
@app.route('/history', methods=['GET', 'POST'])
def history():

    session.clear()

    if request.method == 'POST':
        if not request.form.get('company'):
            return render_template('apology.html')
        history = db.execute("SELECT company, collect_adress, delivery_adress, price, km, register_at FROM companys WHERE company = :company", company=request.form.get('company'))
        return render_template('history.html', history=history)
    else:
        return render_template('history.html')
```

## Build if:
---
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) Web framework.
* [Python](https://www.python.org/) Oriented object programming language.
* [Bootstrap](https://getbootstrap.com/) Open source SVG icon library.

## Author:
---
* ##### Jose Silva Junior 

## Liscense:
---
* [MT liscense](https://gist.github.com/Josewd/eb2785efb6d517fd52d8da3aa4152783)




