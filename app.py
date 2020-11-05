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
        postedbybuilder=postedbydealer=postedbyowner=0
        
        if posted_by=='Builder':
            postedbybuilder=1
        elif posted_by=='Dealer':
            postedbydealer=1
        else:
            postedbyowner=1
         
        
        print("posted_by Builder {0} Dealer {1} Owner {2}:",postedbybuilder,postedbydealer,postedbyowner)
        
        rera  = request.form["RERA"]
        reranum=0
        if rera=='Yes':
            reranum=1
        
        
        print("RERA :",rera)
        BHK_NO  = int(request.form["BHK_NO"])
        print("BHK_NO :",BHK_NO)
        
        Square_Ft  = int(request.form["Square_Ft"])
        print("Square_Ft :",Square_Ft)
        
        Ready_to_Move  = request.form["Ready_to_Move"]
        
        readytomove=0
        if Ready_to_Move=='Yes':
            readytomove=1
        
        print("Ready_to_Move :",Ready_to_Move)
        
        Longtitude  = float(request.form["Longtitude"])
        print("Longtitude :",Longtitude)
        
        Latitude  = float(request.form["Latitude"])
        print("Latitude :",Latitude)
        
        BHK_RK  = int(request.form["BHK_RK"])
        print("BHK_RK :",BHK_RK)
        
        
        

        #df_ridge=pd.DataFrame([0,0,1,0,2,1300.236407,1,12.969910,77.597960,1])
        df_ridge=pd.DataFrame([postedbybuilder,postedbydealer,postedbyowner,reranum,BHK_NO,Square_Ft,readytomove,Longtitude,Latitude,BHK_RK])
        
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
