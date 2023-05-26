from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
       self.id = None
       self.name = name
       self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)
#                # Optionally, you can fetch and print the table information
#         table_info = CURSOR.execute("PRAGMA table_info(songs)").fetchall()
#         print(table_info)

# # Call the create_table() method to create the "songs" table
# Song.create_table()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()
# # Call the create_table() method to create the "songs" table
# Song.create_table()

# # Create and save a song using the create() class method
# song = Song.create("Hello", "25")

# # Access the song attributes
# print(song.name)  # Output: "Hello"
# print(song.album)  # Output: "25"

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song