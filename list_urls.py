import os
import re

def get_slug_or_filename(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        # Etsitään permalink tai slug front matterista
        match_slug = re.search(r'^slug:\s*["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
        if match_slug:
            return match_slug.group(1).strip()
        match_url = re.search(r'^url:\_?["\']?([^"\'\n]+)["\']?', content, re.MULTILINE)
        if match_url:
            return match_url.group(1).strip()
    # Jos slugia ei löydy, käytetään tiedostonimeä
    filename = os.path.basename(filepath).replace('.md', '')
    return filename

print("\n--- CONTENT/PAGES (STAATTISET SIVUT) ---")
pages_dir = 'content/pages'
if os.path.exists(pages_dir):
    for root, dirs, files in os.walk(pages_dir):
        for file in sorted(files):
            if file.endswith('.md'):
                path = os.path.join(root, file)
                slug = get_slug_or_filename(path)
                rel_path = os.path.relpath(path, 'content')
                print(f"Tiedosto: {rel_path}  -->  URL: /{slug}/ tai /{rel_path.replace('.md', '')}/")

print("\n--- CONTENT/POSTS (ARTIKKELIT) ---")
posts_dir = 'content/posts'
if os.path.exists(posts_dir):
    for file in sorted(os.listdir(posts_dir))[:10]:
        if file.endswith('.md'):
            print(f"Postaus: {file}  -->  URL: /posts/{file.replace('.md', '')}/")
