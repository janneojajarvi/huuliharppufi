import os, re

content_dir = "content"
count = 0

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    front_matter = parts[1]
                    body = parts[2]

                    if re.search(r"^description\s*:", front_matter, re.MULTILINE):
                        continue

                    title_match = re.search(r"^title\s*:\s*[\"\x27](.*?)(?<!\\)[\"\x27]", front_matter, re.MULTILINE)
                    if not title_match:
                        title_match = re.search(r"^title\s*:\s*(.*)$", front_matter, re.MULTILINE)
                    
                    title = title_match.group(1).strip("\"'\x27") if title_match else "Huuliharppu-sivusto"

                    clean_body = re.sub(r"{{<.*?>}}", "", body)
                    clean_body = re.sub(r"#+.*", "", clean_body)
                    paragraphs = [p.strip() for p in clean_body.split("\n\n") if p.strip() and not p.strip().startswith("-") and not p.strip().startswith("*")]
                    
                    if paragraphs:
                        desc_text = paragraphs[0].replace("\n", " ").replace("\"", "").replace("\x27", "").strip()
                        desc_text = re.sub(r"\s+", " ", desc_text)[:130]
                    else:
                        desc_text = ""

                    if len(desc_text) < 10:
                        desc_text = f"Tietoa aiheesta {title} - Huuliharppu.fi"

                    new_front_matter = front_matter.rstrip() + f'\ndescription: "{desc_text}"\n'
                    new_content = "---" + new_front_matter + "---" + body

                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1

print(f"Lisätty turvallinen description {count} tiedostoon.")
