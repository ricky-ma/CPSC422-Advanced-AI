import re

corpus = '''
(S (NP /John/) (VP (VP (V /plays/) (NP /soccer/)) (PP (P /at/) (NP /school/))))
(S (NP /John/) (VP (VP (V /plays/) (NP /soccer/)) (PP (P /at/) (NP /school/))))
(S (NP /John/) (VP (VP (V /plays/) (NP /soccer/)) (PP (P /at/) (NP /school/))))
(S (NP /John/) (VP (V /plays/) (NP (NP /soccer/) (PP (P /at/) (NP /school/)))))
(S (NP /John/) (VP (V /plays/) (NP /soccer/)))
(S (NP /John/) (VP (V /plays/) (NP /soccer/)))
(S (NP /John/) (VP (V /plays/) (NP /soccer/)))
(S (NP /John/) (VP (V /plays/) (NP /soccer/)))
(S (NP /John/) (VP (V /plays/) (NP /soccer/)))
(S (NP /John/) (VP (V /plays/) (NP /soccer/)))
'''

total_s = corpus.count('(S ')
total_vp = corpus.count('(VP ')
total_pp = corpus.count('(PP ')
total_np = corpus.count('(NP ')
total_v = corpus.count('(V ')
total_p = corpus.count('(P ')
print(total_s, total_vp, total_pp, total_np, total_v, total_p)

words = set([x for x in corpus.split('/') if not ' ' in x and not ')' in x])
print(words)

# words = re.findall(r'\(.+?\)', corpus)
# words = [x for x in words if x.count('(') == x.count(')')]
# print(words)

# Get all substrings of the corpus
phrases = [corpus[i: j] for i in range(len(corpus))
           for j in range(i + 1, len(corpus) + 1)]

# Filter results to contain only valid phrases
phrases = [x for x in phrases if
           x.count('(') == x.count(')') and
           '\n' not in x and
           x[0] == '(' and
           x[-1] == ')' and
           x.count('(') % 2 == 1]
# print(phrases)
print(len(phrases))

counts = {}
for phrase in phrases:
    # Single word
    if phrase.count('(') == 1:
        part_of_speech = re.search('\((.*) ', phrase).group(1)
        word = re.search('/(.*)/', phrase).group(1)
        try:
            counts[part_of_speech + '_' + word] += 1
        except KeyError as e:
            counts[part_of_speech + '_' + word] = 1
print(counts)