import json
import xml.etree.ElementTree as et
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from db_connection import engine, schema
import constants as const
import queries as qrs
import os

# Table names
table_students = const.TABLE_STUDENTS
table_rooms = const.TABLE_ROOMS

def fetch_data(query):
    with Session(engine) as session:
        result = session.execute(text(query))
        return result.fetchall()

def get_json_data():
    data1 = fetch_data(qrs.query1)
    data_json1 = [{'id': r[0], 'name': r[1], 'students_count': int(r[2])} for r
                  in data1]
    data2 = fetch_data(qrs.query2)
    data_json2 = [{'id': r[0], 'name': r[1], 'avg_students_age': float(r[2])}
                  for r in data2]
    data3 = fetch_data(qrs.query3)
    data_json3 = [{'id': r[0], 'name': r[1], 'age_delta': float(r[2])} for r in
                  data3]
    data4 = fetch_data(qrs.query4)
    data_json4 = [{'id': r[0], 'name': r[1]} for r in data4]

    filename2jsonfile = {
        const.FILENAME_STUD_COUNT: data_json1,
        const.FILENAME_AVG_STUD_AGE: data_json2,
        const.FILENAME_DIFF_STUD_AGE: data_json3,
        const.FILENAME_MIXED_ROOMS: data_json4
    }
    return filename2jsonfile

def save_as_json(format, json_data):
    for filename, data_json in json_data.items():
        file = f'{const.PATH_RESULTS}{filename}.{format}'
        with open(file, 'w') as json_file:
            json.dump(data_json, json_file, indent=4)

def save_as_xml(format, json_data):
    for filename, data_json in json_data.items():
        file = f'{const.PATH_RESULTS}{filename}.{format}'

        root = et.Element('results')
        for row in data_json:
            item_element = et.SubElement(root, 'item')
            for index, value in row.items():
                et.SubElement(item_element, index).text = str(value)
        tree = et.ElementTree(root)
        tree.write(file, xml_declaration=True, encoding='utf-8')

def check_results_folder():
    if not os.path.exists(const.FOLDER_RESULTS):
        os.makedirs(const.FOLDER_RESULTS)

def main():
    check_results_folder()

    # Ask user to choose saving format
    format_choice = input("Choose data saving format (json or xml): ").strip().lower()

    if format_choice == 'json':
        save_as_json(format_choice, get_json_data())
    elif format_choice == 'xml':
        save_as_xml(format_choice, get_json_data())
    else:
        print("Wrong data saving format. Try again")

if __name__ == '__main__':
    main()