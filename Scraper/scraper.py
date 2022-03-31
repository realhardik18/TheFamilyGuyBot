# getting links of all clips
import re

f = open("requested data.txt", "r")
shortcodes = ''
for x in f:
    shortcodes = re.findall(r"([^.]*?shortcode[^.]*\.)", x)
valid_shortcodes = []
for shortcode in shortcodes:
    short_code_list = shortcode.split(',')
    for short_code_element in short_code_list:
        if 'shortcode' in short_code_element:
            valid_shortcodes.append(short_code_element[13:-1])

db = open("db.txt", "a+")
for code in valid_shortcodes:
    db.write(f'https://www.instagram.com/p/{code}/\n')
