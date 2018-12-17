# Import Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests

# Initialize browser
def init_browser():
    # Replace the path with your actual path to the chromedriver
    
    execu_path = {'executable_path': '/Users/Byron/Desktop/Trilogy/chromedriver_win32'}
    return Browser('chrome', headless=True, **execu_path)

# Create Mission to Mars global dictionary that can be imported into MongoDB
mars_info = {}

# NASA Mars News
def scrape_mars_news():
    try:
        # Initialize browser
        browser = init_browser()
        
        # Visit NASA news url using splinter
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        
        # Store HTML
        html = browser.html
        
        # Use Beautiful Soup to parse HTML
        soup = bs(html, 'html.parser')
        
        # Retrieve the latest element containing news title and news paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_par = soup.find('div', class_='article_teaser_body').text
        
        # Dictionary entry from Mars News
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_par
        
        return mars_info
    finally:
        browser.quit()
        
# Featured image
def scrape_mars_img():
    try:
        # Initialize browser
        browser = init_browser()
        
        # Visit Mars Space Images using splinter
        img_url_feat = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_feat)
        
        # Store HTML
        html_img = browser.html
        
        # Use Beautiful Soup to parse HTML
        soup = bs(html_img, 'html.parser')
        
        # Retrieve backgroud image url
        feat_img_url = soup.find('article')['style'].\
                        replace('background-image: url(','').relpace(');', '')[1:-1]
        
        # Website url
        main_url = 'https://www.jpl.nasa.gov'
        
        # Combine website url with scrapped route
        feat_img_url = main_url + feat_img_url
        
        # Display full link to featured image
        feat_img_url
        
        # Dictionary entry for featured image
        mars_info['featured_image_url'] = feat_img_url
        
        return mars_info
    finally:
        browser.quit()
        
# Mars Weather
def scrape_mars_weather():
    try:
        # Initalize browser
        browser = inti_browser()
        
        # Visit Mars Weather Twitter using splinter
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)
        
        # Store HTML
        html_weather = browser.html
        
        # Using Beautiful Soup parse HTML
        soup = bs(html_weather, 'html.parser')
        
        # Find all elements contailing tweets
        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')
        
        # Retrieve all elements containing news title in the specified range
        # Look for entries that display weather related words to exclude unrelated tweets
        for tweet in latest_tweets:
            weather_tweet = tweet.find('p').text
            if 'Sol' and 'pressure' in weather_tweet:
                print(weather_tweet)
                break
            else:
                pass
            
        # Dictionary entry from Weather Tweet
        mars_info['weather_tweet'] = weather_tweet
        
        return mars_info
    finally:
        browser.quit()
        
# Mars Facts
def scrape_mars_facts():
    # Initialize browser
    browser = init_browser()
    
    # Visit Mars Facts url
    facts_url = 'https://space-facts.com/mars/'
    
    # Use Pandas to parse the url
    mars_facts = pd.read_html(facts_url)
    
    # Find the mars facts DataFrame in the list of DataFrames and assign it to 'mars_df'
    mars_df = mars_facts[0]
    
    # Assign columns: Description, Value
    mars_df.columns = ['Description', 'Value']
    
    # Set the index to the 'Description' column without row indexing
    mars.set_index('Description', inplace=True)
    
    # Save HTML code
    data = mars_df.to_html()
    
    # Dictionary entry from Mars Facts
    mars_info['mars_facts'] = data
    
    return mars_info

# Mars Hemispheres
def scrape_mars_hemispheres():
    try:
        # Initialize browser
        browser = init_browser()
        
        # Visit hemisphers website using splinter
        hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemis_url)
        
        # Store HTML
        html_hemis = browser.html
        
        # Using Beautiful Soup parse HTML
        soup = bs(html_hemis, 'html.parser')
        
        # Retieve all items containing mars hemisphere info
        items = soup.find_all('div', class_='item')
        
        # Create empty list for hemisphere URLs
        hemi_info = []
        
        # Store the main URL
        hemis_main_url = 'https://astrogeology.usgs.gov'
        
        # Loop through the items previously stored
        for i in items:
            # Store title
            title = i.find('h3').text
            
            # Store link to full image site then visit it
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            brower.visit(hemis_main_url + partial_img_url)
            
            # Store HTML of individual hemisphere info site
            partial_img_html = browser.html
            
            # Using Beautiful Soup parse HTML
            soup = bs(partial_img_html, 'html.parser')
            
            # Retrieve full image source
            img_url = hemis_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append the retrieved info into list of dictionaries
            hiu.append({"title": title, "img_url": img_url})
        
        # Dictionary entry for Hemisphere Info
        mars_info['hiu'] = hiu
        
        return mars_info
    finally:
        browser.quit()
        