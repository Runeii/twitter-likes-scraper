# Twitter likes scraper
Scrapes a user's likes and saves a local copy, with images.

Based on Scweet: https://github.com/Altimis/Scweet

## Repo

- src – src used to compile dist. Is a modified (hack job) version of Scweet.
- scweet – a simple to work with prepackaged executable. 99% of the time, this is all you need


## Using

1. It's recommended to create a new Twitter user as there is a rare edge possibility you're seen as a bot and the account banned. V unlikely if you're just scraping your own likes, but probably not worth the risk.


2. From this folder, in your terminal, run:

USER_USERNAME=[newly created user username] USER_EMAIL=[newly created user email] USER_PASSWORD=[newly created user password] ./scweet --from_account=[the account you want to scrape username] --since [how far back to scrape eg: 2012-11-01]

**Do not interact with the Chrome browser while it is running!**
It is helpful to see the output for debugging but, if you can't help yourself, set the `--headless` command below to True to hide the window.


3. You can technically pass any arguments supported by Scweet, thought many are useless when scraping likes. These are some that may be useful, however:

```
  -h, --help            show help message with all commands
  --until UNTIL         End date for search query. example : %Y-%m-%d.
  --since SINCE
                        Start date for search query. example : %Y-%m-%d.
  --headless HEADLESS   Whether runs in headless mode or not (ie: when headless is False, you can see the Chrome window in the background). True or False
  --limit LIMIT         Limit tweets to be scraped.
  --resume RESUME       Resume the last scraping. specify the csv file path.
```

4. The process can take quite a while, especially if you have been very online for a long time