Collection of files and code used for my thesis: 

# Exploring the Potential of Linguistic Knowledge to Enhance Wayúunaiki–Spanish Neural Machine Translation

## Code as of March 2023

### Thesis

We present the first neural machine translation system for the low-resource language pair Wayúunaiki–Spanish and explore strategies to inject linguistic knowledge into the model to improve translation quality. We explore a wide range of methods and combine complementary approaches. Results indicate that incorporating linguistic information through linguistically motivated subword segmentation, factored models, and pretrained embeddings helps the system to generate improved translations, with the segmentation contributing most. In order to evaluate translation quality in a general domain and go beyond the available religious domain data, we gather and make here available a new test set and supplementary material. Although translation quality as measured with automatic metrics is low, we hope these resources will facilitate and support further research on Wayúunaiki.


## Paper

### arXiv
A short version of the thesis has been published [Enriching WayúnaikiSpanish Neural Machine Translation with Linguistic Information](https://aclanthology.org/2023.americasnlp-1.9) (Graichen et al., AmericasNLP 2023). Please note that the naming deviates!


### Slides presentation

## Dataset
The data used in this work was exactly processed as described in the paper and can be found in the according directory Dataset.


## Models

### Hyperparamter

We report [our hyperparameters](https://docs.google.com/spreadsheets/d/1A6sTnDGqX4cKL07LO5XxKhAsR7Iq7wk7wLSmZtTUB1Y/edit?usp=sharing) for training the models with the Marian Interface (v.11) and list the explored hyperparameters of the baseline search.

### Notebook
tobeupdated:)

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


## Publications

Please, use the following bibtex entry when citing this research work, tobeupdated:)

@inproceedings{graichen-van-Genabith-espana-bonet-2023,<br>
    title = "Enriching Wayúunaiki–Spanish Neural Machine Translation with Linguistic Information",<br>
    author = "Graichen, Nora and van Genabith, Josef and Espa{\~n}a-Bonet, Cristina",<br>
    booktitle = "Proceedings of the Workshop on Natural Language Processing for Indigenous Languages of the Americas (AmericasNLP)",<br>
    month = 07,
    year = "2023",
    address = "Toronto, Canada",<br>
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.americasnlp-1.9",
    pages = "67--83"
}


## Acknowledgements
Thanks to two supportive natives of the Wayúu community, we were able to analyze our translation results beyond automatic evaluation scores. Both bilingual speakers are non-professional interpreters and translators that helped voluntarily. Adolfo y señora Gladys: ¡Muchas gracias por su ayuda con las traducciones, interés y confianza en el proyecto!
We thank Jörg Steffen for the integration of the Wayúunaiki–Spanish system in TransIns.

