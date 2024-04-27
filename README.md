# web-crawler

The code should return the most common words used and the number of times they are used. The following should be configurable:
1. The number of words to return is set on WORDS_RETURN (default: 10)
2. Words to exclude from the search. It can be string or list. Example: ["excellent", "linux"] or "excellent, linux"


## Quick Start

1. Install 

   ```bash
   pip install 
   ```

2. Start program:
   Update url and exception as well as the WORDS_RETURN

   ```bash
   python run.py 
   ```
3. Run Tests
   Run test example with all test cases

   ```bash
   python run.py 
   ```
## Example:

Page to crawl
https://en.wikipedia.org/wiki/Microsoft
Only words from the section “history” should be accounted for.
Example of the expected result
	# of occurrences
The	205
Microsoft	113
in	110
of	88
and	88
a	81
to	79
on	59
Windows	55
for	50

