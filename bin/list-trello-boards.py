#!/usr/bin/env python
# Load in our dependencies
from __future__ import print_function
import argparse

from trello import TrelloClient


# Define our logic
def main(api_key, token):
    """List out the boards for our client"""
    trello_client = TrelloClient(
        api_key=api_key,
        token=token,
    )
    print('Boards')
    print('-----')
    print('Name: Id')
    for board in trello_client.list_boards():
        print('{board.name}: {board.id}'.format(board=board))


# Run our script
if __name__ == '__main__':
    # Set up our parser
    parser = argparse.ArgumentParser(description='Output list ids for a Trello board')
    parser.add_argument('8e6c0b5d86a5f60ed6809ecd46ee4625', help='Key used for TRELLO_API_KEY in env')
    parser.add_argument('8d2b6ed4a76691cb904428c43c15dbbdd7280a108019976157babef3e52cb52c', help='Token used for TRELLO_TOKEN in env')

    # Parse and run via kwargs
    args = parser.parse_args()
    main(**args.__dict__)
