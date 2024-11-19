import argparse
import structlog
from endpoint import recursive_crawl
from lib.output import save_to_file, save_to_mongo

def setup_logger():
    """Configure and return a structured logger."""
    structlog.configure(
        processors=[
            structlog.processors.JSONRenderer()
        ]
    )
    return structlog.get_logger()

def main():
    logger = setup_logger()

    # Argument parsing
    parser = argparse.ArgumentParser(description="Recursive Web Crawler with Depth and Page Limits")
    parser.add_argument("--url", required=True, help="URL to crawl")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum recursive depth (default: 3)")
    parser.add_argument("--max-pages", type=int, default=10, help="Maximum number of pages to scrape (default: 10)")
    parser.add_argument("--output-type", choices=["file", "mongo"], required=True, help="Output type: 'file' or 'mongo'")
    parser.add_argument("--output-path", help="File name if saving to file")
    parser.add_argument("--mongo-uri", help="MongoDB URI if saving to MongoDB")
    args = parser.parse_args()

    if args.output_type == "file" and not args.output_path:
        parser.error("--output-path is required for file output")
    if args.output_type == "mongo" and not args.mongo_uri:
        parser.error("--mongo-uri is required for MongoDB output")

    # Start crawling
    logger.info("Starting crawl", url=args.url, max_depth=args.max_depth, max_pages=args.max_pages)
    results, _ = recursive_crawl(args.url, args.max_depth, args.max_pages, logger=logger)

    # Save results
    if args.output_type == "file":
        save_to_file({"home_url": args.url, "crawls": results}, args.output_path)
        logger.info("Results saved to file", path=args.output_path)
    elif args.output_type == "mongo":
        save_to_mongo({"home_url": args.url, "crawls": results}, args.mongo_uri)
        logger.info("Results saved to MongoDB", uri=args.mongo_uri)

if __name__ == "__main__":
    main()
