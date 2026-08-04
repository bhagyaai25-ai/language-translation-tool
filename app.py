from flask import Flask,render_template,request
from deep_translator import GoogleTranslator
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    translated=" "
    if request.method=='POST':
        text=request.form['text']
        translated=GoogleTranslator(source='auto',target='kn').translate(text)
    return render_template('index.html',result=translated)
if __name__=='__main__':
    app.run(debug=True)