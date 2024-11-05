# ppr

Check out the site at **https://amith12355.pythonanywhere.com/pprsite/**

This is a simple website to browser the Irish Property Price Register which is a record of all residential property sales (https://www.propertypriceregister.ie/)
Its provided as a CSV file making it difficult to access and navigate
File location: 'https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-ALL.zip/$FILE/PPR-ALL.zip'

There are two main parts of this project:

1) ppr_csv_to_db.py : This downlaods the PPR-ALL.zip file, converts to a pandas dataframe and then satnitizes and restructures it to create ppr/ppr.db
2) A django project that expose the data via a web app using Django ORM and Materialize UI framework.

Listings can be fitlered by Address, County, Min and Max Prices, Date of Sale

Features to add:
Sort via column
Allow updating the DB directly from web page instead of a pull request for each DB update
Add a google maps like using the post code (maybe use an embedded map api/library?)
A page for useful statistics like:
  - Average price by area in a given year
  - Price increases of the same property over the years
  - Areas with most sales
  - Number of sales by of each month, quarter, year
