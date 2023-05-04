Collection of files and code used for my thesis: 

# Exploring the Potential of Linguistic Knowledge to Enhance Wayúunaiki–Spanish Neural Machine Translation

## Code as of March 2023

### Thesis
This work was done as a part of
As such, we make transparent the tools and code developed by the community.
Farther more, it is probable that this work will be merged into that [code base]() and continued from there.
Thus, be sure to check there for the most recent form of this work.

## Paper

### arXiv
A short version of the thesis will be made available on [arXiv](). Please note that the naming deviates!

### Slidea presentation

## Dataset
The data used in this work was exactly processed as described in the paper and can be found in the according directory Dataset.


## Models

### Hyperparamter

We report [our hyperparameters](https://docs.google.com/spreadsheets/d/1A6sTnDGqX4cKL07LO5XxKhAsR7Iq7wk7wLSmZtTUB1Y/edit?usp=sharing) for training the models with the Marian Interface (v.11) and list the explored hyperparameters of the baseline search.

## Segmentation

In this work we applied various unsupervised and semisupervised subword segmentation methods to enrich the data used to train a transformer-based
NMT model with linguistic information. We apply the following segmentation methods:
- Byte-Pair Encoding (BPE) [[Sennrich et al., 2016]](https://doi.org/10.18653/v1/P16-1162)
- with applied Dropout [[Provilkov et al., 2019]](https://doi.org/10.18653/v1/2020.acl-main.170)
- unigram language model for segmentation [[Kudo et al., 2018]](https://doi.org/10.18653/v1/P18-1007)
- Prefix-Root-Postfix-Encoding (PRPE) [[Zuters et al. 2018]](https://doi.org/10.1007/978-3-319-97571-9_23)
- FlatCat [[Grönroos et al. 2014]](https://aclanthology.org/C14-1111) Morfessor variant

## Embeddings
We only explored transfer learning approaches by using pretrained word embeddings.  For this we train fastText embeddings [[Bojanowski et al., 2016]](https://doi.org/10.1162/tacl_a_00051). Transfer learning should be explored further.

## Factors
We extended the architecture of the standard baseline model with subword segmentation by adding linguistic information in the form of POS tag factors and/or supplying the system with pretrained embeddings.
