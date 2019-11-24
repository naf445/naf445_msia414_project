# Based off https://github.com/UKPLab/sentence-transformers/blob/master/examples/basic_embedding.py
from sentence_transformers import SentenceTransformer, LoggingHandler
import numpy as np
import logging
import logging.config
import git
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
    config = config['src']['score_and_store_texts']

if __name__ == '__main__':
    # Load religioBERT or other model from Disk
    model = SentenceTransformer(os.path.join(ROOT, config['model_directory']))

    # Embed a list of sentences
    analects_sentences = []
    with open(os.path.join(ROOT, 'data', config['data_in_file']), 'r') as file:
        for line in file:
            analects_sentences.append(line.strip())
    analects_embeddings = model.encode(analects_sentences)

    # The result is a list of sentence embeddings as numpy arrays
    for sentence, embedding in zip(sentences_to_score, sentence_embeddings):
        print("Sentence:", sentence)
        print("Embedding:", embedding)
        print("")