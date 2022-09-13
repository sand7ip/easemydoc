import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
from invoice_ocr import recognize_invoice

app=Flask(__name__)
## Load the model

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/ocr',methods=['POST'])
def ocr():
    invoice_ocr_path=request.form.get('filepath')
    #invoice_ocr_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output=recognize_invoice(invoice_ocr_path)
    return render_template("home.html",output_text="The Invocie output is {} ".format(output))
    



if __name__=="__main__":
    app.run(debug=True)