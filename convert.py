import xml.etree.ElementTree as ET
import os, re

tree = ET.parse('huuliharppufi.xml')
root = tree.getroot()
channel = root.find('channel')

os.makedirs('content/posts', exist_ok=True)
os.makedirs('content/pages', exist_ok=True)

for item in channel.findall('item'):
    title_el = item.find('title')
    title = title_el.text if title_el is not None and title_el.text else 'Untitled'
    
    post_type_el = item.find('{http://wordpress.org/export/1.2/}post_type')
    post_type = post_type_el.text if post_type_el is not None else 'post'
    
    status_el = item.find('{http://wordpress.org/export/1.2/}status')
    status = status_el.text if status_el is not None else 'publish'
    
    content_el = item.find('{http://purl.org/rss/1.0/modules/content/}encoded')
    content = content_el.text if content_el is not None and content_el.text else ''
    
    slug_el = item.find('{http://wordpress.org/export/1.2/}post_name')
    slug = slug_el.text if slug_el is not None and slug_el.text else title.lower().replace(' ', '-')
    slug = re.sub(r'[^a-zA-Z0-9_-]', '', slug)
    
    if status != 'publish' or post_type not in ['post', 'page']:
        continue
        
    folder = 'content/pages' if post_type == 'page' else 'content/posts'
    filename = os.path.join(folder, f"{slug}.md")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"---\ntitle: \"{title}\"\ntype: \"{post_type}\"\n---\n\n")
        f.write(content)

print("Muunnos valmis! Katso content/posts ja content/pages.")
