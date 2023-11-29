from datetime import datetime
import json
import pymysql

class MySql:
    def __init__(self, db_host, db_user, db_password, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
    
    def insert(self, body):
        # Connect to the database
        conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)
        # Create a cursor object
        cursor = conn.cursor()
        # Execute the SQL query
        cursor.execute("INSERT INTO " + body['model'] + " (" + ",".join(body['data'].keys()) + ") VALUES (" + ",".join(["%s"] * len(body['data'])) + ")", list(body['data'].values()))
        # Commit the changes
        conn.commit()
        # Close the connection
        conn.close()

    def mysql_update(self, body):
        # Connect to the database
        conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)
        # Create a cursor object
        cursor = conn.cursor()
        # Execute the SQL query
        cursor.execute("UPDATE " + body['model'] + " SET " + ",".join(["%s = %s"] * len(body['data'])) + " WHERE " + body['field'] + " = %s", list(body['data'].values()) + [body['value']])
        # Commit the changes
        conn.commit()
        # Close the connection
        conn.close()

    def mysql_delete(self, body):
        # Connect to the database
        conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)
        # Create a cursor object
        cursor = conn.cursor()
        # Execute the SQL query
        cursor.execute("DELETE FROM " + body['model'] + " WHERE " + body['field'] + " = %s", [body['value']])
        # Commit the changes
        conn.commit()
        # Close the connection
        conn.close()

    def mysql_get(body):
        # Connect to the database
        conn = pymysql.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'], database=body['database'])
        # Create a cursor object
        cursor = conn.cursor()
        # Execute the SQL query
        if body['field'] and body['value']:
            cursor.execute("SELECT * FROM " + body['model'] + " WHERE " + body['field'] + " = %s", [body['value']])
        else:
            cursor.execute("SELECT * FROM " + body['model'])
        # return result
        rows = cursor.fetchall()

        # Get column names from the description attribute
        columns = [col[0] for col in cursor.description]

        # Convert rows to dictionaries
        result_dicts = []
        for row in rows:
            result_dicts.append(dict(zip(columns, row)))

        # Close the connection
        conn.close()

        result = json.dumps(result_dicts)
        # bz compress result
        result = bz2.compress(result.encode("utf-8"))
        # Check if the compressed data is within 250 KB (250 * 1024 bytes)
        if len(result) > 250 * 1024:
            # Send the compressed data to SQS
            sqs = boto3.client('sqs')
            sqs.send_message(QueueUrl = os.environ['data_ingestion_queue'], MessageGroupId=body['site_id'], MessageBody = body)
            return  {
                'statusCode': 200,
                'body': 'successfully retrieved entry for '+body['model']+' table'
            }
        else:
            return  {
                'statusCode': 400,
                'body': 'Result too big for sqs message'
            }