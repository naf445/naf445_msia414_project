# Based off https://github.com/UKPLab/sentence-transformers/blob/master/examples/basic_embedding.py
from sentence_transformers import SentenceTransformer, LoggingHandler
import argparse
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import numpy as np
import logging
import logging.config
import git
import glob
import json
import os
import pickle
import scipy
import torch
ROOT = git.Repo('.', search_parent_directories=True).working_tree_dir + '/'
import sys
sys.path.append(os.path.join(ROOT, 'src'))
sys.path.append(os.path.join(ROOT, 'src', 'helpers'))
import helpers.data_clean as data_clean
import yaml

with open(os.path.join(ROOT, 'config', 'config.yml'), "r") as yml_file:
    config = yaml.safe_load(yml_file)
    logging.config.fileConfig(os.path.join(
        ROOT, config['logger']), disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    config = config['app']

# Instantiate app and api objects
app = Flask(__name__)
api = Api(app)

# Request parsing
parser = reqparse.RequestParser()
parser.add_argument("--model_choice",
                    help="Options: 'base' or 'religio'. Chooses which model to use for scoring and finding the relevant passage with.",
                   type=str,
                   choices=['base','religio'])
parser.add_argument("--input_sentence",
                    help="Sentence you wish to be matched with a relevant Analects passage.",
                   type=str)
args = parser.parse_args()

# Create instance of model to be used for predictions
model = SentenceTransformer('bert-base-nli-mean-tokens') if args.model_choice == 'base' else SentenceTransformer(os.path.join(ROOT, config['model_directory']))
model.eval()

class GiveAnalectPassage(Resource):
    def get(self):

        # handle user input
        input_sentence = [args.input_sentence]
        input_sentence = data_clean.clean_text(text=input_sentence, starting_line=0,\
                              ending_line=len(input_sentence)+1)
        input_embedding = model.encode(input_sentence)
        output_dict = {}
        output_dict['input_sentence'] = input_sentence[0]
        input_embedding = [round(embedding_num, 6) for embedding_num in list(input_embedding[0])]
        
        with open(os.path.join(ROOT,config['analects_file']['base'] if args.model_choice == 'base' else config['analects_file']['religio']), 'rb') as pkl_file:
            analects_loaded = pickle.load(pkl_file)

        analects_sentences = list(analects_loaded.keys())
        analects_embeddings = list(analects_loaded.values())
        min_distance = 100000
        for index, corpus_embedding in enumerate(analects_embeddings):
            distance = scipy.spatial.distance.cdist([input_embedding], [corpus_embedding], "cosine")[0]
            if distance<min_distance:
                min_distance = distance
                min_index = index
        output_dict['closest_passage'] = analects_sentences[max(0, min_index-2):min(len(analects_sentences), min_index+3)]
        
        return output_dict


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(GiveAnalectPassage, '/')


if __name__ == '__main__':
    app.run(debug=True)