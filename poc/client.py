import phe as paillier
import json
from data import *
import os

def storeKeys():
    public_key, private_key = paillier.generate_paillier_keypair()
    keys = {}
    keys["public_key"] = {"n": public_key.n}
    keys["private_key"] = {"p": private_key.p, "q": private_key.q}
    with open("userkeys.json", "w") as file:
        json.dump(keys, file)


def getKeys():
    with open("userkeys.json", "r") as file:
        keys = json.load(file)
        pub_key = paillier.PaillierPublicKey(n=int(keys["public_key"]["n"]))
        priv_key = paillier.PaillierPrivateKey(
            pub_key, keys["private_key"]["p"], keys["private_key"]["q"]
        )
        return pub_key, priv_key


def serializeData(public_key, data):
    encrypted_data_list = [public_key.encrypt(x) for x in data]
    encrypted_data = {}
    encrypted_data["public_key"] = {"n": public_key.n}
    encrypted_data["values"] = [
        (str(x.ciphertext()), x.exponent) for x in encrypted_data_list
    ]
    serialized = json.dumps(encrypted_data)
    return serialized

def loadAnswer():
    with open("answer.json", "r") as file:
        ans = json.load(file)
        answer = json.loads(ans)
        return answer


storeKeys()
pub_key, priv_key = getKeys()
print("Key generated successfully!")
print("\tKey location: userkeys.json\n")

print("Now encrypting data...")
serializeData(pub_key, data)
datafile = serializeData(pub_key, data)
with open("data.json", "w") as file:
    json.dump(datafile, file)

print("Data encrypted successfully and is ready to be sent to server!")
print("Files created:\n\t data.json ")

