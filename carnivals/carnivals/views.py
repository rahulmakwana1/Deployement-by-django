from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pickle 


def home(request):
    return render(request, 'predict.html')

def predict(request):

    pickle_in = open("model.pkl", "rb")
    model = pickle.load(pickle_in)

    model_prediction = []

    model_prediction.append(request.GET['Stall_no'])
    model_prediction.append(request.GET['Market_Category'])
    model_prediction.append(request.GET['Loyalty_customer'])
    model_prediction.append(request.GET['Product_Category'])
    model_prediction.append(request.GET['Grade'])
    model_prediction.append(request.GET['Demand'])
    model_prediction.append(request.GET['Discount_avail'])
    model_prediction.append(request.GET['charges_1'])
    model_prediction.append(request.GET['charges_2'])
    model_prediction.append(request.GET['Maximum_price'])
        #pred_args = [Stall_no, Market_Category, Loyalty_customer, Product_Category, Grade, Demand, Discount_avail,charges_1, charges_2, Maximum_price]
        #pred_args_arr = np.array(pred_args)
        #pred_args_arr = pred_args_arr.reshape(1, -1) 
    model_prediction = model.predict([model_prediction])
    print(model_prediction)
    return render(request,'result.html',{'model_prediction':model_prediction})


'''from django.http import HttpResponse
from django.shortcuts import render
import pickle 
import numpy as np

def home(request):
    return render(request, 'predict.html')

def predict(request):

    pickle_in = open("model.pkl", "rb")
    model = pickle.load(pickle_in)

    model_prediction = []

    if request.method == 'POST':

        Stall_no = float(request.form['Stall_no'])
        Market_Category = float(request.form['Market_Category'])
        Loyalty_customer = float(request.form['Loyalty_customer'])
        Product_Category = float(request.form['Product_Category'])
        Grade = float(request.form['Grade'])
        Demand = float(request.form['Demand'])
        Discount_avail = float(request.form['Discount_avail'])
        charges_1 = float(request.form['charges_1'])
        charges_2 = float(request.form['charges_2'])
        Maximum_price = float(request.form['Maximum_price'])
        pred_args = [Stall_no, Market_Category, Loyalty_customer, Product_Category, Grade, Demand, Discount_avail,
                    charges_1, charges_2, Maximum_price]
        pred_args_arr = np.array(pred_args)
        pred_args_arr = pred_args_arr.reshape(1, -1) 
        model_prediction = model.predict([pred_args_arr])
    
    return render(request,'result.html',{'model_prediction':model_prediction})
'''
