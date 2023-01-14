from model import LinearModel
import phe as paillier
import json


def getData(filename):
    with open(filename, "r") as file:
        d = json.load(file)
    data = json.loads(d)
    return data


def computeData(filename):
    data = getData(filename)
    mycoef = LinearModel().getCoef()
    pk = data["public_key"]
    pubkey = paillier.PaillierPublicKey(n=int(pk["n"]))
    enc_nums_rec = [
        paillier.EncryptedNumber(pubkey, int(x[0], int(x[1]))) for x in data["values"]
    ]
    print("Enc Nums Rec:\n", enc_nums_rec)
    
    results = sum([mycoef[i] * enc_nums_rec[i] for i in range(len(mycoef))])
    return results, pubkey


def serializeData(filename):
    results, pubkey = computeData(filename)
    encrypted_data = {}
    encrypted_data["pubkey"] = {"n": pubkey.n}
    encrypted_data["values"] = (str(results.ciphertext()), results.exponent)
    serialized = json.dumps(encrypted_data)
    return serialized


# print(sum([data[i] * mycoef[i] for i in range(len(data))]))


def main():
    datafile = serializeData("enc_data/data_1.json")
    with open("answer.json", "w") as file:
        json.dump(datafile, file)
    print("Result generated successfully!")


if __name__ == "__main__":
    main()
