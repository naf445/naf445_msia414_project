# Based off https://github.com/UKPLab/sentence-transformers/blob/master/examples/basic_embedding.py
from sentence_transformers import SentenceTransformer, LoggingHandler
import numpy as np
import logging
import logging.config
import git
import glob
import json
import os
import torch
ROOT = git.Repo('.', search_parent_directories=True).working_tree_dir + '/'
import sys
sys.path.append(os.path.join(ROOT, 'src'))
sys.path.append(os.path.join(ROOT, 'src', 'helpers'))
import yaml

with open(os.path.join(ROOT, 'config', 'config.yml'), "r") as yml_file:
    config = yaml.safe_load(yml_file)
    logging.config.fileConfig(os.path.join(
        ROOT, config['logger']), disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    config = config['src']['score_and_store_texts_religioBERT']

if __name__ == '__main__':
    
    os.environ["CUDA_VISIBLE_DEVICES"] = config['cuda_device']
    device = torch.device("cuda")
    n_gpu = torch.cuda.device_count()
    
    # Load religioBERT or other model from Disk
    model = SentenceTransformer(os.path.join(ROOT, config['model_directory']))
    model.to(device)
    model.eval()
    text_index = 0
    for religious_text_file_name in glob.glob(os.path.join(ROOT, 'data', 'cleaned_data' ,"*.txt")):
        logger.info("Getting embeddings for every sentence in {}".format(religious_text_file_name))
        religious_text_sentences = []
        with open(os.path.join(ROOT, 'data', 'cleaned_data', religious_text_file_name), 'r') as file:
            for line in file:
                religious_text_sentences.append(line.strip())
        len_text = len(religious_text_sentences)
        logger.info('{} has {} lines to get embeddings for'.format(religious_text_file_name,\
                                                                   len_text))
        religious_text_embeddings = model.encode(religious_text_sentences)
        religious_text_dictionary = {}
        line_num = 1
        for sentence, embedding in zip(religious_text_sentences, religious_text_embeddings):
            religious_text_dictionary[str(embedding)] = sentence
            line_num+=1
            perc_complete = round(line_num/len_text*100, 2)
            if perc_complete>9.9 and perc_complete<10.1:
                logger.info('Done with {}%'.format(perc_complete))
            if perc_complete>29.9 and perc_complete<30.1:
                logger.info('Done with {}%'.format(perc_complete))
            if perc_complete>49.9 and perc_complete<50.1:
                logger.info('Done with {}%'.format(perc_complete))
            if perc_complete>89.9 and perc_complete<90.1:
                logger.info('Done with {}%'.format(perc_complete))
        with open(os.path.join(ROOT, 'data', 'religioBERT_scored_texts',\
                               config['data_out_file_names'][text_index]), 'w') as json_output:
            json.dump(religious_text_dictionary, json_output, indent=4)
        text_index+=1
