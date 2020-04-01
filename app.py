from flask import Flask, render_template, request
import os
import pickle
import pandas as pd
import re
import numpy as np 

app = Flask(__name__)
data = pd.read_csv('index.csv')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search/results', methods=['GET','POST'])
def request_search():
    import csv
    data = []
    with open('index.csv') as csv_file:
        file_data = csv.reader(csv_file, delimiter=',')
        for row in file_data:
            data.append({
            "title": row[0],
            "abstract": row[1],
            # "publish_time": row[2],
            "authors": row[3],
            "url":row[4]
            })
    

    return render_template('results.html', data=data)

if __name__ == "__main__":
    app.run('127.0.0.1')
