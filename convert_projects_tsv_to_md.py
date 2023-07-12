#!/usr/bin/env python3

import os
import csv
from operator import itemgetter
from argparse import ArgumentParser

def reformat_projects_tsv(tsv_filename, sort_by=None):

    data_rows = []
    with open(tsv_filename) as tsv_contents:
        reader = csv.DictReader(tsv_contents, dialect="excel-tab")

        for row in reader:
            row['Issue'] = int(os.path.basename(row['URL']))
            data_rows.append(row)

    if sort_by is not None:
        data_rows = sorted(data_rows, key=itemgetter(*sort_by))

    for row in data_rows:
        print("- [{Repository} #{Issue}]({URL}) - {Title}".format(**row))


def main():

    parser = ArgumentParser("Convert a TSV export from Github Projects into Markdown that can be more easily plopped into this repo's CHANGELOG")

    parser.add_argument("tsv_file", help="Name of TSV file to parse")
    parser.add_argument("-s" "--sort_by", dest="sort_by",
        help="Name of column to sort by", nargs='*',
        choices=["Title", "Issue", "URL", "Assignees", "Status", "Feature", "Labels", "Release", "Repository", "Dependency"],
        default=["URL", "Issue"],
    )

    args = parser.parse_args()

    reformat_projects_tsv(args.tsv_file, args.sort_by)

if __name__ == "__main__":
    main()
