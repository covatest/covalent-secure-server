from flask import Flask, request, render_template
import base64
app = Flask(__name__)

def convert_to_original(cd):
    return base64.b64decode(cd)

@app.route('/data_owner')
def data_owner_form():
    return render_template('data-owner-form.html')

@app.route('/data_owner', methods=['POST'])
def data_owner_post():
    text = request.form['Data Key']
    f=open('key.txt','w')
    f.write(text)
    return 'Data is logged'

@app.route('/model_trainer')
def model_trainer_form():
    return render_template('model-trainer-form.html')

@app.route('/model_trainer', methods=['POST'])
def model_trainer_post():
    f=open('data_hash.txt','w')
    f.write(request.form['Data Hash'])
    f=open('model_train.py','wb')
    f.write(convert_to_original(request.form['Code']))
    return 'Data is logged'
    

if __name__ == '__main__':
    app.run()