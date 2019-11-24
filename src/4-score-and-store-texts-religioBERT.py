# Based off https://github.com/UKPLab/sentence-transformers/blob/master/examples/basic_embedding.py
from sentence_transformers import SentenceTransformer, LoggingHandler
import numpy as np
import logging
import logging.config
import git
import glob
import json
import os
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
    # Load religioBERT or other model from Disk
    model = SentenceTransformer(os.path.join(ROOT, config['model_directory']))
    text_index = 0
    for religious_text_file_name in glob.glob(os.path.join(ROOT, 'data', 'cleaned_data' ,"*.txt")):
        religious_text_sentences = []
        with open(os.path.join(ROOT, 'data', 'cleaned_data', religious_text_file_name), 'r') as file:
            for line in file:
                religious_text_sentences.append(line.strip())
        religious_text_embeddings = model.encode(religious_text_sentences)
        religious_text_dictionary = {}
        for sentence, embedding in zip(religious_text_sentences, religious_text_embeddings):
            religious_text_dictionary[str(embedding)] = sentence
        with open(os.path.join(ROOT, 'data', 'religioBERT_scored_texts',\
                               config['data_out_file_names'][text_index]), 'w') as json_output:
            json.dump(religious_text_dictionary, json_output, indent=4)
        text_index+=1
