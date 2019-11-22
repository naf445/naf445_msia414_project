## Word2Vec:
- Context independent word embedding. The context does NOT matter for the embedding representation of the word. Intuitively this is not optimal. As the word "cell" can have many different meanings depending on the context it's being used in, the surrounding words, the type of document, etc...
- A predictive model which trains by either trying to pick the correct masked word given context words (CBOW) or the correct context words given a target word (s-gram). 

## Glove:
- Another context independent embedding vector algorithm

## LSTM:

## Bi-directional LSTM:

## Attention/Transformers: 

## ELMo:
- **E**mbeddings from **L**anguage **Mo**dels
- Bi-directional LSTM to learn **context-dependent** 
- Similar to how a deep network can use early layers to recognize edges and then recognize high level structures, the ELMo can use lower levels to recognize contexts and higher levels for definitions. 

## BERT:
- **B**idirectional **E**ncoder **R**epresentations from **T**ransformers
- Attention is all you need
- Transformer means that you don't need LSTM or any type of RNN anymore
- It's architecture means the lower layers can understand the context and send that to the higher layers which can make the word embeddings. 


_________________________________

NLP TEXT ANALYTICS 414 PROJECT

- Check DM’s with Emilia and timo about your idea
- Perhaps given a user input sentence, pick the most relevant sentence/paragraph from a religious text, or maybe the most relevant paragraph from each of the religious texts so the person has their choice of what to read
- Go back through and listen to these data skeptic episodes and take notes/official citations
-           ELMo, Attention Primer, The Transformer, Transfer Learning, BERT, BERT is Magic, BERT is shallow, SpanBERT, What BERT is Not, talking to GPT-2
- Research MultiFit, RoBERTa, XLM-R, ULM-fit
- Transformer: https://jalammar.github.io/illustrated-transformer/
- BERT: https://jalammar.github.io/illustrated-bert/
- Fine tuning Bert: https://medium.com/swlh/painless-fine-tuning-of-bert-in-pytorch-b91c14912caa 
- actual Attention paper: https://arxiv.org/abs/1706.03762
- actual BERT paper: https://arxiv.org/abs/1810.04805 

Using the https://github.com/huggingface/transformers hugging face transformers library, I fine-tuned a pre-trained BERT model on DD2 on my religious corpus. Intuitively, what we are doing here is:
- Normal BERT makes it’s goal to predict the masked word, and that is how it comes up with it’s language embeddings
- But this masked word will not be the same in religious corpuses, and words will get slightly different embeddings and relationships etc in a religious corpus. So I can take the already pre-trained BERT, and run a few more epochs of training, in order to generate my BERT-religion model which will be better for my task!
- actually i am not fine-tuning I am continuing the pre-training task
data: https://www.kaggle.com/datasets?search=bible 

pre-processing: https://medium.com/swlh/painless-fine-tuning-of-bert-in-pytorch-b91c14912caa 

train model on deepish

transfer model to jupyter hub and do everything else from there, not local!

to run on deepdish, you need to set environmental variable, 
and eventually run 

`source pre_train_settings.sh`

then

```hyperdash run -n 'BERT_pretrain' python pretraining.py --train_corpus $TRAIN_CORPUS --bert_model $BERT_MODEL --output_dir $OUTPUT_DIR --do_train --do_lower_case --cuda_device $CUDA_DEVICE```

and whatever other parameters you want to specify!

your conda environment is called

text-project

_____

text analytics project:

currently the only version is on GitHub
you will have to put a copy on jupyter hub and do all your editing and pre-processing and everything there and then you can go to deepdish and clone to there and you should have environments on both i guess! 

but essentially there’s 3 parts
- Part one on jupyter hub, grabbing and preprocessing data
- Part 2 on DD2, pre-train bert
- Part 3 on jupyter hub i guess or follow directions for how to do this, which is do rest of app set up and deployment

- BERT embeddings can take a lot of dimensions, they capture things like semantics or syntax, so you can actually do another transformation on the word embeddings from BERT to get the semantic embeddings, separate from the syntactical embeddings. But this is dependent on what you want to match a users input with!

