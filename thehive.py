#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import requests
import sys
import json
import time
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTask, CustomFieldHelper

THEHIVE_URL = 'http://10.2.28.21:9000/'
THEHIVE_API_KEY = 'G0wVbUKKoGGa8iCZAb5ghqi0XreTSNaL'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

def create_case(description,thehive_description):
  print(str(thehive_description))
  tasks = [
    CaseTask(title='Tracking'),
    CaseTask(title='Communication'),
    CaseTask(title='Investigation', status='Waiting', flag=True)
  ] 
   
  case  =  Case(title=description,
              tlp=3,
              pap=3,
              flag=True,
              tags=['soc', 'qradar'],
              description=str(thehive_description),
              tasks=tasks)

  #print('Create case')
  #print('-----------------------------')
  id = None
  response = api.create_case(case)

  if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
  else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)
  
  # Get all the details of the created case
  print('Get created case {}'.format(id))
  print('-----------------------------')
  response = api.get_case(id)
  if response.status_code == requests.codes.ok:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
  else:
    print('ko: {}/{}'.format(response.status_code, response.text)) 

 