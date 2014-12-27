#! /usr/bin/env python

import sys
import os
from collections import defaultdict
import json
from itertools import ifilter
import click

default_words_file = '/usr/share/dict/words'


@click.group()
def cli():
    """Anagram solver."""


def idx_key(word):
    return ''.join(sorted(word.lower()))


def mk_idx(f):
    idx = defaultdict(list)
    for l in f:
        word = l.rstrip()
        key = idx_key(word)
        idx[key].append(word)
    return idx


@cli.command()
@click.argument('wordsfile', type=click.File())
def index(wordsfile):
    """Index a words file.
    \b
    e.g.
    index /usr/share/dict/words > words.idx.json
    """
    idx = mk_idx(wordsfile)
    click.echo(json.dumps(idx))


def anagrammer(word, idx):
    key = idx_key(word)
    return ifilter(lambda a: a.lower() != word.lower(), idx[key])


@cli.command()
@click.option('idxfile', '-i', '--index', type=click.File(),
              help='input index file')
@click.option('-w', '--wordsfile', type=click.File(),
              help='input words file')
@click.argument('word')
def solve(idxfile, wordsfile, word):
    """Solve anagrams for given word."""
    if idxfile and wordsfile:
        click.echo('"--index" and "--wordsfile" are mutually exclusive',
                   err=True)
        sys.exit(2)
    if not idxfile and not wordsfile:
        try:
            wordsfile = open(default_words_file)
        except IOError:
            click.echo('cannot find default file "{}"'
                       .format(default_words_file), err=True)
            sys.exit(1)
    if idxfile:
        idx = json.load(idxfile)
    else:
        idx = mk_idx(wordsfile)
    for anagram in anagrammer(word, idx):
        click.echo(anagram)


if __name__ == '__main__':
    cli()
