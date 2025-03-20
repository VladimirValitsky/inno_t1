import pandas as pd
import constants as const
from db_connection import connection, schema
from io import StringIO


# Default Path to files
default_students_path = const.JSON_STUDENTS_PATH
default_rooms_path = const.JSON_ROOMS_PATH

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return pd.read_json(StringIO(file_content))



def load_data(students_file_path, rooms_file_path):
    result_message = ''
    input_student_file_path = students_file_path.strip().lower()
    input_rooms_file_path = rooms_file_path.strip().lower()

    if input_student_file_path == 'd':
        student_path = default_students_path
    else:
        student_path = input_student_file_path

    if input_rooms_file_path == 'd':
        rooms_path = default_rooms_path
    else:
        rooms_path = input_rooms_file_path

    try:
        # Read JSON files to DataFrame
        df_students = read_json_file(student_path)
        df_rooms = read_json_file(rooms_path)

        try:
            # Load data to DB
            df_rooms.to_sql(const.TABLE_ROOMS, con=connection, schema=schema, if_exists='append', index=False)
            df_students.to_sql(const.TABLE_STUDENTS, con=connection, schema=schema,
                            if_exists='append', index=False)
            print("Data successfully loaded from JSON to db tables")
            result_message = "Data successfully loaded from JSON to db tables"

        except Exception as loading_error:
            print(f'Error: during loading data: {loading_error}')
            result_message = f'Error: during loading data: {loading_error}'

    except Exception as reading_error:
        print(f'Error: File path is invalid. Choose correct one.')
        result_message = f'Error: File path is invalid. Choose correct one.'
    return result_message



