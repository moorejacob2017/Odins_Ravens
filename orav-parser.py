import argparse
import json


def load_data(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def all_urls(data):
    return list(data.keys())


def all_urls_with_input(data):
    return [url for url, info in data.items() if info['has_user_input']]


def all_urls_with_queries(data):
    return [url for url, info in data.items() if info['query_parameters']]


def all_inputs(data):
    inputs = set()
    for info in data.values():
        inputs.update(info['input_values'].keys())
    return list(inputs)


def all_queries(data):
    parameters = set()
    for info in data.values():
        parameters.update(info['query_parameters'].keys())
    return list(parameters)


def all_values_of_specific_input(data, input_name):
    values = set()
    for info in data.values():
        values.update(info['input_values'].get(input_name, []))
    return list(values)


def all_values_of_specific_query_parameter(data, parameter_name):
    values = set()
    for info in data.values():
        values.update(info['query_parameters'].get(parameter_name, []))
    return list(values)


def all_urls_with_specific_input(data, input_name):
    return [url for url, info in data.items() if input_name in info['input_values']]


def all_urls_with_specific_query(data, parameter_name):
    return [url for url, info in data.items() if parameter_name in info['query_parameters']]


def all_headers(data):
    headers = set()
    for info in data.values():
        headers.update(info['http_headers'].keys())
    return list(headers)


def all_values_of_specific_header(data, header_name):
    values = set()
    for info in data.values():
        values.add(info['http_headers'].get(header_name, ''))
    return list(values)


def all_urls_with_specific_header(data, header_name):
    return [url for url, info in data.items() if header_name in info['http_headers']]


def main():
    parser = argparse.ArgumentParser(description='Parse the serialized data from the website crawler.')
    parser.add_argument('file', type=str, help='The JSON file containing the serialized data.')
    parser.add_argument('-a', '--all-urls', action='store_true', help='List all URLs.')

    parser.add_argument('-ai', '--all-inputs', action='store_true', help='List all input names.')
    parser.add_argument('-aq', '--all-queries', action='store_true', help='List all query parameter names.')
    parser.add_argument('-ah', '--all-headers', action='store_true', help='List all headers.')

    parser.add_argument('-ui', '--urls-with-input', action='store_true', help='List all URLs with input.')
    parser.add_argument('-uq', '--urls-with-queries', action='store_true', help='List all URLs with query parameters.')

    parser.add_argument('-vi', '--input-values', metavar='INPUT_VALUE', type=str, help='List all values of a specific input.')
    parser.add_argument('-vq', '--query-values', metavar='QUERY_VALUE', type=str, help='List all values of a specific query parameter.')
    parser.add_argument('-vh', '--header-values', metavar='HEADER_VALUE', type=str, help='List all values of a specific header.')

    parser.add_argument('-uvi', '--urls-with-specific-input', metavar='INPUT_VALUE', type=str, help='List all URLs with a specific input.')
    parser.add_argument('-uvq', '--urls-with-specific-query', metavar='QUERY_VALUE', type=str, help='List all URLs with a specific query parameter.')
    parser.add_argument('-uvh', '--urls-with-header', metavar='HEADER_VALUE', type=str, help='List all URLs with a specific header.')

    args = parser.parse_args()

    data = load_data(args.file)

    if args.all_urls:
        print(all_urls(data))
    if args.urls_with_input:
        print(all_urls_with_input(data))
    if args.urls_with_queries:
        print(all_urls_with_queries(data))
    if args.all_inputs:
        print(all_inputs(data))
    if args.all_queries:
        print(all_queries(data))
    if args.input_values:
        print(all_values_of_specific_input(data, args.input_values))
    if args.query_values:
        print(all_values_of_specific_query_parameter(data, args.query_values))
    if args.urls_with_input:
        print(all_urls_with_specific_input(data, args.urls_with_input))
    if args.urls_with_query_parameter:
        print(all_urls_with_specific_query(data, args.urls_with_query_parameter))
    if args.all_headers:
        print(all_headers(data))
    if args.header_values:
        print(all_values_of_specific_header(data, args.header_values))
    if args.urls_with_header:
        print(all_urls_with_specific_header(data, args.urls_with_header))


if __name__ == '__main__':
    main()
