## Introduction

The News Indexer is a web application designed to index news articles searched by users across multiple languages, including English, Spanish, Portuguese, German, Dutch, Russian, and others. Comprising two layers, the application features a frontend built with Next.js and React.js, enabling Progressive Web App (PWA) functionality for installation. It communicates with a backend web API developed in Python.

## Functionality Overview

The News Indexer provides the following functionality:

1. **Home Page Loading**: Upon loading the home page, default news articles are displayed. The frontend sends a request to the server, which responds with a list of news articles.

2. **Language Settings**: Users can change the language settings via the settings menu. Upon selecting a language, the user receives news articles relevant to the chosen language.

3. **Search Feature**: Users can perform searches, triggering a request to the server. The server scrapes news sites based on the provided keywords and sends the search results to the frontend.

4. **News Analysis**: When a news article is clicked, the frontend sends a request to the server to analyze it. The server retrieves the raw HTML of the article and applies Natural Language Processing (NLP) algorithms to understand its content. The analyzed news content is then sent to the frontend to render the interface.

## Project Structure

The News Indexer project is structured into two layers:

### Frontend Layer

- **Description**: The frontend layer, built with Next.js and React.js, provides the user interface for interacting with the application. It features PWA functionality, allowing users to install the application on their devices for offline access.
- **Source Code**: [Frontend Source Code](https://github.com/RodrigoGaluppo/MyNews-FrontEnd/)

### Backend Layer

- **Description**: The backend layer consists of a web API developed in Python. It utilizes Selenium for web scraping news sites to fetch news articles based on user queries. Additionally, it incorporates NLP algorithms to analyze the content of selected news articles.
- **Source Code**: [Backend API Source Code](https://github.com/RodrigoGaluppo/MyNews-Python)

## Conclusion

The News Indexer combines the power of frontend technologies like Next.js and React.js with backend capabilities in Python to deliver a versatile news indexing platform. By leveraging web scraping and NLP algorithms, the application provides users with access to news articles in multiple languages, enhancing their browsing experience.


