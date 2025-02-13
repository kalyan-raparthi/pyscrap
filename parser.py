# HTML PASER FUNTIONS

\s = '''<h1>HELLO WORLD. </h1>'''

def get_tag(s, cur_pos):
    i = cur_pos
    while(i < len(s) - cur_pos):
        c = s[i]    
        if (c == '<'):
            i += 1
            cur_tag = ''
            while(i < len(s) and s[i] != '>'):
                cur_tag += s[i]
                i += 1
            if cur_tag:
                return [cur_tag, i]
        i += 1

START_POS = 0

tag_1 = get_tag(s, START_POS)
tag_2 = get_tag(s, tag_1[1])

print(tag_1[0], tag_1[1])
print(tag_2[0], tag_2[1])
