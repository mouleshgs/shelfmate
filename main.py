from argparse import ArgumentParser
import api
import os
import json 



def search(args):
    result = api.search(args.book_name)

    if result is None:
        print("not found")
        return

    for (idx, res) in enumerate(result, 1):
        print(f"{idx}.")
        print(res['title'])
        print(res['url'])
        print(res['author'])
        print("-----------------")

    with open(".last_search.json", "w") as file:
        json.dump(result, file, indent=4)
    
def add(args):

    if not os.path.isfile(".last_search.json"):
        print("the file is not found")
        return
    
    book_num = args.book_num-1;


    with open(".last_search.json", "r+") as file:
        books = json.load(file)
    
    if (book_num >= len(books)) or book_num < 0:
        print("your index is out of bound!")
        return 
    
    print(books[book_num])

def recommend(args):
    print(args.genre)

def track(args):
    print(args.book_name)


def main():

    parser = ArgumentParser(prog="shelfmate")

    subparser = parser.add_subparsers(dest="command", help="commands like search, recommend, etc ...", required=True)

    search_parser = subparser.add_parser("search", help="search for the books")
    search_parser.add_argument("book_name", help="enter the book name")
    search_parser.set_defaults(func=search)

    add_parser = subparser.add_parser("add", help="add books")
    add_parser.add_argument("book_num", help="enter the book number", type=int)
    add_parser.set_defaults(func=add)

    recommend_parser = subparser.add_parser("recommend")
    recommend_parser.add_argument("genre")
    recommend_parser.set_defaults(func=recommend)

    track_parser = subparser.add_parser("track")
    track_parser.add_argument("book_name")
    track_parser.set_defaults(func=track)


    args = parser.parse_args()  
    args.func(args)

if __name__ == "__main__":
    main()