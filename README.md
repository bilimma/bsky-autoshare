# autoshare for bluesky with github actions

Its a simple autoshare script for atproto applications. 

## Installation
### prerequitements

> i prefer to use dotenv with [direnv](https://direnv.net/) for exporting environment variables in .env file. You have to export thoose variables manually before you run main.py in your computer if you don't want to use direnv. exp: `export BSKY_USERNAME=test`


- Fork the repository
- clone
- copy .env.dist as .env file and update variables. FEED_URL must be valid rss feed.
- remove autoshare.db file
- install dependencies with `pip install`
- run `python3 main.py create-db`it will create an empty database
- commit your changes
- push your changes to github

After you complete to install, it will start action and fetch all feed, then will start to share every item in every 6 hours.



[![Autoshare Status](https://github.com/bilimma/bsky-autoshare/actions/workflows/skeet.yml/badge.svg)](https://github.com/bilimma/bsky-autoshare/actions/workflows/skeet.yml)
