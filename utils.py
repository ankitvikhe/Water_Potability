import pickle
import pandas as pd
import numpy as np

class Water_Potability():

    def file_opening(self):
        with open("normalization.pkl","rb") as f:
            self.normalize = pickle.load(f)

        with open("Logistic_model.pkl","rb") as f:
            self.log_reg = pickle.load(f)

    def main_prediction(self,ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity):
        self.file_opening()
        test_array = np.zeros(9)

        test_array[0]=ph
        test_array[1]=Hardness
        test_array[2]=Solids
        test_array[3]=Chloramines
        test_array[4]=Sulfate
        test_array[5]=Conductivity
        test_array[6]=Organic_carbon
        test_array[7]=Trihalomethanes
        test_array[8]=Turbidity

        print("This is test array :",test_array)


        new_array = self.normalize.transform([test_array])
        print("This is normalized test array :",new_array)

        predict = self.log_reg.predict(new_array)
        print("*"*80)

        if predict[0]==0:
            print("The water is drinkable")
            return "The water is drinkable"

        else :
            print("The water is not drinkable")
            return "The water is not drinkable"

