from db_connection import engine, schema
import constants as const

# Table names
table_students = const.TABLE_STUDENTS
table_rooms = const.TABLE_ROOMS


# List of rooms and number of students in each of them
query1 = f"""  
    SELECT r.id, r.name, COUNT(s.id) AS students_count  
    FROM {schema}.{table_rooms} r  
    LEFT JOIN {schema}.{table_students} s ON r.id = s.room  
    GROUP BY r.id, r.name  
    ORDER BY r.id;  
    """

# 5 rooms with the lowest average age of students
query2 = f"""  
    SELECT r.id, r.name, AVG(EXTRACT(YEAR FROM AGE(s.birthday))) as avg_students_age 
    FROM {schema}.{table_rooms} r  
    LEFT JOIN {schema}.{table_students} s ON r.id = s.room  
    GROUP BY r.id, r.name  
    ORDER BY avg_students_age
    LIMIT 5;  
    """

# 5 rooms with the largest age difference between students
query3 = f"""  
    SELECT r.id, r.name, 
    MAX(EXTRACT(YEAR FROM AGE(s.birthday))) - MIN(EXTRACT(YEAR FROM AGE(s.birthday))) 
    as age_delta 
    FROM {schema}.{table_rooms} r  
    LEFT JOIN {schema}.{table_students} s ON r.id = s.room  
    GROUP BY r.id, r.name 
    HAVING COUNT(s.id) > 0
    ORDER BY age_delta DESC
    LIMIT 5;  
    """
# List of rooms with mixed-sex students
query4 = f"""  
    SELECT r.id, r.name
    FROM {schema}.{table_rooms} r  
    LEFT JOIN {schema}.{table_students} s ON r.id = s.room  
    GROUP BY r.id, r.name 
    HAVING COUNT(distinct s.sex) = 2
    ORDER BY r.id; 
    """

# Query dictionaty by result filename
# Query dictionaty keys: returned fields / values: queries
filename2query_dict = {
    'students_count': {('id', 'name', 'students_count'): query1},
    'avg_students_age': {('id', 'name', 'avg_students_age'): query2},
    'large_diff_students_age': {('id', 'name', 'age_delta'): query3},
    'mixed_rooms': {('id', 'name'): query4}
}