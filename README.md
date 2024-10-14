# Web Page Analysis Tool

This Python script allows you to analyze the content and structure of any web page by entering its URL. It provides insights such as the number of internal/external links, word count, meta tags, and more.

## Features

- **URL Validation**: Ensures the provided URL starts with `http://` or `https://`.
- **Internal/External Links**: Counts the number of internal, external, and other links.
- **Word Analysis**: Counts words in the body that are longer than four letters and calculates the average number of words per sentence.
- **Image Analysis**: Counts images on the page and checks how many have `alt` descriptions.
- **Meta Tags**: Checks if the page has a title, meta description, and counts all meta elements.
- **DOM Elements**: Counts the total number of HTML DOM elements on the page.
- **Loading Time**: Displays how long it took to load the page.
- **Frequent Words**: Finds the top five most common words in the body of the page (with a length greater than four letters).

## Requirements

- Python 3.x
- requests
- beautifulsoup4

To install the required packages, run the following command:

```bash
pip install requests beautifulsoup4
```

## Usage

1. **Clone the repository or the script file:**

```bash
git clone https://github.com/TsikaAndreas/web-page-analyzer.git
```

2. **Run the script and provide the URL of the web page you want to analyze:**

```bash
python web_analysis_tool.py
```

3. **Enter the URL when prompted. The URL must start with `http://` or `https://`.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more information.
