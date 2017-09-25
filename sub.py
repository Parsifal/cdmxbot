import nltk

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

def process_tweet(status):
    print(u'{1} (https://twitter.com/{0}/status/{2}) - @{0}'.format(
        status.user.screen_name,
        status.text[:20] + '...' if len(status.text) > 10 else status.text,
        status.id_str
    ))

def extract_names(text):
    result = []
    sentences = nltk.sent_tokenize(text)
    # tokenised_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    for chunk in chunked_sentences:
        if hasattr(chunk, 'node') and chunk.node:
            if chunk.node == 'NE':
                result.append(' '.join([child[0] for child in chunk]))
            else:
                for child in chunk:
                    result.extend(extract_names(child))
    return result
