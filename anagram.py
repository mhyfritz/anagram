#! /usr/bin/env python

import sys
from collections import defaultdict
import click
import os

default_dict_file = '/usr/share/dict/words'


def solve_db(query, db):
    for word in db[''.join(sorted(query.lower()))]:
        if word.lower() != query.lower():
            yield word


def mk_db(fn):
    db = defaultdict(list)
    with open(fn) as f:
        for l in f:
            word = l.rstrip()
            db[''.join(sorted(word.lower()))].append(word)
    return db


def solve_file(query, fn):
    db = mk_db(fn)
    return solve_db(query, db)


@click.command()
@click.option('dictionary', '-d', '--dict',
              help='dictionary file',
              type=click.Path(),
              default=default_dict_file)
@click.argument('word')
def main(dictionary, word):
    if not os.path.exists(dictionary):
        click.echo('no such file "{}"'.format(dictionary), err=True)
        sys.exit(1)
    anagrams = solve_file(word, dictionary)
    for a in anagrams:
        click.echo(a)

if __name__ == '__main__':
    main()
