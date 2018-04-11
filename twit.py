#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'CMSVGMKuMfDEqnK4feXWuipUj'
CONSUMER_SECRET = 'xHApPtDJx6xjkmRZabUvCP0x8Pi1xh2Qc5CAWpRBqnGYbB7sdg'
ACCESS_KEY = '455317197-6E6fmaviIARgJO2u80CIS26zRBLlzh4bWfnIZYW1'
ACCESS_SECRET = 'jZXtGCTPbK39sYOkhaj3Om3SXsZ680ZAmLupGWkTL5ypO'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1])

