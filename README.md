Farm To Franchise 

Required dependencies:

To view our website please go to our URL:https://nzproject.herokuapp.com/

Getting the data:
1st issue – there are a number of sites from which to get data
What data points do we want/need?

2nd issue – different sources have different stats
determine how to pull the data
narrow what we pull and not get bogged down
ESPN data doesn’t have the MLB ID’s
MLB data doesn’t have the country of origin
chose scraping which minimized the need to try to merge disparate file formats & ID’s

3rd issue – determining which database worked best for our needs. We needed to have multiple tables and we had a requirement to use Heroku. We therefore decided that using a relational database like postgres would be our best option. Once we had all of the data in tables in Postgress we connected the site through Heroku. 

4th issue – We began laying out the tables we would employ and creating an ERD 

5th issue – To solve the issue of needing a unique ID for our tables we…

6th issue – We connected our JavaScript and pgAdmin to Heroku to upload our data through an API and to create a live site. This required…

7th issue – Site aesthetics- we were able to put background images in both the jumbotron and the main page to enhance the page appeal. Then we made the entire page responsive to make it accessible from all screen types.
