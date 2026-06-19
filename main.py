from argparse import ArgumentParser
import api



def search(args):
    result = api.search(args.book_name)

    if result is None:
        print("not found")
        return

    print(result['title'])
    print(result['url'])
    print(result['author'])
    

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