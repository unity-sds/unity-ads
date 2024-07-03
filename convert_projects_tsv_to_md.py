#!/usr/bin/env python3

import os
import re
import csv
from operator import itemgetter
from argparse import ArgumentParser

def reformat_projects_tsv(tsv_filename, sort_by=None, show_repo=True, add_release=False, add_url=True, filter_repo=None):

    data_rows = []
    with open(tsv_filename) as tsv_contents:
        reader = csv.DictReader(tsv_contents, dialect="excel-tab")

        for row in reader:
            if filter_repo is None or re.search(filter_repo, row['Repository']):
                row['Issue'] = int(os.path.basename(row['URL']))
                data_rows.append(row)

    if sort_by is not None:
        data_rows = sorted(data_rows, key=itemgetter(*sort_by))

    for row in data_rows:

        item_md = "- "

        if add_url:
            if show_repo:
                item_md += "[{Repository} #{Issue}]({URL})".format(**row)
            else:
                item_md = "[#{Issue}]({URL})".format(**row)
        else:
            if show_repo:
                item_md += "{Repository} #{Issue}".format(**row)
            else:
                item_md = "#{Issue}".format(**row)
 
        item_md += " - {Title}".format(**row)

        if add_release:
            item_md += " ({Release})".format(**row)

        print(item_md)

def main():

    parser = ArgumentParser("Convert a TSV export from Github Projects into Markdown that can be more easily plopped into this repo's CHANGELOG")

    parser.add_argument("tsv_file", help="Name of TSV file to parse")

    parser.add_argument("-s", "--sort_by", dest="sort_by",
        help="Name of column to sort by", nargs='*',
        choices=["Title", "Issue", "URL", "Assignees", "Status", "Feature", "Labels", "Release", "Repository", "Dependency"],
        default=["URL", "Issue"],
    )

    parser.add_argument("-r", "--add_release", action="store_true", default=False,
        help="Add display of the release version for each item"
    )

    parser.add_argument("-f", "--filter_repo", default=None,
        help="Filter out all other items except those matching the given string for the Repository column"
    )

    parser.add_argument("--no_repo", dest="show_repo_name", action="store_false", default=True,
        help="Hide the repository name in links to each issue."
    )

    parser.add_argument("--no_url", dest="add_url", action="store_false", default=True,
        help="Do not add a URL for each item"
    )

    args = parser.parse_args()

    reformat_projects_tsv(args.tsv_file, sort_by=args.sort_by, show_repo=args.show_repo_name, add_release=args.add_release, add_url=args.add_url, filter_repo=args.filter_repo)

if __name__ == "__main__":
    main()
