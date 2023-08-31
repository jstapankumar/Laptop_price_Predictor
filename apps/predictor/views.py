from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pickle
import numpy as np
import os
from apps.settings import BASE_DIR


# Load the model and data frame from the same directory
pipe = pickle.load(open(os.path.join(BASE_DIR, 'predictor', 'pipe.pkl'), 'rb'))
df = pickle.load(open(os.path.join(BASE_DIR, 'predictor', 'df.pkl'), 'rb'))


'''
    Company = models.CharField(max_length=100)
    TypeName = models.CharField(max_length=100)
    Ram = models.IntegerField()
    Weight = models.FloatField()
    Touchscreen = models.IntegerField()
    Ips = models.IntegerField()
    ppi = models.IntegerField()
    Cpu_brand = models.CharField(max_length=100)
    HDD = models.IntegerField()
    SSD = models.IntegerField()
    Gpu_brand = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
'''
# Create your views here.

# predict post request
@api_view(['POST'])
def predict(request):
    # get the data from the request
    # parse the data to get the features
    parsed_data = request.data
    Company = parsed_data['company']
    TypeName = parsed_data['typename']
    Ram = parsed_data['ram']
    Weight = parsed_data['weight']
    Touchscreen = parsed_data['touch_screen']
    Resolution = parsed_data['resolution']
    Ips = parsed_data['ips']
    Inches = parsed_data['inches']
    Cpu_brand = parsed_data['cpu_brand']
    HDD = parsed_data['HDD']
    SSD = parsed_data['SSD']
    Gpu_brand = parsed_data['gpu_brand']
    os = parsed_data['os']

    # convert to their respective data types
    Ram = int(Ram)
    Weight = float(Weight)
    Touchscreen = int(Touchscreen)
    Ips = int(Ips)
    Inches = float(Inches)
    HDD = int(HDD)
    SSD = int(SSD)
    
    # Get ppi
    splitted = Resolution.split('x')
    ppi = (int(splitted[0]) ** 2 + int(splitted[1]) ** 2) ** 0.5 / Inches
    
    # predict the price
    query = [[Company, TypeName, Ram, Weight, Touchscreen, Ips, ppi, Cpu_brand, HDD, SSD, Gpu_brand, os]]
    
    log_price = pipe.predict(query)[0]
    price = np.exp(log_price)
    
    # print(query)
    
    # return the response
    return Response({'price': int(price)}, status=status.HTTP_200_OK)
    
# get all unique values for each feature
@api_view(['GET'])
def unique_list(request):
    # get the unique values
    companies = df['Company'].unique()
    ram = df['Ram'].unique()
    types = df['TypeName'].unique()
    cpus = df['Cpu brand'].unique()
    gpus = df['Gpu brand'].unique()
    os = df['os'].unique()
    
    # return the response
    return Response({'companies': companies.tolist(), 'ram': ram.tolist(), 'types': types.tolist(), 'cpus': cpus.tolist(), 'gpus': gpus.tolist(), 'os': os.tolist()}, status=status.HTTP_200_OK)
    

    
    
    

