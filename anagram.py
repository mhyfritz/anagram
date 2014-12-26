#! /usr/bin/env python

import sys
import os
from collections import defaultdict
import click

default_dict_file = '/usr/share/dict/words'


def solve_with_db(query, db):
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


def solve_with_file(query, fn):
    db = mk_db(fn)
    return solve_with_db(query, db)


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
    for anagram in solve_with_file(word, dictionary):
        click.echo(anagram)

if __name__ == '__main__':
    main()
