from Bio import Entrez
import xml.etree.ElementTree as ET
import argparse
email = "tnphung@ucla.edu"

### Credit: this script is adapted from: http://biopython.org/DIST/docs/api/Bio.Entrez-module.html
def parse_args():
    """
    Parse command-line argument
    """
    parser = argparse.ArgumentParser(description="This script takes in a list of snps and pubmed id and return the title of the pubmed article")
    parser.add_argument(
            "--snp_pubmed_cited", required=True,
            help="REQUIRED.")
    parser.add_argument(
            "--outfile", required=True,
            help="REQUIRED.")
    args = parser.parse_args()
    return args


def get_title(PubmedID):
    Entrez.email = email
    handle = Entrez.esummary(db="pubmed", id=PubmedID, retmode="xml")
    records = Entrez.parse(handle)
    title = ''
    for record in records:
        title = record['Title']
    handle.close()

    return title

def main():
    args = parse_args()
    outfile = open(args.outfile, "w")
    with open(args.snp_pubmed_cited, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            line = line.split("\t")
            title = get_title(line[1])
            toPrint = [line[0], line[1], title]
            print >>outfile, ",".join(x for x in toPrint).encode('utf-8').strip()
main()

