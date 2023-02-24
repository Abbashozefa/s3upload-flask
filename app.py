from flask import Flask,render_template,request
import boto3
from fileinput import filename

s3 = boto3.resource('s3')

app=Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload',methods=['POST','GET'])
def homepage():
    if request.method =='POST':
        for bucket in s3.buckets.all():
            print(bucket.name)
            b=str(bucket.name)

        f=request.files['file']
        f.save(f.filename)
        data = open(f.filename, 'rb')
        s3.Bucket(b).put_object(Key=f.filename, Body=data)
        

        return render_template('uploaded.html',name=f.filename)
    


if __name__=='__main__':
    app.run(debug=True)