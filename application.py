from flask import Flask, render_template, request
from openpyxl import load_workbook

 
app = Flask(__name__)

@app.route('/')
def homepage():
    excel = load_workbook('task.xlsx')
    page = excel['Sheet']
    string = page['A']
    li = []
    for j in range(len(string)):
        li.append(string[j].value)
        
    return render_template('index.html', tovar = li)


@app.route('/add/', methods=["POST"])
def add():
    goods = request.form['good']
    excel = load_workbook('task.xlsx')
    page = excel.active
    m_row = page.max_row
    for i in range(1, m_row + 1):
        cell_obj = page.cell(row = i, column=1)
        cell_obj.value = goods
   
        

    excel.save('task.xlsx')
    return "<h1>Инвентарь пополнен</h1> <a href='/'>Домой</a>"



if __name__ == "__main__":
    app.run()


