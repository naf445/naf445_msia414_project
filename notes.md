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

## The Transformer
- https://jalammar.github.io/illustrated-transformer/

## Attention
- https://arxiv.org/abs/1706.03762

## BERT:
- **B**idirectional **E**ncoder **R**epresentations from **T**ransformers
- Attention is all you need
- Transformer means that you don't need LSTM or any type of RNN anymore
- It's architecture means the lower layers can understand the context and send that to the higher layers which can make the word embeddings.
- https://jalammar.github.io/illustrated-bert/
- https://arxiv.org/abs/1810.04805 

## DM's w/ Emilia / Timo

- Using the https://github.com/huggingface/transformers hugging face transformers library, I fine-tuned a pre-trained BERT model on DD2 on my religious corpus. Intuitively, what we are doing here is:
- Normal BERT makes it’s goal to predict the masked word, and that is how it comes up with it’s language embeddings
- But this masked word will not be the same in religious corpuses, and words will get slightly different embeddings and relationships etc in a religious corpus. So I can take the already pre-trained BERT, and run a few more epochs of training, in order to generate my BERT-religion model which will be better for my task!
- Actually i am not fine-tuning I am continuing the pre-training task
- BERT embeddings can take a lot of dimensions, they capture things like semantics or syntax, so you can actually do another transformation on the word embeddings from BERT to get the semantic embeddings, separate from the syntactical embeddings. But this is dependent on what you want to match a users input with!


 

## Data Skeptic
- ELMo
- Attention Primer
- The Transformer
- Transfer Learning
- BERT
- BERT is Magic
- BERT is Shallow
- SpanBERT
- What BERT is Not, 
- Talking to GPT-2

## MultiFit:

## Roberta:

## XLM-R: 

## ULM-Fit:

## GPT-2:

_____
## Deploying my model with a REST api via flask and heroku!
Following : https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166
And: https://towardsdatascience.com/designing-a-machine-learning-model-and-deploying-it-using-flask-on-heroku-9558ce6bde7b

- We are using Flask RESTful
- We need a python script which constructs our app
- In this script we need to accopmlish some things
    + Create an app and api instance
    + We need to load in our model object, however we see fit
    + Create an argument parser, but this argparse is for request parsing, not just for arg parsing
    + We need to create a new class which inherits from the flask_restful class `resource`, this is the meat of Flas RESTful api's.
    + This class will have methods which correspond to the HTTP `GET`/`PUT`/`POST` etc...
    + For example, in a method we define called `get` in this class, we could provide directions on how to handle the user’s input and how to package a JSON object to be returned.
    + We must assign the resource to URLs, so we can assign our resource created to the base URL
    + In an if __name__ == '__main__' chunk we need an app.run() call


