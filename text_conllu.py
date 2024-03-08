# %%

from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,

    Doc
)
emb = NewsEmbedding()
segmenter = Segmenter()
morph_vocab = MorphVocab()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)

text = 'Открытки “С днем 8 Марта” в СССР начали выпускать лишь с 1952 года.\n\nКаждый год выпускалось от 10 до 80 видов открыток. Над их созданием трудились лучшие художники, выпускались специальные тематические серии и целые коллекционные альбомы.'

# %%

doc = Doc(text)

doc.segment(segmenter)
print(doc.sents)
# %%
doc.tag_morph(morph_tagger)
doc.sents[0].morph.print()
# %%
doc.parse_syntax(syntax_parser)
print(doc.tokens[:5])
doc.sents[0].syntax.print()
# %%
doc.tokens[0].lemmatize(morph_vocab)
doc.tokens[0]
# %%
