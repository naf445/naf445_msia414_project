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

### Contonue BERT pre-training


## Setting Up the App from Start 2 Finish

### CPU Machine:

1)
```bash
source activate text-project-cpu
```

2)
```bash
python 1-get-data.py
```

3)
```bash
kaggle datasets download tentotheminus9/religious-and-philosophical-texts --unzip --path data/raw_data/
```

4)
```bash
mv data/raw_data/35895-0.txt data/raw_data/buddha_raw.txt;
mv data/raw_data/pg10.txt data/raw_data/bible_raw.txt;
mv data/raw_data/pg17.txt data/raw_data/mormon_raw.txt;
mv data/raw_data/pg2680.txt data/raw_data/meditations_raw.txt;
mv data/raw_data/pg2800.txt data/raw_data/quran_raw.txt;
```

5 )
```bash
python 2-create-combined-corpus.py
```

6 ) Send files to GPU machine

### GPU Machine:

7 )
```bash
source activate text-project-gpu
```

8 ) 
```bash
source pre_train_settings.sh
```

9 )
```bash
hyperdash run -n 'BERT_pretrain' python pretraining.py --train_corpus $TRAIN_CORPUS --bert_model $BERT_MODEL --output_dir $OUTPUT_DIR --do_train --do_lower_case --cuda_device $CUDA_DEVICE
```

10 ) Send pretrained religioBERT to CPU

### CPU Machine:

- XXXXXXXXXXXXXXX

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