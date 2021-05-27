from flask import Flask,render_template,request
from Caesar_cipher import *

app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html",page="home")
    pass


@app.route('/caesar-cipher',methods=['GET','POST'])
def caesarCipher():
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


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)