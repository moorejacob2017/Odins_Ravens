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
usage: orav-parser.py [-h] [-a] [-ai] [-aq] [-ah] [-ui] [-uq] [-vi INPUT_VALUE] [-vq QUERY_VALUE] [-vh HEADER_VALUE] [-uvi INPUT_VALUE] [-uvq QUERY_VALUE] [-uvh HEADER_VALUE] file

Parse the serialized data from the website crawler.

positional arguments:
  file                  The JSON file containing the serialized data.

options:
  -h, --help            show this help message and exit
  -a, --all-urls        List all URLs.
  -ai, --all-inputs     List all input names.
  -aq, --all-queries    List all query parameter names.
  -ah, --all-headers    List all headers.
  -ui, --urls-with-input
                        List all URLs with input.
  -uq, --urls-with-queries
                        List all URLs with query parameters.
  -vi INPUT_VALUE, --input-values INPUT_VALUE
                        List all values of a specific input.
  -vq QUERY_VALUE, --query-values QUERY_VALUE
                        List all values of a specific query parameter.
  -vh HEADER_VALUE, --header-values HEADER_VALUE
                        List all values of a specific header.
  -uvi INPUT_VALUE, --urls-with-specific-input INPUT_VALUE
                        List all URLs with a specific input.
  -uvq QUERY_VALUE, --urls-with-specific-query QUERY_VALUE
                        List all URLs with a specific query parameter.
  -uvh HEADER_VALUE, --urls-with-header HEADER_VALUE
                        List all URLs with a specific header.
```
