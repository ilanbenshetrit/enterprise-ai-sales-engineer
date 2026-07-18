import sqlite3



class Database:


    def __init__(
        self,
        db_name="sales_engineer.db"
    ):

        self.connection = sqlite3.connect(
            db_name,
            check_same_thread=False
        )


        self.create_tables()



    def create_tables(
        self
    ):

        cursor = self.connection.cursor()



        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS customers
            (
                id TEXT PRIMARY KEY,
                name TEXT,
                industry TEXT,
                size TEXT,
                created_at TEXT
            )
            """
        )



        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS opportunities
            (
                id TEXT PRIMARY KEY,
                customer_id TEXT,
                title TEXT,
                description TEXT,
                created_at TEXT
            )
            """
        )



        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS opportunity_intelligence
            (
                id TEXT PRIMARY KEY,
                opportunity_id TEXT,

                analysis TEXT,
                solution TEXT,
                poc_plan TEXT,
                implementation_plan TEXT,
                demo_plan TEXT,
                proposal TEXT,

                created_at TEXT
            )
            """
        )



        self.connection.commit()



    def execute(
        self,
        query,
        params=()
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            query,
            params
        )


        self.connection.commit()


        return cursor



    def fetch_all(
        self,
        query,
        params=()
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            query,
            params
        )


        return cursor.fetchall()



    def fetch_one(
        self,
        query,
        params=()
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            query,
            params
        )


        return cursor.fetchone()