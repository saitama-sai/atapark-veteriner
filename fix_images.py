import os
import shutil

def main():
    image_dir = 'assets/images'
    source_dir = r"C:\Users\sait\.gemini\antigravity\brain\3686f355-e031-4d3d-ad24-91ec235f532f"
    html_file = 'index.html'

    # Mapping of missing img_N to generated filenames
    mapping = {
        'img_2.jpg': 'cute_dog_hero_1776796551196.png',
        'img_3.jpg': 'cute_cat_display_1776796616105.png',
        'img_5.jpg': 'cute_dog_display_1776796602538.png',
        'img_6.jpg': 'vet_clinic_hero_1776796588451.png',
        'img_8.jpg': 'pets_landscape_1776796632843.png',
        'img_9.jpg': 'teddy_bear_about_1776796646846.png',
        'img_10.jpg': 'cute_cat_hero_1776796573273.png',
    }

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    for old_img, new_img_name in mapping.items():
        # Copy the file
        src_path = os.path.join(source_dir, new_img_name)
        new_relative_path = f'assets/images/{new_img_name}'
        dst_path = os.path.join(image_dir, new_img_name)
        
        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
            # update HTML
            old_relative_path = f'assets/images/{old_img}'
            content = content.replace(old_relative_path, new_relative_path)
            print(f"Replaced {old_relative_path} with {new_relative_path}")

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("index.html updated successfully with local generated images.")

if __name__ == '__main__':
    main()
