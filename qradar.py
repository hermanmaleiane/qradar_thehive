import requests
import sys
import json
import time
import uuid
from qradar4py.api import QRadarApi
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact, CustomFieldHelper
from thehive import create_case
from utils import format_description,get_epochdate


QRADAR_URL = 'https://qradar-01.bci.co.mz/'
QRADAR_API_KEY = 'd1e46471-7704-4e23-aa90-4083d2c3bc75'

# Initalize the API with the URL, your API token and whether the certificate should be checked.
qradar_api = QRadarApi(QRADAR_URL, QRADAR_API_KEY, version='16.0', verify=False)

# Get all offenses different from closed status in the last 15 minutes

param_filter='status != CLOSED  and start_time>'+str(get_epochdate())
response = qradar_api.siem.get_offenses(filter=param_filter,  Range='items=0-10')
offenses_json_list = response[1]

for offense_json  in offenses_json_list:
                  # Access fields
             offense_id = str(offense_json['id']) 
             description = offense_json['description']  
             severity  = str(offense_json['severity']) 
             offense_type  = str(offense_json['offense_type']) 
             log_sources   = str(offense_json['log_sources']) 
             source_network   = str(offense_json['source_network']) 
             destination_networks   = str(offense_json['destination_networks']) 
             categories   = str(offense_json['categories'])  
             start_time    = str(offense_json['start_time'])
             thehive_description= format_description(description, offense_type,severity,source_network,destination_networks,categories)
             #print(str(start_time))
             create_case(description,thehive_description)




