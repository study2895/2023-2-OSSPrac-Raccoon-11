from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('main.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['University']=request.form.get('University')
        result['Major']=request.form.get('Major')
        domainlist = request.form.get('domainlist')
        domaintxt = request.form.get('domaintxt')
        if domainlist != 'type': 
            result['Email'] = f'{domaintxt}@{domainlist}'
        else:
            result['Email'] = '오류입니다.'
        result['Gender']=request.form.get('Gender')
        checkbox_values = request.form.getlist('Programming Languages')
        result['Programming Languages'] = ', '.join(checkbox_values)
        return render_template('result.html',result=result)
        


if __name__ =='__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
