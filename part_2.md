## Nathan Franklin
## Text Project, Part 2:
Survey relevant academic literature on the topic and write a one-page or less summary of findings. The survey should include a summary of various significant approaches on the task, including citations. Refer to the “Related Literature” section of any of the academic papers discussed in class as an example of what the literature survey should contain.  

----
This project's main technical approach is focused on extracting vectorized representations of words and/or sentences. With this in mind, I did some research into different ways to accomplish this task.

One of the most popular approaches to this task in the NLP community was using either a pre-trained word2vec model or a custom trained word2vec model, as [1] Mikolov et al. (2013) explains. The approach taken by these researchers was to build a neural network, which after training, would be able to produce unique vectors for any word used in its training vocabulary. These embeddings are word-by-word, and cannot be extended directly to sentence embeddings, one drawback of this method. The embeddings generated also are not context-dependent, meaning the word "cell" (or any other homonym groups) will get only one vector representation, where optimally we could get different vector representations for its different uses in everyday language (context-dependent). Word2vec took a creative approach to generate these embeddings, using 2 different model architexture and vector extraction strategies. The CBOW model took as input words which appeared near a masked word, and tried to predict this masked word. The skip-gram model took as input one word, and trued to predict the context words around it. 

An improvement in ways over word2vec came from [2] Peters et al. (2018) with the introduction of ELMo. As previously noted, one of the weaknesses of word2vec was the context-independent nature of the embeddings. ELMo uses a bi-directional LSTM structure in order to be able to take into account the context of a word being used in a sentence. Similar to how a deep learning network uses earlier layers to recognize edges and simpler structure, and later layers to recognize more complex structures, the ELMo architecture can be thought of as using its earlier layers to get the context of a word in a sentence, and then the later layers to get the specific definition for that word in a given context.   

While ELMo, was an improvement over word2vec, BERT, layed out in [3] Devlin et al. (2018), is the latest improvement to this strategy. The context-dependent embeddings are retained, while the complex, bi-directional-lstm architecture is eschewed in favor of a simpler Transformer approach using language attention. 

Inspired by the idea of applying BERT to a specific knowledge/nlp topic in order to achieve better understanding as displayed in [4] Beltagy et al (2019) with their deployment of SciBERT, I wanted to follow a similar approach. Based on this idea, in combination of BERT seeming to perform the best and be the simplest model to implement with robust online resources, I decided to continue pre-training BERT on my own religious text corpus in order to train and deploy ReligioBERT.

---
[1] Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., and Dean, J. (2013b). Distributed representations of words and phrases and their compositionality. In Advances in Neural Information Processing Systems, pages 3111–3119.

[2] Matthew E Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer. 2018b. Deep Contextualized Word Representations. arXiv preprint arXiv:1802.05365.

[3] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of Deep Bidirec- tional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805, 2018.

[4] Iz Beltagy, Kyle Lo, and Arman Cohan. 2019. Scibert: Pretrained Language Model for Scientific Text. In EMNLP.