## Nathan Franklin
## Text Project, Part 3:
Determine and describe the approach/method you have chosen on your choice of NLP topic/task. Note that you might need to try out several techniques before settling on an approach. Run relevant experiments and record results. Write a one-to-two page description of 1) the method and 2) the results of your experiments.

---
For my NLP task, I have chosen to work with vector representations of words/sentences, specifically using the BERT implementation provided by the Huggingface Transformers implementation of BERT (https://github.com/huggingface/transformers).

My experiments involve comparing the performance of the uncased base BERT pre-trained model (12-layer, 768-hidden, 12-heads, 110M parameters) with a custom ReligioBERT model which begins with this baseBERT model and continues the pre-training step on a religious corpus. This religious corpus consisted of 10 religious texts, with details for each document found in the `README` of the code repository. The motivation for this approach comes from SciBERT, which trained a BERT model on a corpus of scientific documents, in order to get word embeddings which were more specialized for the types of vocabulary, syntax, and other language characteristics from this scientific world. Because eventually I wanted my word embeddings to be good at applying to religious words and concepts, and these words/concepts may not have been plentiful in the original corpus which BERT was trained on, I commenced with these further pre-training steps. Below is a comparison of how baseBERT compared with my ReligioBERT model in a couple of tasks.

### TSNE Visualizations

#### baseBERT

#### ReligioBERT

### Religious Text Recommendations

#### baseBERT

#### ReligioBERT
