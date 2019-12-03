# MSiA 414 Text Analytics Project

## Nathan Franklin

Project Assignment: https://canvas.northwestern.edu/courses/98186/assignments/640163

## Charter

### Vision

As unenlightened humans, we are faced with a barrage of environmental stimuli, interpretations of those stimuli, events which occur to us, challenges, important questions and many more things which buffet us in our daily lives. Over the millenia, human civilization has created religions and philosophy to try to make sense of these precarious circumstances we find ourselves in and and try and best navigate our way through them. Religious and philosphical texts from major cultures/religions are the storage of the most well known answers and strategies for this ubiquitous human condition, and thus an easy way to find a relevant passage or topic from one of these texts could come in handy. This project attempts to use techniques in machine learning and specifically natural language processing to make it easier for someone to find the right topic or passage for their situation.

### Mission

The goal of this project is for a user to be able to enter in some topic, problem, question, or situation in their lives, and to have the application provide suggestions for which passage from the available religious/philosophical literature would best match a user's input. The idea is that a passage which is similar in meaning/syntax/topic to a user's input will be directly relevant to a user and thus will be worth reading for that person.

## App Details

### Gather the Data

The data comes from 2 didfferent sources. One is a kaggle page with 5 of the texts used in this training, while the other 5 come from online project Gutenberg versions. The urls for these can be found in the `Data` section below. The process to retreive these texts is detailed in the `Start2Finish` section below.

### Compile cleaned_and_combined_corpus.txt

### Continue BERT pre-training


## Setting Up the App from Start 2 Finish

### CPU Machine:

1) Create/Activate conda environment
```bash
conda env create environment_cpu.yml
```

```bash
source activate text-project-cpu
```

2) Retrieve some data


```bash
python 1-get-data.py
```

3) Retrieve rest of data (you will first have to configure [kaggle command line](https://github.com/Kaggle/kaggle-api))

```bash
kaggle datasets download tentotheminus9/religious-and-philosophical-texts --unzip --path data/raw_data/
```

4) Rename texts grabbed from Kaggle 

```bash
mv data/raw_data/35895-0.txt data/raw_data/buddha_raw.txt;
mv data/raw_data/pg10.txt data/raw_data/bible_raw.txt;
mv data/raw_data/pg17.txt data/raw_data/mormon_raw.txt;
mv data/raw_data/pg2680.txt data/raw_data/meditations_raw.txt;
mv data/raw_data/pg2800.txt data/raw_data/quran_raw.txt;
```

5 ) Run from root folder, to create cleaned version of texts ready for BERT model, both separate versions and one large combined version.

```bash
python src/2-create-cleaned-texts.py
```

6 )
- Send `cleaned_and_combined.txt` to GPU machine for continued BERT pre-training
- Place in `data/cleaned_and_combined.txt` on GPU machine

### GPU Machine:

7 ) Create/Activate GPU conda environment

```bash
conda env create environment_gpu.yml
```

```bash
source activate text-project-gpu
```

8 ) Run from root directory, to prepare GPU machine for BERT pre-training
```bash
source config/pre_train_settings.sh
```

9 ) Run from root directory to initiate BERT pretraining. (You will have to have [hyperdash](https://hyperdash.io) installed and configured). You could do it without hypderdash but hyperdash is cool...

```bash
hyperdash run -n 'BERT_pretrain' python src/3-pretrain-religioBERT.py --train_corpus $TRAIN_CORPUS --bert_model $BERT_MODEL --output_dir $OUTPUT_DIR --do_train --do_lower_case --cuda_device $CUDA_DEVICE
```

10 ) 
- Now we will need to change our directory structure a bit in order to prepare things for generating our sentence embeddings using religioBERT.
- First download one of these files, probably `bert-base-nli-mean-tokens.zip` from https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/v0.2/
- Place this unzipped folder in a new folder in your project repository, `data/bert-base-nli-mean-tokens/`
- Delete everything from `data/bert-base-nli-mean-tokens/0_BERT/`,  **except for the file** `data/bert-base-nli-mean-tokens/0_BERT/sentence_bert_config.json`
- Place everything that was in `pretraining_output/best` in the now almost empty `data/bert-base-nli-mean-tokens/0_BERT`
- Delete the now completely empty `pretraining_output/best/`
- Change name of `data/bert-base-nli-mean-tokens/` to `data/pretraining_output/`

11 ) 
- Now we can use religioBERT to get embeddings for input texts. Right now we are just going to do this for one religious text, and we will do it on the GPU because it is much faster.
- To set this up, we need our text file placed in `data/cleaned_data/ready_for_scoring/`, comprised of lines of words or sentences separated by a new line character.
- This can be accomplished prior to this step (for example, the output of `src/2-create-cleaned-texts.py` is in this form), or it will be done automatically at the time of running. 
- To do at this time, run the following:

```bash
python src/4-preprocess-new-text.py
```

12 ) Score new text with ReligioBERT and save output
- Once your cleaned text data has been placed in `data/cleaned_data/ready_for_scoring/`, head to the `config.yml` file and make sure `data_out_file_names:` has listed as many output files as you have input files, and the names are as you want them to appear.
- Run from root directory
```bash
python src/5-score-and-store-texts-religioBERT.py
```
- This script will return a serialized python dictionary object as an output file (one file for each of the input files) with each of these lines as keys and the associated BERT embeddings as values.

13 ) Score new text w/ baseBERT and save output
- Change `config:src:score_and_store_texts_baseBERT:data_out_file_names` to `analects_baseBERT_embeddings.pkl`
- Run from root directory
```bash
python src/6-score-and-store-texts-baseBERT.py
```

14 ) Send files/models to CPU machine
- Send the further-pretrained religioBERT `model/pretraining_output/best` folder to CPU machine, place in `model/pretraining_output/best/`.
- Also send the cleaned religious texts (one scored with baseBERT and one with religioBERT) which you want to your CPU machine and place in `data/religioBERT_scored_texts/` and `data/baseBERT_scored_texts/`

### CPU Machine:

15 ) 
```bash
source activate text-project-cpu
```

16 ) Place phrases to be visualized in `data/cleaned_data/ready_for_scoring/`
- Can run if needed:
```bash
python src/4-preprocess-new-text.py
```
- Then run the following three items:
```bash
python src/5-score-and-store-texts-religioBERT.py
```
```bash
python src/6-score-and-store-texts-baseBERT.py
```
```bash
python src/7-plot-TSNEs.py
```

17 ) To use python script from command line for one off predictions, can use:
```bash
python src/8-score-and-serve.py --model_choice <'base' or 'religio'> --input_sentence <sentence> 
```

18 ) To deploy model to local server, run from ROOT:
```bash
python app/app.py
```

```bash
curl -X POST http://127.0.0.1:8080/ -d model_choice="base" -d input_sentence=="test sentence"
```
 
19 ) To deploy model to Heroku:
- Create Heroku account and app
- Install Heroku command line on a local machine
- May need to `source .bash_profile` after adding `PATH=$PATH:$HOME/z/heroku/bin:$HOME/bin` to it
- run `heroku login
- run `heroku create`
- make sure build pack is present
    + may need to `pip freeze > requirements.txt` from your activate conda environment
- within this `requirements.txt` file, you may need to replace pytorch with the cpu version:
    + `https://download.pytorch.org/whl/cpu/torch-1.0.1.post2-cp37-cp37m-linux_x86_64.whl`
- run `git push heroku master`
- from separate command line, run 
```bash
curl -X POST https://religio-bert.herokuapp.com/ -d model_choice="base" -d input_sentence=="test sentence"
```


## Data

Christian/Jewish:
- King James Bible
- https://www.kaggle.com/tentotheminus9/religious-and-philosophical-texts

Hindu:
- Bhagavad Gita
- https://www.gutenberg.org/files/2388/2388-h/2388-h.htm

Islamic:
- The Quran
- https://www.kaggle.com/tentotheminus9/religious-and-philosophical-texts

Buddhist:
- The Gospel of Buddha
- https://www.kaggle.com/tentotheminus9/religious-and-philosophical-texts

Confucianism:
- Analects
- http://www.gutenberg.org/cache/epub/3330/pg3330.txt

Egyptian:
- Egyptian Book of the Dead
- https://www.gutenberg.org/files/28282/28282-8.txt

Mormon:
- Book of Mormon
- https://www.kaggle.com/tentotheminus9/religious-and-philosophical-texts

Tibetan:
- The Tibetan Book of the Dead
- https://archive.org/stream/TheTibetanBookOfTheDead/The-Tibetan-Book-of-the-Dead_djvu.txt

Stoic:
- Meditations
- https://www.kaggle.com/tentotheminus9/religious-and-philosophical-texts

## Misc

- Special thanks to Emilia Apostolova and Timo Wang for direction and help!