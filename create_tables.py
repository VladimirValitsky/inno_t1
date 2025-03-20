import constants as const
from db_connection import schema, connection
from sqlalchemy import text

# Table names
table_students = const.TABLE_STUDENTS
table_rooms = const.TABLE_ROOMS

# Create Schema if not exist
create_schema_query = f"""
CREATE SCHEMA IF NOT EXISTS {schema};
"""
create_rooms_query = f"""
CREATE TABLE IF NOT EXISTS {schema}.{table_rooms} (
    id SERIAL PRIMARY KEY,  
    name VARCHAR(100) NOT NULL
);
"""
create_students_query = f"""
CREATE TABLE IF NOT EXISTS {schema}.{table_students} (  
        birthday TIMESTAMP NOT NULL,
        id SERIAL PRIMARY KEY,  
        name VARCHAR(100) NOT NULL,  
        room INTEGER NOT NULL REFERENCES {schema}.{table_rooms}(id),  
        sex CHAR(1) CHECK (sex IN ('M', 'F'))  
);
"""

# Add index for optimization
add_room_index = f"""
CREATE INDEX idx_students_room ON {schema}.{table_students}(room);
"""
add_birthday_index = f"""
CREATE INDEX idx_students_birthday ON {schema}.{table_students}(birthday);
"""

try:
    connection.execute(text(create_schema_query))
    connection.execute(text(create_rooms_query))
    connection.execute(text(create_students_query))
    connection.execute(text(add_room_index))
    connection.execute(text(add_birthday_index))
    connection.commit()

except Exception as creation_error:
    print(f'Error: during metadata creation: {creation_error}')
