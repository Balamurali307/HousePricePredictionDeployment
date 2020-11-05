from flask import Flask, request, render_template
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("hsepricepredict.pkl")
#model = joblib.load("model.pkl")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        posted_by  = request.form["posted_by"]
        print("posted_by :",posted_by)
        rera  = request.form["RERA"]
        print("RERA :",rera)
        BHK_NO  = request.form["BHK_NO"]
        print("BHK_NO :",BHK_NO)
        Square_Ft  = request.form["Square_Ft"]
        print("Square_Ft :",Square_Ft)
        Ready_to_Move  = request.form["Ready_to_Move"]
        print("Ready_to_Move :",Ready_to_Move)
        Longtitude  = request.form["Longtitude"]
        print("Longtitude :",Longtitude)
        Latitude  = request.form["Latitude"]
        print("Latitude :",Latitude)
        BHK_RK  = request.form["BHK_RK"]
        print("BHK_RK :",BHK_RK)

        df_ridge=pd.DataFrame([0,0,1,0,2,1300.236407,1,12.969910,77.597960,1])
        df_ridge
        df_ridge=df_ridge.transpose()
        df_ridge.columns=['POSTED_BY_Builder', 'POSTED_BY_Dealer', 'POSTED_BY_Owner', 'RERA',
       'BHK_NO.', 'SQUARE_FT', 'READY_TO_MOVE', 'LONGITUDE', 'LATITUDE',
       'BHK_RK']

        #houseprice = model.predict([[Square_Ft]])
        houseprice = model.predict(df_ridge)
        
    return render_template('index.html', prediction_text="House Price = {}".format(houseprice))
    
if __name__ == "__main__":
    app.run()
