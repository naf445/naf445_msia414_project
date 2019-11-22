import git
import os
ROOT = git.Repo('.', search_parent_directories=True).working_tree_dir + '/'
import sys
sys.path.append(os.path.join(ROOT, 'src', 'helpers'))
import logging
import logging.config
import yaml
np.random.seed(39)

with open(os.path.join(ROOT, 'config', 'config.yml'), "r") as yml_file:
    config = yaml.safe_load(yml_file)
    logging.config.fileConfig(os.path.join(
        ROOT, config['logger']), disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    config = config['src']['get-data']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'test', help="test")
    args = parser.parse_args()

    logger.info("Load in data")
