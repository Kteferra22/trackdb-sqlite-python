🎵 Music Library Database Manager

This Python script reads track data from a plain text file and organizes it into a structured SQLite database with normalized tables for artists, albums, genres, and tracks.


🔧 Features

1. Parses a text file with comma-separated music track data.

2. Automatically creates and populates four related database tables:
-  Artist: stores unique artist names.
-  Genre: stores unique genres.
-  Album: links albums to artists.
-  Track: stores track metadata and links to albums and genres.

3. Performs deduplication using INSERT OR IGNORE.

4. Prints a sample of organized data for verification.
   

📁 File Structure

trackdb.sqlite          #Generated SQLite database
tracks.txt              #Input file containing music track data
music_library.py        #Main script file


🧪 Example Input (tracks.txt)


Let It Be,The Beatles,Let It Be,Rock,50,5,243

Billie Jean,Michael Jackson,Thriller,Pop,60,5,294

Bohemian Rhapsody,Queen,A Night at the Opera,Rock,80,5,355


🚀 Getting Started
Prerequisites

1. Python 3.x installed

2. tracks.txt input file in the same directory
   

Running the Script

1. python music_library.py

   
🗃️ Database Schema

Artist(id INTEGER PRIMARY KEY, name TEXT UNIQUE)

Genre(id INTEGER PRIMARY KEY, name TEXT UNIQUE)

Album(id INTEGER PRIMARY KEY, artist_id INTEGER, title TEXT UNIQUE)

Track(id INTEGER PRIMARY KEY, title TEXT UNIQUE, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)


🧩 Sample Output

Top 3 Tracks with Artist, Album, Genre:

Track: Billie Jean, Artist: Michael Jackson, Album: Thriller, Genre: Pop  

Track: Bohemian Rhapsody, Artist: Queen, Album: A Night at the Opera, Genre: Rock  

Track: Let It Be, Artist: The Beatles, Album: Let It Be, Genre: Rock  


📌 Notes
1. If trackdb.sqlite already exists, it will be reset (existing tables dropped).

2. Only lines with at least 7 comma-separated fields are processed.

3. INSERT OR IGNORE and INSERT OR REPLACE ensure data integrity.
