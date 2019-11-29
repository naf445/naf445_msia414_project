import git
import logging
import logging.config
import glob
import os
ROOT = git.Repo('.', search_parent_directories=True).working_tree_dir + '/'
import sys
sys.path.append(os.path.join(ROOT, 'src'))
sys.path.append(os.path.join(ROOT, 'src', 'helpers'))
import helpers.data_clean as data_clean
import yaml
from urllib.request import urlopen

with open(os.path.join(ROOT, 'config', 'config.yml'), "r") as yml_file:
    config = yaml.safe_load(yml_file)
    logging.config.fileConfig(os.path.join(
        ROOT, config['logger']), disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    config = config['src']['preprocess_new_text']
    
def load_clean_store(text_file_name, outfile_name):
    with open(os.path.join(ROOT, config['data_in_directory'], text_file_name), 'r') as file:
        text_to_clean = file.readlines()
    logger.info("Imported {}".format(text_file_name))
    logger.info("First line before processing:\n{}".format(text_to_clean[0]))
    text_to_clean = data_clean.clean_text(text=text_to_clean, starting_line=0,\
                          ending_line=len(text_file_name)+1)
    logger.info("First line after processing:\n{}".format(text_to_clean[0]))
    with open(os.path.join(ROOT, 'data', config['data_out_directory'], text_file_name), "w") as cleaned_file:
        cleaned_file.write('\n'.join(text_to_clean))
    logger.info("Saved Cleaned file to {}".format(config['data_out_directory']+text_file_name))

if __name__ == '__main__':
    outfile_num = 0
    file_name_list = glob.glob(os.path.join(ROOT, config['data_in_directory'], "*.txt"))
    for text_file_name in file_name_list:
        load_clean_store(text_file_name=text_file_name,\
                         outfile_name=text_file_name)
        outfile_num += 1
    
    

    