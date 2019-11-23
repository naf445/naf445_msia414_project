from bs4 import BeautifulSoup
import git
import logging
import logging.config
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
    config = config['src']['create_combined_corpus']

if __name__ == '__main__':
    
    logger.info("Import Analects")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['analects']['in_path']), 'r') as file:
        analects = file.readlines()
    analects = data_clean.clean_text(text=analects, starting_line=config['analects']['start_line'],\
                          ending_line=config['analects']['end_line'])
    logger.info("First 3 lines:\n{}".format(analects[:3]))
    logger.info("Last 3 lines:\n{}".format(analects[-3:]))
    
    logger.info("Import Bible")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['bible']['in_path']), 'r') as file:
        bible = file.readlines()
    bible = data_clean.clean_text(text=bible, starting_line=config['bible']['start_line'],\
                          ending_line=config['bible']['end_line'])
    logger.info("First 3 lines:\n{}".format(bible[:3]))
    logger.info("Last 3 lines:\n{}".format(bible[-3:]))
    
    logger.info("Import Buddha")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['buddha']['in_path']), 'r') as file:
        buddha = file.readlines()
    buddha = data_clean.clean_text(text=buddha, starting_line=config['buddha']['start_line'],\
                          ending_line=config['buddha']['end_line'])
    logger.info("First 3 lines:\n{}".format(buddha[:3]))
    logger.info("Last 3 lines:\n{}".format(buddha[-3:]))
    
    logger.info("Import Egypt")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['egypt']['in_path']), 'r') as file:
        egypt = file.readlines()
    egypt = data_clean.clean_text(text=egypt, starting_line=config['egypt']['start_line'],\
                          ending_line=config['egypt']['end_line'])
    logger.info("First 3 lines:\n{}".format(egypt[:3]))
    logger.info("Last 3 lines:\n{}".format(egypt[-3:]))
    
    logger.info("Import Gita")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['gita']['in_path']), 'r') as file:
        gita = file.readlines()
    gita = data_clean.clean_text(text=gita, starting_line=config['gita']['start_line'],\
                          ending_line=config['gita']['end_line'])
    logger.info("First 3 lines:\n{}".format(gita[:3]))
    logger.info("Last 3 lines:\n{}".format(gita[-3:]))
    
    logger.info("Import Meditations")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['meditations']['in_path']), 'r') as file:
        meditations = file.readlines()
    meditations = data_clean.clean_text(text=meditations,\
                                        starting_line=config['meditations']['start_line'],\
                                        ending_line=config['meditations']['end_line'])
    logger.info("First 3 lines:\n{}".format(meditations[:3]))
    logger.info("Last 3 lines:\n{}".format(meditations[-3:]))
    
    logger.info("Import Mormon")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['mormon']['in_path']), 'r') as file:
        mormon = file.readlines()
    mormon = data_clean.clean_text(text=mormon, starting_line=config['mormon']['start_line'],\
                          ending_line=config['mormon']['end_line'])
    logger.info("First 3 lines:\n{}".format(mormon[:3]))
    logger.info("Last 3 lines:\n{}".format(mormon[-3:]))
    
    logger.info("Import Quran")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['quran']['in_path']), 'r') as file:
        quran = file.readlines()
    quran = data_clean.clean_text(text=quran, starting_line=config['quran']['start_line'],\
                          ending_line=config['quran']['end_line'])
    logger.info("First 3 lines:\n{}".format(quran[:3]))
    logger.info("Last 3 lines:\n{}".format(quran[-3:]))
    
    logger.info("Import Tibet")
    with open(os.path.join(ROOT, 'data', 'raw_data', config['tibet']['in_path']), 'r') as file:
        tibet = file.readlines()
    tibet = data_clean.clean_text(text=tibet, starting_line=config['tibet']['start_line'],\
                          ending_line=config['tibet']['end_line'])
    logger.info("First 3 lines:\n{}".format(tibet[:3]))
    logger.info("Last 3 lines:\n{}".format(tibet[-3:]))

    combined_and_cleaned = analects+bible+buddha+egypt+gita+meditations+mormon+quran+tibet
    combined_and_cleaned = '\n'.join(combined_and_cleaned)
    logger.info("Saving Combined Religious Texts to {}".format(config['out_path']))
    with open(os.path.join(ROOT, 'data', config['out_path']), "w") as combined_and_cleaned_file:
        combined_and_cleaned_file.write(combined_and_cleaned)
    logger.info("Saved Combined Religious Texts to {}".format(config['out_path']))
    