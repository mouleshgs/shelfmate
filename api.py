import requests

url = "https://openlibrary.org/search.json"

def search(book_name):

    custom_header = {
        "User-Agent": "shelfmate/1.0 (shelfmate@gmail.com)"
    }

    res = requests.get(url, params={"q": book_name, "limit" : "1"}, headers=custom_header)

    data = res.json()

    if not data.get("docs"):
        return None

    doc = data["docs"][0]

    book_data = {
        "title" : doc.get("title"),
        "url": "https://openlibrary.org" + doc.get("key", ""),
        "author": doc.get("author_name")[0]
    }

    

    return book_data

    

if __name__ == "__main__":
    search("white nights")