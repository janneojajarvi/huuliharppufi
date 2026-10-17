import xml.etree.ElementTree as ET

try:
    tree = ET.parse('huuliharppufi.xml')
    root = tree.getroot()
    channel = root.find('channel')

    print("\n--- KOPIOI NÄMÄ RIVIT config.toml -TIEDOSTOOSI ---\n")
    
    weight = 1
    for item in channel.findall('item'):
        post_type_el = item.find('{http://wordpress.org/export/1.2/}post_type')
        if post_type_el is not None and post_type_el.text == 'nav_menu_item':
            title_el = item.find('title')
            title = title_el.text if title_el is not None and title_el.text else 'Linkki'
            
            # Etsitään linkin kohdeosoite tai slug
            slug_el = item.find('{http://wordpress.org/export/1.2/}post_name')
            slug = slug_el.text if slug_el is not None else ''
            
            print(f"[[menu.main]]")
            print(f"  name = '{title}'")
            print(f"  url = '/{slug}/'")
            print(f"  weight = {weight}\n")
            weight += 1

except FileNotFoundError:
    print("Virhe: huuliharppufi.xml -tiedostoa ei löytynyt kansiosta.")
