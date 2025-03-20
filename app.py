from flask import Flask, render_template, request  
from create_tables import create_DBtables
from data_loader import load_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def index():  
    result = ''  
    if request.method == 'POST':
		if students and rooms:
			students = request.form.get('students_path')  
			rooms = request.form.get('rooms_path')  
			result = load_data(students, rooms)
	return render_template('index.html', result=result)  

@app.route('/create_tables', methods=['POST'])  
def create_tables():  
    try:  
        create_DBtables()
        result = "Tables was created successfully!"  
        return result, 200  
    except Exception as e:
        return f"Error: {str(e)}", 500  

if __name__ == '__main__': 
    app.run(debug=True)


