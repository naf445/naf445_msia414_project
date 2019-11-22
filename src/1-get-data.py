from bs4 import BeautifulSoup
import git
import logging
import logging.config
import os
ROOT = git.Repo('.', search_parent_directories=True).working_tree_dir + '/'
import sys
import yaml
from urllib.request import urlopen

with open(os.path.join(ROOT, 'config', 'config.yml'), "r") as yml_file:
    config = yaml.safe_load(yml_file)
    logging.config.fileConfig(os.path.join(
        ROOT, config['logger']), disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    config = config['src']['get_data']

if __name__ == '__main__':
    logger.info("Downloading Gita")
    gita_html = urlopen(config['text_urls']['gita']).read()
    gita_raw = BeautifulSoup(gita_html, features="html.parser").get_text()
    logger.info("Gita Sample:\n{}".format(gita_raw[:200]))
    
    logger.info("Downloading Analects")
    analects_html = urlopen(config['text_urls']['analects']).read()
    analects_raw = BeautifulSoup(analects_html, features="html.parser").get_text()
    logger.info("Analects Sample:\n{}".format(analects_raw[:200]))
    
    logger.info("Downloading Egypt")
    egypt_html = urlopen(config['text_urls']['egypt']).read()
    egypt_raw = BeautifulSoup(egypt_html, features="html.parser").get_text()
    logger.info("Egpyt Sample:\n{}".format(egypt_raw[:200]))
    
    logger.info("Downloading Tibet")
    tibet_html = urlopen(config['text_urls']['tibet']).read()
    tibet_raw = BeautifulSoup(tibet_html, features="html.parser").get_text()
    logger.info("Tibet Sample:\n{}".format(tibet_raw[:200]))
    
    logger.info("Saving Text Files")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['out_files']['gita']), "w") as gita_file:
        gita_file.writelines(gita_raw)
    with open(os.path.join(ROOT, 'data', 'raw_data', config['out_files']['analects']), "w") as analects_file:
        analects_file.writelines(analects_raw)
    with open(os.path.join(ROOT, 'data', 'raw_data', config['out_files']['egypt']), "w") as egypt_file:
        egypt_file.writelines(egypt_raw)
    with open(os.path.join(ROOT, 'data', 'raw_data', config['out_files']['tibet']), "w") as tibet_file:
        tibet_file.writelines(tibet_raw)
    