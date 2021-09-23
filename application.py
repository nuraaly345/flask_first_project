from flask import Flask, render_template
from openpyxl import load_workbook


 
app = Flask(__name__)

@app.route('/')
def homepage():
    excel = load_workbook('task.xlsx')
    page = excel['Sheet']
    good = [page['A1'].value, page['A2'].value, page['A3'].value, page['A4'].value]
    return render_template('index.html', tovar = good)

if __name__ == "__main__":
    app.run()