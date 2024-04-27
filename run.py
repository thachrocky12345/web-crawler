import sys
from web_crawler import stream_crawl_most_common_words
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Microsoft#History"
    sys_para = sys.argv
    exclude = None
    # Try to get input url else default is Microsoft wiki
    if len(sys_para) > 1 and "http" in sys_para[1]:
        url = sys_para[1]

    # Try to get exclude list example ['on', 'in'] or "on, in"
    if len(sys_para) > 2:
        exclude = sys_para[2]
        if "[" in exclude and "]" in exclude:
            try:
                exclude = eval(exclude)
            except Exception as error:
                exclude = str(exclude)

    most_common_words = stream_crawl_most_common_words(url, num_words=10, exclude=exclude)
    print(f"URL: {url}, exclude list: {exclude}")
    print("-" * 32)
    print("| {:15} | {:>10} |".format("# of", "occurrences"))

    # Print data rows
    for word, count in most_common_words:
        print("| {:15} | {:>10} |".format(word, count))
    print("-" * 32)