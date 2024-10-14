import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import time

while True:
    #url example "https://example.com"
    url = input("Enter URL to analyze: ")
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Invalid URL. Please enter a valid URL starting with http:// or https://")
        continue

    # Make request to URL and create BeautifulSoup object
    start_time = time.time()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    loading_time = time.time() - start_time

    # Count number of internal and external links
    internal_links = []
    external_links = []
    other_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None and (href.startswith('/') or href.startswith(url) or href.startswith('#')):
            internal_links.append(href)
        elif str(href).startswith('http') or str(href).startswith('www'):
            external_links.append(href)
        else:
            other_links.append(href)
    print("Number of internal links: ", len(internal_links))
    print("Number of external links: ", len(external_links))
    print("Number of other links: ", len(other_links))

    # Count number of small words in body
    body_text = soup.find('body').get_text()
    small_words_max_limit = 5
    small_words = re.findall(r'\b\w{1,' + str(small_words_max_limit) + r'}\b', body_text)
    print(f"Number of words in body with length less than {small_words_max_limit} letters: ", len(small_words))

    # Count number of big words in body
    big_words_min_limit = 5
    big_words = re.findall(r'\b\w{' + str(big_words_min_limit) + r',}\b', body_text)
    print(f"Number of words in body with length over {big_words_min_limit} letters: ", len(big_words))

    # Count number of words per sentence in body
    sentences = re.findall(r'([A-Z][^\.!?]*[\.!?])', body_text)
    word_count_per_sentence = [len(sentence.split()) for sentence in sentences]

    if len(word_count_per_sentence) > 0:
        # with 2 decimal places
        print("Number of words per sentence in body: ", "{:.2f}".format(sum(word_count_per_sentence)/len(word_count_per_sentence)))
    else:
        print("Number of words per sentence in body: 0")

    # Count number of images in body and check if they have alt description
    image_count = 0
    image_alt_count = 0
    for img in soup.find_all('img'):
        image_count += 1
        if img.has_attr('alt') and img['alt']:
            image_alt_count += 1
    print("Number of images in body: ", image_count)
    print("Number of images with alt description in body: ", image_alt_count)

    #Check if title exists
    title = soup.find('title')
    if title:
        print("Title: OK")
    else:
        print("Title: Not found")

    # Check if meta description exists
    meta_description = soup.find('meta', attrs={'name': 'description'})
    if meta_description:
        print("Meta Description: OK")
    else:
        print("Meta Description: Not found")

    # Count number of meta elements in the HTML document
    meta_count = len(soup.find_all('meta'))
    print("Number of meta elements: ", meta_count)

    # Count number of DOM elements in the HTML document
    dom_count = len(soup.find_all())
    print("Number of DOM elements: ", dom_count)

    # Print loading time
    print("Loading Time: {:.2f} seconds".format(loading_time))

    # Find words with highest frequency in body
    comon_words_limit = 5
    big_word_counts = Counter(big_words)
    most_common_big_words = big_word_counts.most_common(comon_words_limit)
    print(f"Most common words in body with length over {big_words_min_limit} letters: ", ", ".join([f"{word} ({count})" for word, count in most_common_big_words]))

    smalL_word_counts = Counter(small_words)
    most_common_small_words = smalL_word_counts.most_common(comon_words_limit)
    print(f"Most common words in body with length less than {small_words_max_limit} letters: ", ", ".join([f"{word} ({count})" for word, count in most_common_small_words]))

    # Ask user if they want to run the script again
    run_again = input("Do you want to analyze another URL? (yes/no): ")
    if run_again.lower() != 'yes':
        break