import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from molgenis.eucan_connect.eucan_client import EucanSession
from molgenis.eucan_connect.eucan import Eucan

# First, initialise an EricSession (an extension of the molgenis-py-client Session)
session = EucanSession(url="https://dieuwke.gcc.rug.nl")
session.login("admin", "Replace-Flour-Idea-Plural")

# Get the catalogue(s) you want to import
catalogues = session.get_catalogues(['MS'])

print(catalogues)

eucan = Eucan(session)
import_report = eucan.import_catalogues(catalogues)
