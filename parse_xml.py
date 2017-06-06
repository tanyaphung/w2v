from Bio import Entrez
from urllib2 import HTTPError
import xml.etree.ElementTree as ET
import os
import sys
import argparse

def parse_args():
    """
    Parse command-line argument
    """
    parser = argparse.ArgumentParser(description="This script tparse the xml file and returns a file with last name and first name which are the authors of a particular article.")
    parser.add_argument(
            "--XML_file", required=True,
            help="REQUIRED. Give the path to the XML file")
    parser.add_argument(
            "--outfile", required=True,
            help="REQUIRED. Give the path to the output file")
    args = parser.parse_args()
    return args

def main():
	
    args = parse_args()
    outfile = open(args.outfile, "w")
    header = ["Last_name", "First_name"]
    print >>outfile,"\t".join(x for x in header)

    tree = ET.ElementTree(file=args.XML_file)
    root = tree.getroot()
    for child in root:
    	if child.tag == "front":
    		for step_child in child:
    			if step_child.tag == "article-meta":
    				for step_child_2 in step_child:
    					if step_child_2.tag == "contrib-group":
    						for step_child_3 in step_child_2:
    							for step_child_4 in step_child_3:
    								toprint = []
    								for step_child_5 in step_child_4:
    									toprint.append(step_child_5.text)
    								print >>outfile,"\t".join(x for x in toprint)
main()




