Orthoptera-TElib: A library of Orthoptera transposable elements for TE annotation

The Orthoptera-TElib.fa and Orthoptera-TElib.db have been deposited into the figshare database (https://doi.org/10.6084/m9.figshare.23993616.v3)

We used a Python script to generate a SQLite3 database of Orthoptera-TElib.db (https://github.com/Liuxuanzeng/OTElib). The table Orthoptera-TElib is created in Orthoptera-TElib.db, which contains five fields: unique id, species name, TE Class, TE superfamily, and sequence. Users can use our provided Python script to update Orthoptera-TElib.db.

Users can search the required sequence according to the species name, TE class, and TE superfamily generating Fasta format files. For example, users can run SQL (Structured Query Language) " SELECT * FROM OTElib WHERE class='LTR' " to obtain LTR records (Fasta format) in Orthoptera-TElib.



Generate an SQL format file from the TE Fasta file.

Usage: python3 OTElib_store_Sqlite3.py [input.fa]



Fasta sequence was extracted from Orthoptera-TElib.db according to TE class.

Usage: python3 OTElib_db_slect.py [TEclass] Orthoptera-TElib.db


need: 

import pyfastx

import sqlite3

import sys
