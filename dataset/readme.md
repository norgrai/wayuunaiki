## Data Collection

### Parallel corpora
We use the only online parallel corpus for Wayúunaiki and Spanish available in the Tatoeba MT Challenge, version v2021-08-07
[[Tiedemann, 2020]](https://aclanthology.org/2020.wmt-1.139) The corpus consists of ~43k sentence pairs, which we divided
into a train, development, and test set. The original partitions are labeled with RAW. We provide the [BPE](https://github.com/rsennrich/subword-nmt) data here (with 4k merge operations with separate vocabularies) under bitext.

Edit: The new general domain test data set is available upon request (due to its usage in an MT class at the UdS)

### Monolingual corpora
We extracted Wayúunaiki text from the translation of the book [_The Little Prince_](https://www.academia.edu/37583043/P�rinsipechonkai) by Antoine de Saint-Exupery. We also extract from a bilingual Spanish–Wayúunaiki
dictionary [[David M. Captain, 2005]](https://www.academia.edu/9990081/DICCIONARIO_BÁSICO_ILUSTRADO_WAYUUNAIKI_ESPAÑOL_ESPAÑOL_WAYUUNAIKI) entries in Wayúunaiki, which we used, one token per line,
as additional data.

### Supplementary Material
Some of our experiments require supplemental information in the form of linguistic annotations, or dictionaries. We
extracted morphological analyses of verb conjugations in Wayúunaiki from the work of [Álvarez (2017)](https://www.academia.edu/37617681/Manual_de_la_lengua_wayuu) and [Lluís Simarro Lacabra (2014)](https://ieslluissimarro.org/castella/files/2014/02/An%C3%A1lisis-morfol%C3%B3gico-de-la-palabra.pdf) to guide the semi-supervised training of the segmentation models (Prefix-Root-Postfix-Encoding and FlatCat).

We manually annotate the morph categories prefix, stem, and suffix of 26 words in Wayúunaiki and 91 in Spanish for the Morfessor Flatcat approach. To
perform Prefix-Root-Postfix-Encoding, we created two heuristics that contain the common suffixes, prefixes and endings for the Wayúu and Spanish languages.

We provide the POS tag annotated data for the BPE data under ling-factors, fullfilling the standards of [Marian](https://marian-nmt.github.io/docs/api/factors), as well as the factored vocabulary.
