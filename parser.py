s = '''<h1>HELLO WORLD. </h1>'''

def next_tag(s, cur_pos):
    i = cur_pos
    while(i < len(s)):
        c = s[i]    
        if c == '<':  # Found the start of a tag
            i += 1
            cur_tag = ''
            while(i < len(s) and s[i] != '>'):  # Collect the tag until '>'
                cur_tag += s[i]
                i += 1
            i += 1  # To skip the '>' character
            if cur_tag and not cur_tag.startswith('/'):  # Ensure it's an opening tag
                return [cur_tag, i]  # Return the tag and the new position
        i += 1
    return [None, i]  # No more tags found

def get_content_next(s, tag, pos):
    content = ''
    i = pos
    while(i < len(s)):
        c = s[i]
        
        # Look for the next opening tag (it starts with '<')
        if c == '<':
            next_tag_info = next_tag(s, i)
            next_tag_name = next_tag_info[0]
            if next_tag_name:
                # Skip closing tags (they start with '</')
                if next_tag_name.startswith('</'):
                    i = next_tag_info[1]  # Move past the closing tag
                    continue
                
                # Stop capturing content when the next opening tag is encountered
                if next_tag_name == f'{tag}':
                    break
            else:
                break
        else:
            content += c
        i += 1
    return content

# Example usage:
start_pos = 0
while start_pos < len(s):
    tag_info = next_tag(s, start_pos)
    if tag_info[0]:
        tag = tag_info[0]
        start_pos = tag_info[1]
        
        # Only process opening tags (not closing tags)
        if not tag.startswith('</'):
            content = get_content_next(s, tag, start_pos)
            print(f'Tag: {tag}, Content: "{content}"')
    else:
        break

