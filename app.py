"""  
This Flask web application provides an interface for loading and uploading data   
to a database. It consists of three main functionalities:   
1. Creating tables in the database. 
2. Loading data from specified file paths for students and rooms.
3. Uploading data in JSON or XML formats.

The application routes are defined for handling these operations, and responses are   
returned based on the success or failure of each operation.  
"""  
from flask import Flask, render_template, request  
from create_tables import create_DBtables
from data_loader import load_data
from upload_data import data_upload

app = Flask(__name__)  

# Creating tables in the database
@app.route('/create_tables', methods=['POST'])  
def create_tables():  
    try:  
        create_DBtables()
        result = "Tables was created successfully!"  
        return result, 200  
    except Exception as e:
        return f"Error: {str(e)}", 500

# Loading data from specified file paths for students and rooms
@app.route('/', methods=['POST'])  
def index():  
    result = ''  
    if request.method == 'POST':  
        students = request.form.get('students_path')  
        rooms = request.form.get('rooms_path')       
        if students and rooms:  
            result = load_data(students, rooms)  
    return render_template('index.html', result=result) 

#Uploading data in JSON or XML formats
@app.route('/upload_data', methods=['POST'])  
def upload_data():  
    try:  
        file_format = request.form.get('file_format')   
        if file_format:  
            result = data_upload(file_format) 
        return result, 200  
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__': 
    app.run(debug=True)