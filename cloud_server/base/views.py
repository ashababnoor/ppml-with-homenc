from django.shortcuts import render
from django.http import HttpResponse
import phe as paillier
from .algorithms import LinearModel
import json 


# Create your views here.

def runModel():
    cof = LinearModel().getCoef()
    print("The trained weights are: \n", cof)


def getData(datafile):
    with open(datafile, "r") as file:
        d = json.load(file)
    data = json.loads(d)
    return data


def computeData(datafile):
    data = getData(datafile)
    mycoef = LinearModel().getCoef()
    pk = data["public_key"]
    pubkey = paillier.PaillierPublicKey(n=int(pk["n"]))
    enc_nums_rec = [
        paillier.EncryptedNumber(pubkey, int(x[0], int(x[1]))) for x in data["values"]
    ]
    results = sum([mycoef[i] * enc_nums_rec[i] for i in range(len(mycoef))])
    return results, pubkey


def serializeData(datafile):
    results, pubkey = computeData(datafile)
    encrypted_data = {}
    encrypted_data["pubkey"] = {"n": pubkey.n}
    encrypted_data["values"] = (str(results.ciphertext()), results.exponent)
    serialized = json.dumps(encrypted_data)
    return serialized


def server(request):
    datafile = request.data
    runModel()
    datacontents = serializeData(datafile)
    with open("answer.json", "w") as file:
        json.dump(datacontents, file)
    print("Result generated successfully!")
    return HttpResponse(datacontents)
    