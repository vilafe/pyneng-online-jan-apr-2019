# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os
from pprint import pprint

#$ python cfg_gen.py templates/for.txt data_files/for.yml
TEMPLATE_DIR, template_file = os.path.split(sys.argv[1])

VARS_FILE = sys.argv[2]

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template(template_file)

with open(VARS_FILE) as f:
    vars_dict = yaml.load(f, Loader=yaml.FullLoader)

print(template.render(vars_dict))
#pprint(vars_dict)
