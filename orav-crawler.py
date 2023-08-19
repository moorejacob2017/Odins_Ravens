import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
from queue import Queue
import threading
import argparse
import json
import time


def get_links_and_data(url, base_url, delay):
    time.sleep(delay)  # Add the delay before sending the request
    links = []
    data = {
        'has_user_input': False,
        'input_values': {},
        'http_headers': {},
        'query_parameters': {}
    }
    try:
        response = requests.get(url)
        headers = response.headers
        data['http_headers'] = {k: v for k, v in headers.items()}

        soup = BeautifulSoup(response.text, 'html.parser')

        # Check for forms and input values
        for form in soup.find_all('form'):
            data['has_user_input'] = True
            for input_tag in form.find_all('input', {'name': True}):
                name = input_tag['name']
                value = input_tag.get('value', '')
                if name not in data['input_values']:
                    data['input_values'][name] = []
                data['input_values'][name].append(value)

        # Parse and collect query parameters
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        for k, v in query_params.items():
            data['query_parameters'][k] = v

        # Collect links
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            full_url = urljoin(base_url, link)
            if base_url in full_url and full_url not in visited:
                links.append(full_url)
                visited.add(full_url)  # Add URL to the visited set right away

    except Exception as e:
        print(f"An error occurred: {e}")

    return links, data



def worker():
    while True:
        url = q.get()
        if url is None:
            break
        print(f"Processing {url}")
        links, data = get_links_and_data(url, base_url, delay)
        collected_data[url] = data
        for link in links:
            q.put(link)
        q.task_done()


def main():
    parser = argparse.ArgumentParser(description='Crawl a website or multiple websites.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-w', '--website', type=str, help='The website URL to crawl.')
    group.add_argument('-f', '--file', type=str, help='A file containing a list of URLs to crawl.')
    parser.add_argument('-t', '--threads', type=int, default=10, help='The number of threads to use. Default is 10.')
    parser.add_argument('-o', '--output', type=str, default='collected_data.json', help='The output file name. Default is "collected_data.json".')
    parser.add_argument('-d', '--delay', type=float, default=0.0, help='The time (in seconds) to wait between each HTTP request. Default is 0.')
    args = parser.parse_args()

    global base_url, q, visited, collected_data, delay
    base_url = args.website if args.website else None
    delay = args.delay  # Set the global delay variable
    urls_to_crawl = [base_url] if base_url else []
    if args.file:
        with open(args.file, 'r') as file:
            urls_to_crawl = [line.strip() for line in file.readlines()]

    q = Queue()
    visited = set()
    collected_data = {}

    num_threads = args.threads
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for url in urls_to_crawl:
        visited.add(url)  # Add URL to the visited set right away
        q.put(url)
    q.join()

    for i in range(num_threads):
        q.put(None)
    for t in threads:
        t.join()

    # Pretty print collected data
    print(json.dumps(collected_data, indent=4))

    # Serialize data to a file with the specified name
    with open(args.output, 'w') as file:
        json.dump(collected_data, file, indent=4)


if __name__ == '__main__':
    main()