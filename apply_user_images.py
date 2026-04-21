import os
import shutil

def main():
    root_dir = r"C:\Users\sait\Downloads\stitch_annotated_image_modifier"
    image_dir = os.path.join(root_dir, 'assets', 'images')
    artifacts_dir = r"C:\Users\sait\.gemini\antigravity\brain\3686f355-e031-4d3d-ad24-91ec235f532f"
    html_file = os.path.join(root_dir, 'index.html')

    mappings = {
        'cute_cat_display_1776796616105.png': 'media__1776797942969.png',
        'cute_dog_display_1776796602538.png': 'media__1776797952039.png',
        'pets_landscape_1776796632843.png': 'media__1776797970592.png',
        'vet_clinic_hero_1776796588451.png': 'media__1776797990395.png',
        'cute_dog_hero_1776796551196.png': 'media__1776798000529.png',
        'teddy_bear_about_1776796646846.png': 'media__1776798000529.png', # Use dog/cat heart for teddy too
        'cute_cat_hero_1776796573273.png': 'media__1776797990395.png'  # Use vet for the other hero too
    }

    # Copy files
    for old_name, user_media_name in mappings.items():
        src_path = os.path.join(artifacts_dir, user_media_name)
        dst_path = os.path.join(image_dir, user_media_name)
        if os.path.exists(src_path) and not os.path.exists(dst_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied {user_media_name} to assets")

    # Replace in HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    for old_name, user_media_name in mappings.items():
        old_path = f"assets/images/{old_name}"
        new_path = f"assets/images/{user_media_name}"
        content = content.replace(old_path, new_path)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully linked user media files in index.html!")

if __name__ == '__main__':
    main()
