import wikipedia
import sys

# Uses Wikipedia API developed by https://github.com/goldsmith

# If a command line argument was provided, search for it.
# Else, prompt the user for a search input.
def main():
    if (len(sys.argv) > 1):
        summary(sys.argv[1])
    else:
        summary(get_query())

# ----------------------------------------------
# Prompts user for a query.
# RETURNS a string containing their search query.
# ----------------------------------------------
def get_query():
    query = input("What topic would you like to know about? ")
    return query

def summary(query):
    try:
        print('-----------------------------------------------------')
        print(wikipedia.summary(query))
        print('-----------------------------------------------------')
    except wikipedia.exceptions.DisambiguationError as e:
        print(e)
        print('''
            -----------------------------------------------------
            Run this script again on a more specific search term!
            -----------------------------------------------------
        ''')

if __name__ == '__main__':
    main()