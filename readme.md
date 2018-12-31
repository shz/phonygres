# Phonygres [![Build Status](https://travis-ci.org/shz/phonygres.svg?branch=master)](https://travis-ci.org/shz/phonygres)

A Python3 implementation of Postgres.

## My god man, why?

Testing against a real Postgres instance has a lot of drawbacks.

Also, fun.

### The Caveats

Fully reimplementing Postgres in Python would be, as you expect, a pretty
useless project, and a huge amount of work besides.  That's not the goal
here, so here are the shortcuts taken to get things manageable:

 * It's all in-memory
 * Concurrent transaction support is... limited
 * Indexes are no-ops
 * There's one execution strategy: loop over every record in each
   queries table

## Installing

```
¯\_(ツ)_/¯
```

## Developing

```bash
# Setup
python -m venv .venv # It's 2018, use a virtual env
. .venv/scripts/activate # Modify per your shell's flavor
pip install -r requirements.txt

# And to test your stuff
./setup.py lint
./setup.py test
```

### TODOs



## License

[Unlicense](http://unlicense.org/), so basically public domain.  See
[license.md](license.md) for details.
