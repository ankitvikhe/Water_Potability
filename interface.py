from flask import Flask,request,render_template,jsonify
from utils import Water_Potability

app = Flask(__name__)
WP = Water_Potability()


@app.route("/",methods = ["GET","POST"])
def prediction():
    data = request.form

    ph = float(data["ph"])
    print(ph)
    Hardness = float(data["Hardness"])
    Solids = float(data["Solids"])
    Chloramines = float(data["Chloramines"])
    Sulfate = float(data["Sulfate"])
    Conductivity = float(data["Conductivity"])
    Organic_carbon = float(data["Organic_carbon"])
    Trihalomethanes = float(data["Trihalomethanes"])
    Turbidity = float(data["Turbidity"])

    

    Potability = WP.main_prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity) 

    # print(Potability)
    return f"{Potability}"

if __name__ == "__main__":
    app.run()