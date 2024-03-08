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


def format_feats(feats):
    if not feats:
        return '_'

    return '|'.join(
        '%s=%s' % (_, feats[_])
        for _ in sorted(feats)
    )

# %%
def conllu(text):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    for token in doc.tokens:
        token.lemmatize(morph_vocab)

    for sent_id, sent in enumerate(doc.sents, 1):
        yield(f'# text = {sent.text}')
        for token in sent.tokens:
            feats = format_feats(token.feats)
            id = token.id.removeprefix(f'{sent_id}_')
            head_id = token.head_id.removeprefix(f'{sent_id}_')
            yield(f'{id}\t{token.text}\t{token.lemma}\t{token.pos}\t_\t{feats}\t{head_id}\t{token.rel}\t')
            # f'\tTag={token.tag}'  # misc = ner tag
        yield('')
# %%
c = '\n'.join([x for x in conllu(text)])
open('1.conllu', 'w').write(c)
print(c)
# %%
