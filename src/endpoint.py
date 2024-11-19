from lib.extract import fetch_page_content

def recursive_crawl(url, max_recursive_calls, max_pages, visited=None, page_count=0, depth=0, logger=None):
    """
    Recursively crawl a webpage to extract text and follow links.
    """
    if visited is None:
        visited = set()
    if depth >= max_recursive_calls or url in visited or page_count >= max_pages:
        return [], page_count

    visited.add(url)
    page_count += 1
    logger.info("Crawling", url=url, depth=depth, page_count=page_count)

    page_text, links = fetch_page_content(url)
    if not page_text:
        logger.warning("Failed to fetch content", url=url)
        return [], page_count

    page_data = {
        "url": url,
        "text": page_text,
        "recursive_crawls": []
    }

    for link in links:
        if page_count < max_pages:  # Check before starting new recursion
            crawled_data, page_count = recursive_crawl(
                link, max_recursive_calls, max_pages, visited, page_count, depth + 1, logger
            )
            page_data["recursive_crawls"].extend(crawled_data)

    return [page_data], page_count
