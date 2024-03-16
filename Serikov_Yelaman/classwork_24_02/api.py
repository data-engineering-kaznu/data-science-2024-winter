from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api")
def get_data():
    data_to_show = []
    with open('database.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data_to_show.append([
                row[0],
                row[1],
                row[2],
            ])
    return data_to_show

@app.route("/api/add_record", methods = ['GET'])
def add_record():
    return render_template('add_record.html')

@app.route("/api/add_record", methods = ['POST'])
def post_data():
    year = request.form.get('year')
    region = request.form.get('region')
    price = request.form.get('price')
    with open('database.csv', 'a') as csv_file:
        csv_appender = csv.writer(csv_file)
        csv_appender.writerow([year, region, price + "\n"])
    return render_template('add_record.html')