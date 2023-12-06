# food-review-summarizer

This repository is for the Food Review Summarization project.

</br>
### <u> data-processing </u>

extract_reviews.ipynb
* Extracts reviews from YELP's academic dataset. 
* Utilizes pandas library to manipulate and filter dataset (cleaning, content thresholding, usefulness sorting)
* Outputs filtered reviews into csv file

final_reviews.csv
* Contains filtered reviews where each row corresponds to a restaurant
* Each row has 10 reviews concatenated into a string

</br>
### <u> summarization-models </u>

#### This directory contains many files used for testing various models. Here are some of the noteworthy aspects of this directory:

Experimented with different model architectures and types
* Summarization models
    * Solely designed for the summarization task (extractive or abstractive summarization)
* Sequence-to-Sequence models
    * Useful for converting input sequences (text) into output sequences (summaries)
    * Very popular in wide range of natural language processing tasks
* Transformer models
    * Efficient for capturing long-range dependencies in data
    * Good for summarization tasks that require understanding context over extended text (self-attention mechanism)
* Question Answering models
    * Experimented adapting QnA models to summarization task
    * Framed summary generation as a question-answering problem, where the answer is the summary of the input text
* Text Generation
    * Generation of new text employed for abstractive summarization
    * Created concise summaries while generating new language
* Text2Text Generation
    * More generalized approach to text generation, models are more equipped to handle various text transformations
    * Framed summarization task as converting one text into another
* Conversational
    * Good for more dynamic, interactive summarization process
    * Chat-bots perform better with varied queries and give summaries in conversational manner

inference_summaries.ipynb
* Creates of dataset of reviews mapping to generated summaries, per restaurant
* Uses Quantization to reduce precision of weights and activations of model
    * Lower number of bits used (sacrifice of accuracy)
    * Reduction of memory footprint and computational requirements of model
* Includes transformation of input text into tensor of encoded tokens for model to interpret text
* Includes dynamic attention masking to assign weights to tokens, guiding model's focus

inferenced_summaries.csv
* Contains reviews mapped to generated summaries corresponding to respective restaurants


</br>
### <u> model-creation </u>

model_fine_tuning.ipynb
* Code for fine-tuning a smaller summarization model

* Setup
    * Randomized batched split of inferenced_summaries dataset into train, validation, test sets
    * Uses tokenization function to pad/truncate reviews so that shapes are same when passed into model

* Training
    * Uses Trainer API with Stochastic Gradient Descent
    * Uses "accuracy" evaluation metric
    * Evaluation metric function
        * Final activation function converts "log odds of probability" (logits) to probability distribution
        * "accuracy" metric used in evaluation along with ground truth labels

</br>
### <u> front-end </u>

This directory includes files for the front-end of our product. We utilize Flask to run our chrome web extension.

