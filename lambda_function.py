def dump_note_table():
    try:
        import boto3
        import psycopg2
        import json
        from datetime import datetime

        # Credentials
        DB_NAME = 'DB_NAME'
        DB_USER = 'DB_USER'
        DB_PASSWORD = 'DB_PASSWORD'
        DB_HOST = 'DB_HOST'
        DB_PORT = 0000
        AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
        AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
        AWS_STORAGE_BUCKET_NAME = 'AWS_STORAGE_BUCKET_NAME'
        DUMP_FOLDER = 'dump_folder/'

        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Execute SQL query to retrieve data
        cursor.execute("SELECT * FROM amazon_learning_note")

        # Fetch data
        data = cursor.fetchall()

        # Close database connection
        cursor.close()
        conn.close()

        data = [(item[0], item[1].isoformat(), item[2].isoformat(), item[3], item[4]) for item in data]
        # Convert list to JSON
        json_data = json.dumps(data)
        filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

        # Store data as JSON object in S3
        s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        s3.put_object(Bucket=AWS_STORAGE_BUCKET_NAME, Key=f'{DUMP_FOLDER}{filename}', Body=json.dumps(json_data))
        return True, ''
    except Exception as e:
        return False, f'{e}'


if __name__ == '__main__':
    dump_note_table()