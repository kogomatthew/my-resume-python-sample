from flask import Flask, render_template, request, redirect 
import csv 
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html') 

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name) 

@app.route('/submit_form', methods=['POST', 'GET'] )
def submit_form():
    # et form data
    if request.method == 'POST':

        try :

            data = request.form.to_dict() 
            email = data['email']
            subject = data['subject']
            message = data['message'] 
            full_name = data['full_name']

            write_to_csv(data)
        except :
            return 'did not save to database'
        # save to db
        
        return render_template('/thankyou.html' , full_name=full_name)  
    else:
        return 'something went wrong. Try again!'
    
# def write_to_db(dict):
#     with open('database.txt', mode='a') as database :
#         database.write('Full Name : '  + dict['full_name'])
        
def write_to_csv(dict1):
    with open('database.csv', mode='a') as database2 :
      
        #  add header
        fieldnames = ['full_name', 'email', 'message']
        writer = csv.DictWriter(database2, fieldnames=fieldnames)
        writer.writeheader()
        # add data

        writer.writerow({'full_name': dict1['full_name'], 'email': dict1['email'], 'message': dict1['message']}) 
