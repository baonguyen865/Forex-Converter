from forex_python.converter import CurrencyRates
from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import ConverterForm


app = Flask(__name__)

app.config["SECRET_KEY"] = 'bao865'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# connect_db(app)
toolbar = DebugToolbarExtension(app)


@app.route('/', methods=['GET', 'POST'])
def converting_form():
    form = ConverterForm()
    converted = 0
    if form.validate_on_submit():
        b = form.base_currency.data
        c = form.converted_currency.data
        amount = form.amount.data
        print(c)
        print(b)
        print(amount)
        rate = CurrencyRates()
        converted = rate.convert(b, c, amount)

    
    return render_template('base.html', form=form, converted=converted)



