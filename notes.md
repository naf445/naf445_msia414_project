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


