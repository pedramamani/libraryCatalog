# Library Catalog
A set of tools for cataloging books with minimal effort, originally used to catalog the Hollyburn library

## Steps
### Scan and crop book covers
1. create folders for each genre inside `asset/image/scan`
2. scan the cover of each book as `.jgp` and save it in its genre folder
3. run `renameScan.py` to rename each scan into a random 8-character-long alphanumeric, used as the id of that book
4. run `cropScan.py` to crop each scan and save it in `asset/image/cover`

### Extract text from covers
5. obtain Google client secrets with `auth/cloud-vision` scopes and place the `client.json` file inside `secret`
6. run `obtainToken.py` to create an access token and save to `secret/token.json`
7. run `extractText.py` to find text on the covers and save to `asset/db/text.json`

### Form queries and search for books
8. run `assignGenre.py` to save book genres to `assets/db/genre.json`
9. some covers may contain no text or the text may be unclear, for these add an entry to `asset/db/supplement.json` that points the book id to a string containing the title and author
10. run `assembleQuery.py` to filter out text fragments that are too small, build queries with the rest, and save to `asset/db/query.json` 
11. Obtain a Google Books API key and place it in `.env` under `booksApiKey`
12. run `searchTitle.py` to seach for books using the queries and save title and author information to `asset/db/title.json`
13. You may manually change these information in `asset/db/title.json`

### Generate HTMLs
14. run `finalizeBook.py` to combine title, author, genre, and cover information for each book and save to `asset/db/book.json`
15. run `generateHtml.py` to generate an HTML for each genre using provided template `asset/html/template.html`
