from bs4 import BeautifulSoup as bs

def clean_content(content):
    soup = bs(content, "lxml")
    return soup.get_text(separator=' ', strip=True)

def get_first_image(content):
    soup = bs(content, "lxml")
    all_images = soup.find("img")
    if all_images:
        return all_images.get("src")
    return "/media/blog.jpg"
