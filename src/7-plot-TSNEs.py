import git
import os
ROOT = git.Repo('.', search_parent_directories=True).working_tree_dir + '/'
import sys
sys.path.append(os.path.join(ROOT, 'src', 'helpers'))
import logging
import logging.config
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pickle
from sklearn.manifold import TSNE
import yaml
np.random.seed(39)

with open(os.path.join(ROOT, 'config', 'config.yml'), "r") as yml_file:
    config = yaml.safe_load(yml_file)
    logging.config.fileConfig(os.path.join(
        ROOT, config['logger']), disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    config = config['src']['plot_TSNEs']
    
def tsne_plot_words(title, sentences, embeddings_en_2d, path_to_save):
    plt.figure(figsize=(16, 9))
    x = embeddings_en_2d[:, 0]
    y = embeddings_en_2d[:, 1]
    plt.scatter(x, y, label=sentences)
    for i, txt in enumerate(sentences):
        plt.annotate(txt, (x[i], y[i]))
    plt.title(title)
    plt.grid(True)
    plt.savefig(path_to_save)
    plt.clf()
    plt.cla()

if __name__ == '__main__':
    logger.info("Load baseBERT encoded phrases from {}".format(config['data_in_baseBERT']))
    with open(config['data_in_baseBERT'], 'rb') as pkl_file:
        baseBERT_dict = pickle.load(pkl_file)
    logger.info("Load religioBERT encoded phrases from {}".format(config['data_in_religioBERT']))
    with open(config['data_in_religioBERT'], 'rb') as pkl_file:
        religioBERT_dict = pickle.load(pkl_file)
        
    base_sentences = list(baseBERT_dict.keys())
    base_embeddings = list(baseBERT_dict.values())
    religio_sentences = list(religioBERT_dict.keys())
    religio_embeddings = list(religioBERT_dict.values())
    
    base_embeddings = np.array(base_embeddings)
    religio_embeddings = np.array(religio_embeddings)
    
    logger.info("Fitting TSNE models")
    tsne_model_2D_base = TSNE(perplexity=15, n_components=2, init='pca', n_iter=3500, random_state=40)
    embeddings_base_2D = np.array(tsne_model_2D_base.fit_transform(base_embeddings))
    tsne_model_2D_religio = TSNE(perplexity=15, n_components=2, init='pca', n_iter=3500, random_state=30)
    embeddings_religio_2D = np.array(tsne_model_2D_religio.fit_transform(religio_embeddings))
    
    logger.info("Plotting and saving TSNE plot to {}".format(config['plots_store_out']['base']))
    tsne_plot_words(title='baseBERT Phrases TSNE Projections',
                    sentences=base_sentences,
                    embeddings_en_2d=embeddings_base_2D,
                   path_to_save=config['plots_store_out']['base'])
    
    logger.info("Plotting and saving TSNE plot to {}".format(config['plots_store_out']['religio']))
    tsne_plot_words(title='religioBERT Phrases TSNE Projections',
                    sentences=religio_sentences,
                    embeddings_en_2d=embeddings_religio_2D,
                   path_to_save=config['plots_store_out']['religio'])