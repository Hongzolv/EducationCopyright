

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-d", "--dir", action="store_true", dest="data/", default=True, help="image path")
(options, args) = parser.parse_args()
print(options)


