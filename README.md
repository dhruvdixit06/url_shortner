# URL Shortener
This is a web app developed using Flask framwork.

## A. What will our Web app do (Objectives)? 
As the name suggests, it shortens URLs. Users can also save URLS by coming to the web app. 

## B. Why do we need URL Shortener? 
Sometimes we need to share or send links and this can be tiresome and annoying to copy and paste long URLs. That is where URL shorteners come in. Not only it helps in shortening the URL but it also allows the user to copy the shortened URL with a click of a button. 

## C. The project consists of following parts: 
1. Frontend (done with HTML, CSS, JavaScript and Bootstrap) 
2. Backend - Flask (Python) Backend - Database ORM (SQLAlchemy) 
3. Backend - Database (SQLite)

## D. Front-End Information: 
-> The front-end consists of 2 web pages: 
Home Page - A page will be shown where the user can enter the URL he/she wants to shorten. After the ‘shorten’ button is clicked, the shortened URL is displayed in the text-field which the user can copy using the copy button.<br />
History Page - Containing all the Original URLs along with the Shortened URLs. 

## E. Project Workflow 
Users can enter the URL they want to shorten. After entering a URL, click on the ‘Shorten’ URL button to display the shortened URL in the following text-field which can be copied by clicking on the copy button. After the ‘Shorten’ button is clicked, the URL that is entered is saved in our database with the shortened URL. It is saved in the database so that the user can look into the previous URLs he/she entered in our web-app with their shortened URL. The app also verifies that whether the URL entered by the user is correct or not.
