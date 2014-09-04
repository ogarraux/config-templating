import argparse
from CsvDataSource import CsvDataSource
from MultiInstanceGenerator import MultiInstanceGenerator
from SingleInstanceGenerator import SingleInstanceGenerator

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--csv", required=True, help="CSV file with values")
    ap.add_argument("-t", "--template", required=True,
                    help="Template file to use")
    ap.add_argument("-s", "--single-instance", action="store_true",
                    help="Single instance")
    args = ap.parse_args()


cds = CsvDataSource(args.csv)
if args.single_instance:
    ig = SingleInstanceGenerator(args.template)
else:
    ig = MultiInstanceGenerator(args.template)
out_objs = ig.generate(cds)
for oo in out_objs:
    print "#### {t} ####".format(t=oo.title)
    print oo.output
