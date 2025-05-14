import sqlite3 #imports sqlite database tools

music_database = sqlite3.connect('trackdb.sqlite') #create a file if not created 
cursor_for_db = music_database.cursor() #allows for instructions to be written moving forward

cursor_for_db.executescript(''' 
DROP TABLE IF EXISTS Artist; 
DROP TABLE IF EXISTS GENRE;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
                  
CREATE TABLE Artist (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE           
);
                                                                                                                          
CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,                         
    len INTEGER, rating INTEGER, count INTEGER
);
                  
''') #deletes any existing tables and creates new tables with specific columns

tracks_file = open('tracks.txt') #open the track.cvs file so we can read through it

for line in tracks_file: # go through each line one at a time
    line = line.strip() # remove any spaces and nelines from the end of each line
    pieces = line.split(',') # break the line into a list of parts seperated by commas 
    if len(pieces) < 7: continue # if the list doesnt have 6 parts skip to next line

    name = pieces[0] # track title 
    artist = pieces [1] # artist name
    album = pieces[2] # album name
    genre = pieces[3] # type of genre 
    count = pieces[4] # number of plays  
    rating = pieces[5] # rating (1-5) 
    length = pieces[6] # track lenght in seconds 

    print(name, artist, album, count, rating, length) # show the parsed data 

    # Insert artist if they don't already exist
    cursor_for_db.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cursor_for_db.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cursor_for_db.fetchone()[0]

    # Insert album (if not already there), then get album_id
    cursor_for_db.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
    cursor_for_db.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cursor_for_db.fetchone()[0]

    #Insert genre (if not already there),. then get genre_id
    cursor_for_db.execute('INSERT OR IGNORE INTO GENRE (name) VALUES (?)', (genre,))
    cursor_for_db.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
    genre_id = cursor_for_db.fetchone()[0]

    # Insert or update track information 
    cursor_for_db.execute('''INSERT OR REPLACE INTO Track 
        (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (name, album_id, genre_id, length, rating, count))
    
music_database.commit()

cursor_for_db.execute('''
    SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track
    JOIN Genre On Track.genre_id = Genre.id
    JOIN Album ON Track.album_id = Album.id
    JOIN Artist ON Album.artist_id = Artist.id
    ORDER BY Artist.name
    LIMIT 3
''')   

# Featch and print results 
results = cursor_for_db.fetchall()
print("\nTop 3 Tracks with Artist, Album, Genre:\n")
for row in results:
    print(f"Track: {row[0]}, Artist: {row[1]}, Album: {row[2]}, Genre: {row[3]}")