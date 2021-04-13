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

totals = {}
for pos in ['S', 'VP', 'PP', 'NP', 'V', 'P']:
    totals[pos] = corpus.count('(' + pos + ' ')
print(totals)

words = set([x for x in corpus.split('/') if not ' ' in x and not ')' in x])
print(words)

# Get all substrings of the corpus
phrases = [corpus[i: j] for i in range(len(corpus))
           for j in range(i + 1, len(corpus) + 1)]

# Filter results to contain only valid phrases
phrases = [x for x in phrases if
           x.count('(') == x.count(')') and
           '\n' not in x and
           x[0] == '(' and
           x[-1] == ')' and
           x.count('(') % 2 == 1 and
           (x[3] == '(' or x[4] == '(' or x[5] == '(' or x.count('(') == 1)]
print(len(phrases))

counts = {}
for phrase in phrases:
    # Get main part of speech from phrase
    part_of_speech, *_ = re.findall('\((.*?) ', phrase)

    # Single word
    if phrase.count('(') == 1:
        word = re.search('/(.*)/', phrase).group(1)
        try:
            counts[part_of_speech + '_' + word] += 1
        except KeyError as e:
            counts[part_of_speech + '_' + word] = 1

    # Get count of two-part phrase
    else:
        # TODO: fix calculation for V_VP_PP
        phrase = phrase[len(part_of_speech) + 2:]
        pos1, *_ = re.findall('\((.*?) ', phrase)
        phrase = phrase[len(pos1) + 2:]
        pos2, *_ = re.findall('\((.*?) ', phrase)
        try:
            counts[part_of_speech + '_' + pos1 + '_' + pos2] += 1
        except KeyError as e:
            counts[part_of_speech + '_' + pos1 + '_' + pos2] = 1
print(counts)

grammar = {}
for pos in counts.keys():
    main_pos = pos.split('_')[0]
    grammar[pos] = counts[pos]/totals[main_pos]
print(grammar)
