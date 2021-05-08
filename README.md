![Skull Icon](https://cdn3.iconfinder.com/data/icons/universal-signs-symbols/128/pirate-sword-skull2-512.png)

                                                                                Version: Release v4.0

## Github project URL
https://github.com/brandongallagher1999/CrypTorrents---FastAPI/

## Hosted Website URL
http://cryptorrents.herokuapp.com/
- **The website could currently be down to my Heroku Free-Tier running out of dyno hours. If this is the case, please run it using docker-compose.**
- *Accessing website may be slow initially due to the Docker Container spinning up.*


## Contributors
1. **Brandon Gallagher**
  - Roles: Back-end / Front-End / Database
  - Email: brandonegallagher@gmail.com
  - [Github Profile](https://github.com/brandongallagher1999)

## Description
- Front-End is built in React
- Back-End is built in FastAPI
- Uses ThePirateBay REST API to fetch torrent information based on a query, parses it, and displays the top 3 results
sorted by Seeders, and displays them beside a relevant picture from the DuckDuckGo API.

## React
- https://reactjs.org/

## Fast API
- https://fastapi.tiangolo.com/features/


# How to run
## Docker
1. Download Docker for Desktop (https://www.docker.com/products/docker-desktop)

## Container
1. Go into root folder and run
```
docker-compose build
docker-compose up
```
  
## Opening Web App
1. Go into any browser, preferably Google Chrome
2. In the URL bar, type "localhost:3000"


# Upcoming Changes
- Login page completed, working on having a profile page load stored user's content.
