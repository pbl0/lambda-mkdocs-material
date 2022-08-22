
import os
from mdutils import MdUtils


def replace_numbers(string: str):
    # print(string)
    for i in range(0, 20):
        if len(str(i)) == 1:
            str_to_replace = '0' + str(i)
        else:
            str_to_replace = str(i)
        if str_to_replace in string:
            print(str_to_replace)
            string = string.replace(str_to_replace, '')
    return string

sections = os.listdir('docs')
sections.sort()
section_dict = {
    'title': '',
    'pages': []
}

nav = []

for page in sections:
    
    if '.md' in page or 'img' in page or 'css' in page or 'Historia' in page:
        pass
    else:
        pages = os.listdir('docs/'+page)
        pages.sort()
        section_dict = {
            'title': page,
            'pages':  pages
        }
        page_title = page.replace('-', ' ')
        mdFile = MdUtils(file_name='docs/' + page + '/index.md',title=page_title)
        link_list = []
        for item in pages:
            # item = item.replace('.md', '').replace('-',' ')
            item_name = item.replace('.md', '')
            item_name = item_name.replace('-' , ' ')
            item_name = replace_numbers(item_name)
            link = {
                'text': item_name,
                'url': './' + item
            }
            if 'index' not in item_name:
                inline_link = mdFile.new_inline_link(link['url'],link['text'])
                link_list.append(inline_link)


        mdFile.new_list(link_list)
        mdFile.create_md_file()
        nav.append(section_dict)




# print(nav)
        

