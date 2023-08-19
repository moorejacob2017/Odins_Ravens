```



                                                 /\
                                                /  \
                                           /\  / /\ \
                                          /  \/ /  \ \
                                         / /\ \/ /\ \ \
                                        / / /\ \/  \ \ \
                                       / / / /\/ /\ \ \ \
                                      / / / / / /\ \ \ \ \
                                     / / / / / /\ \ \ \ \ \
                                    / / / / / /  \ \ \ \ \ \
                                   / / / / / /    \ \ \ \ \ \
                                  / / / / / /      \ \ \ \ \ \
                                 / / / / / / Odin's \ \ \ \ \ \
                                / / / / / /  Ravens  \ \ \ \ \ \
                               / / / /_/_/____________\ \_\_\_\ \
                              / / /____________________\ \_______\
                             / /_____/ /________________\ \ \ \
                            /_______/ /____________________\ \ \
                                   / /________________________\ \
                                  /______________________________\



```

A crawler and parser pair for mapping and targeting web application attack surfaces.

___
#### The Crawler
```
usage: orav-crawler.py [-h] (-w WEBSITE | -f FILE) [-t THREADS] [-o OUTPUT] [-d DELAY]

Crawl a website or multiple websites.

options:
  -h, --help            show this help message and exit
  -w WEBSITE, --website WEBSITE
                        The website URL to crawl.
  -f FILE, --file FILE  A file containing a list of URLs to crawl.
  -t THREADS, --threads THREADS
                        The number of threads to use. Default is 10.
  -o OUTPUT, --output OUTPUT
                        The output file name. Default is "collected_data.json".
  -d DELAY, --delay DELAY
                        The time (in seconds) to wait between each HTTP request. Default is 0.
```
___
#### The Parser
```
usage: orav-parser.py [-h] [--all-urls] [--urls-with-input] [--urls-with-queries] [--all-inputs] [--all-queries] [--all-headers] [--input-values INPUT_VALUES] [--query-values QUERY_VALUES] [--header-values HEADER_VALUES]
                      [--urls-with-specific-input URLS_WITH_SPECIFIC_INPUT] [--urls-with-specific-query URLS_WITH_SPECIFIC_QUERY] [--urls-with-header URLS_WITH_HEADER]
                      file

Parse the serialized data from the website crawler.

positional arguments:
  file                  The JSON file containing the serialized data.

options:
  -h, --help            show this help message and exit
  --all-urls            List all URLs.
  --urls-with-input     List all URLs with input.
  --urls-with-queries   List all URLs with query parameters.
  --all-inputs          List all input names.
  --all-queries         List all query parameter names.
  --all-headers         List all headers.
  --input-values INPUT_VALUES
                        List all values of a specific input.
  --query-values QUERY_VALUES
                        List all values of a specific query parameter.
  --header-values HEADER_VALUES
                        List all values of a specific header.
  --urls-with-specific-input URLS_WITH_SPECIFIC_INPUT
                        List all URLs with a specific input.
  --urls-with-specific-query URLS_WITH_SPECIFIC_QUERY
                        List all URLs with a specific query parameter.
  --urls-with-header URLS_WITH_HEADER
                        List all URLs with a specific header.
```
