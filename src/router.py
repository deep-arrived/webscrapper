from endpoint import crawl_website


def handle_request(input_url, max_pages, max_recursive_calls, output):
    result = crawl_website(input_url, max_pages, max_recursive_calls)
    
    if output == 'file':
        with open('output.json', 'w') as f:
            import json
            json.dump(result, f, indent=4)
        print("Output written to output.json")
    elif output == 'mongo':
        # MongoDB logic goes here
        print("Output stored in MongoDB")