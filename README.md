# web-crawler

The code should return the most common words used and the number of times they are used. The following should be configurable:
1. The number of words to return is set on WORDS_RETURN (default: 10)
2. Words to exclude from the search. It can be string or list. Example: ["excellent", "linux"] or "excellent, linux"


## Quick Start

1. Install 

   ```bash
   pip install -r requirements.txt
   ```

2. Start program:
   Update url and exception as well as the WORDS_RETURN

   ```bash
   python run.py
   python run.py https://en.wikipedia.org/wiki/Microsoft#History ['in', 'on']
   ```
3. Run Tests
   Run test example with all test cases

   ```bash
   python -m unittest tests
   ```
## Example:

Page to crawl
https://en.wikipedia.org/wiki/Microsoft
Only words from the section “history” should be accounted for.
Example of the expected result
```bash
python run.py https://en.wikipedia.org/wiki/Microsoft#History ['in','on']

--------------------------------
| # of            | occurrences |
| the             |        979 |
| microsoft       |        608 |
| of              |        371 |
| to              |        357 |
| and             |        317 |
| retrieved       |        271 |
| from            |        265 |
| a               |        258 |
| archived        |        211 |
| original        |        205 |
--------------------------------

```
	

