from flask import Flask,render_template,request

from Caesar_cipher import *
from monoalphabetic_cipher import *
from polyalphabetic_cipher import *
from playfair_cipher import *
from rail_fence_cipher import *
from row_transposition_cipher import *


app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html",page="home")
    pass


@app.route('/caesar-cipher',methods=['GET','POST'])
def caesar_cipher():
    encData = {}
    decData = {}
    bruteForceData = {}
    if (request.form):
        if request.form['submitButton']=="Encrypt":

            plain_text=request.form["plainText"]
            key = int(request.form["key"])
            encData = caesar_cipher_enc(plain_text,key)
            pass

        elif request.form['submitButton'] == 'Decrypt':

            cipher_text=request.form["cipherText"]
            if request.form['key'] != "":

                key = int(request.form["key"])
                decData = caesar_cipher_dec(cipher_text,key)
                pass

            else:
                cipher_text=request.form["cipherText"]
                bruteForceData = caesar_cipher_brute_force(cipher_text)
                pass


        elif request.form ['submitButton'] == 'Brute Force':
           
            cipher_text=request.form["cipherText"]
            bruteForceData = caesar_cipher_brute_force(cipher_text)
            pass

        pass
    print(encData)
    print(decData)
    print(bruteForceData)
    return render_template("caesar-cipher.html",bruteForceData=bruteForceData,decData=decData,encData=encData,page = "caesar-cipher")   
    pass

@app.route('/monoalphabetic-cipher',methods=['GET','POST'])
def monoalphabetic_cipher():
    encData = {}
    decData = {}


    key = "qazwsxedcrfvtgbyhnujmikolp"
    key = key.upper()


    if (request.form):
        if request.form['submitButton']=="Encrypt":
            
            plain_text=request.form["plainText"]
            
            keyList = []
            for i in range(26):
                keyList.append(request.form["key"+str(i)])

            key = "".join(keyList)
            encData = monoalphabetic_cipher_enc(plain_text,key)
            print(encData)
            pass
        elif request.form['submitButton'] == 'Decrypt':

            cipher_text=request.form["cipherText"]
            keyList = []
            for i in range(26):
                keyList.append(request.form["key"+str(i)])

            key = "".join(keyList)
            decData = monoalphabetic_cipher_dec(cipher_text,key)
            print(decData)
            pass
    return render_template("monoalphabetic-cipher.html",key = key,decData=decData,encData=encData,page = "monoalphabetic-cipher")   
    pass


@app.route('/polyalphabetic-cipher',methods=['GET','POST'])
def polyalphabetic_cipher():
    encData = {}
    decData = {}

    if (request.form):
        if request.form['submitButton']=="Encrypt":

            plain_text=request.form["plainText"]
            key = list(request.form["key"])

            new_key = []
            for i in key:
                new_key.append(int(i))

            encData = polyalphabetic_cipher_enc(plain_text,new_key)
            pass

        elif request.form['submitButton'] == 'Decrypt':

            cipher_text=request.form["cipherText"]
            key = list(request.form["key"])
            
            new_key = []
            for i in key:
                new_key.append(int(i))
           
            decData = polyalphabetic_cipher_dec(cipher_text,new_key)
            pass

        pass
    print(encData)
    print(decData)
    return render_template("polyalphabetic-cipher.html",decData=decData,encData=encData,page = "polyalphabetic-cipher")   
    pass

@app.route('/vigenère-cipher',methods=['GET','POST'])
def vigenère_cipher():
    encData = {}
    decData = {}

    if (request.form):
        if request.form['submitButton']=="Encrypt":

            plain_text=request.form["plainText"]
            key = request.form["key"]
            key = key.lower()
            new_key = []
            for i in key:
                if(i.isdigit()):    
                    new_key.append(int(i))
                else:
                    new_key.append(ord(i)-ord('a'))

            encData = polyalphabetic_cipher_enc(plain_text,new_key)
            encData['key'] = key
            encData['new_key'] = new_key

            print(encData)
            pass

        elif request.form['submitButton'] == 'Decrypt':

            cipher_text=request.form["cipherText"]
            key = request.form["key"]
            
            key = key.lower()
            new_key = []
            for i in key:
                if(i.isdigit()):    
                    new_key.append(int(i))
                else:
                    new_key.append(ord(i)-ord('a'))
            decData = polyalphabetic_cipher_dec(cipher_text,new_key)
          
            decData['key'] = key
            decData['new_key'] = new_key
           
            pass

        pass
    print(encData)
    print(decData)
    return render_template("vigenère-cipher.html",decData=decData,encData=encData,page = "vigenère-cipher")   
    pass

@app.route('/playfair-cipher',methods=['GET','POST'])
def playfair_cipher():
    encData = {}
    decData = {}

    if (request.form):
        if request.form['submitButton']=="Encrypt":

            plain_text=request.form["plainText"]
            key = request.form["key"]

            encData = play_fair_enc(plain_text,key)

            pass

        elif request.form['submitButton'] == 'Decrypt':

            cipher_text=request.form["cipherText"]
            key = request.form["key"]

            decData = play_fair_dec(cipher_text,key)
           
            pass

        pass
    print(encData)
    print(decData)
    return render_template("playfair-cipher.html",decData=decData,encData=encData,page = "playfair-cipher")   
    pass


@app.route('/row-transposition-cipher',methods=['GET','POST'])
def row_transposition_cipher():
    encData = {}
    decData = {}

    if (request.form):
        if request.form['submitButton']=="Encrypt":

            plain_text=request.form["plainText"]
            key = request.form["key"]

            encData = row_transposition_enc(plain_text,key)

            pass

        elif request.form['submitButton'] == 'Decrypt':

            cipher_text=request.form["cipherText"]
            key = request.form["key"]

            decData = row_transposition_dec(cipher_text,key)
           
            pass

        pass
    print(encData)
    print(decData)
    return render_template("row-transposition-cipher.html",decData=decData,encData=encData,page = "row-transposition-cipher")   
    pass


@app.route('/rail-fence-cipher',methods=['GET','POST'])
def rail_fence_cipher():
    encData = {}
    decData = {}

    if (request.form):
        if request.form['submitButton']=="Encrypt":

            plain_text=request.form["plainText"]
            key = int(request.form["key"])
            subtype = request.form["subtype"]

            print(subtype)
            encData = rail_fence_enc(plain_text,key,subtype=subtype)

            pass

        elif request.form['submitButton'] == 'Decrypt':

            cipher_text=request.form["cipherText"]
            key = int(request.form["key"])
            subtype = request.form["subtype"]

            

            decData = rail_fence_dec(cipher_text,key,subtype)
           
            pass

        pass
    print(encData)
    print(decData)
    return render_template("rail-fence-cipher.html",decData=decData,encData=encData,page = "rail-fence-cipher")   
    pass

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)