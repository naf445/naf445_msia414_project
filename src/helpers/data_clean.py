import git
import logging
import logging.config
import os
ROOT = git.Repo('.', search_parent_directories=True).working_tree_dir + '/'
import re
import string
import sys
from unidecode import unidecode
import yaml


with open(os.path.join(ROOT, 'config', 'config.yml'), "r") as yml_file:
    config = yaml.safe_load(yml_file)
    logging.config.fileConfig(os.path.join(
        ROOT, config['logger']), disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    config = config['src']['helpers']['data_clean']
    
def clean_text(text, starting_line, ending_line):
    text = text[starting_line:ending_line+1]
    text = [line for line in text if line!='\n' ]
    text = [line.strip() for line in text]
    text = [line.lower() for line in text]
    text = [line.translate(str.maketrans('', '', string.punctuation)) for line in text]
    line_ending_num_regex = re.compile(r" +\d+$", re.IGNORECASE)
    text = [line_ending_num_regex.sub('', line) for line in text]
    new_line_regex = re.compile(r"""\n""", re.IGNORECASE)
    text = [new_line_regex.sub('', line) for line in text]
    text = [unidecode(line) for line in text]
    roman_num_regex_pattern=r'\bM{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b'
    roman_num_regex = re.compile(roman_num_regex_pattern, re.IGNORECASE)
    text = [roman_num_regex.sub('', line) for line in text]
    text = [line for line in text if line!='' ]
    numerals_regex = re.compile(r'\d+', re.IGNORECASE)
    text = [numerals_regex.sub('', line) for line in text]
    chap_regex = re.compile(r"chap +", re.IGNORECASE)
    text = [chap_regex.sub('', line) for line in text]
    multi_space_regex_pattern = r' {2,}'
    multi_space_regex = re.compile(multi_space_regex_pattern, re.IGNORECASE)
    text = [multi_space_regex.sub(' ', line) for line in text]
    text = [line.strip() for line in text]
    text = [line for line in text if line!='' ]
    return text