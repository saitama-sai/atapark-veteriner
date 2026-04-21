import urllib.request
import re
import os
import hashlib

def main():
    html_file = 'code.html'
    output_file = 'index.html'
    image_dir = 'assets/images'
    
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    urls = set(re.findall(r'https://lh3.googleusercontent.com/[^\s"\'\\]+', content))
    
    url_map = {}
    for i, url in enumerate(urls):
        ext = '.jpg'
        # Assign a simpler name or hash
        filename = f'img_{i+1}{ext}'
        filepath = os.path.join(image_dir, filename)
        
        print(f"Downloading {url[:50]}... to {filepath}")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
            url_map[url] = filepath.replace('\\', '/')
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            
    # Replace URLs
    new_content = content
    for url, local_path in url_map.items():
        new_content = new_content.replace(url, local_path)
        
    # Append missing script tag before </body>
    script_js = """
<script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('#heroSlides .slide');
    
    function moveSlide(direction) {
        if(!slides.length) return;
        currentSlide += direction;
        if(currentSlide < 0) currentSlide = slides.length - 1;
        if(currentSlide >= slides.length) currentSlide = 0;
        document.getElementById('heroSlides').style.transform = `translateX(-${currentSlide * 100}%)`;
    }

    function showHome() {
        if(document.getElementById('homeContent')) document.getElementById('homeContent').style.display = 'block';
        if(document.getElementById('aboutContent')) document.getElementById('aboutContent').style.display = 'none';
        if(document.getElementById('heroSection')) document.getElementById('heroSection').style.display = 'block';
    }

    function showAbout() {
        if(document.getElementById('homeContent')) document.getElementById('homeContent').style.display = 'none';
        if(document.getElementById('heroSection')) document.getElementById('heroSection').style.display = 'none';
        if(document.getElementById('aboutContent')) document.getElementById('aboutContent').style.display = 'block';
        window.scrollTo(0, 0);
    }

    function switchAnimal(animal) {
        const dogDisplay = document.getElementById('dog-display');
        const catDisplay = document.getElementById('cat-display');
        
        if(animal === 'dog') {
            dogDisplay.className = 'animal-display-fade active-animal w-full';
            catDisplay.className = 'animal-display-fade hidden-animal w-full';
        } else {
            catDisplay.className = 'animal-display-fade active-animal w-full';
            dogDisplay.className = 'animal-display-fade hidden-animal w-full';
        }
    }
</script>
"""
    if '</body>' in new_content:
        new_content = new_content.replace('</body>', script_js + '\n</body>')
    else:
        new_content += script_js
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Done. Created index.html")

if __name__ == '__main__':
    main()
