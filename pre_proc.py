import re
import string
import sys

# STEP 1
ignore = False
sentences_file = open('sentences_temp.txt', 'w')

with open(sys.argv[1], 'r') as input_file:

    for line in input_file:

        # Ignore title tag contents
        if '<t>' in line:
            ignore = True
        elif '</t>' in line:
            ignore = False

        if line[0] != '<' and not ignore:

            # Discarding annotations
            token = line.split()[0]

            # Adding blank spaces
            # the reason for this condition is that string.punctuation also contains these symbols
            if token[0] in '({[':
                token_out = ' ' + token
            elif token[0] in string.punctuation:
                token_out = token
            else:
                token_out = ' ' + token

            # Adding break line
            token_out = token_out + '\n' if token_out[0] in '.?!' else token_out

            sentences_file.write(token_out)

# STEP 2
large_sent_file = open('large_sent_temp.txt', 'w')
minimum_len = 2 if len(sys.argv) < 4 else int(sys.argv[3])

with open('sentences_temp.txt', 'r') as sentences_file:

    for line in sentences_file:

        tokens = line.split()

        # Removes sentences with less than 'minimum_len' words and
        # removes three final dots (these are not suspension points!)
        if line != '...\n' and len(tokens) >= minimum_len:
            large_sent_file.write(line)

# STEP 3
output_file = open(sys.argv[2], 'w')

# Matches '« example example »'
regex1 = re.compile(r'( «|« |«| »|» |»)')
# Matches '( '
regex2 = re.compile(r'\(\s')
# Matches two or more blank spaces
regex3 = re.compile(r' {2,}')
# Matches blank spaces at the start
regex4 = re.compile(r'^ ')

output_file = open('x.txt', 'w')

with open('t.txt', 'r') as file:

    for line in file:

        line = regex1.sub('', line)
        line = regex2.sub('(', line)
        line = regex3.sub(' ', line)
        line = regex4.sub('', line)

        output_file.write(line)
