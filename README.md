# ppr

Check out the site at **https://amith12355.pythonanywhere.com/pprsite/**

This is a simple website to browser the Irish Property Price Register which is a record of all residential property sales (https://www.propertypriceregister.ie/)

File location: 'https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-ALL.zip/$FILE/PPR-ALL.zip'

There are two main parts of this project:

1) ppr_csv_to_db.py : This downlaods the PPR-ALL.zip file, converts to a pandas dataframe and then satnitizes and restructures it to create ppr/ppr.db
2) A django project that expose the data via a web app using Django ORM and Materialize UI framework.

Listings can be fitlered by Address, County, Min and Max Prices, Date of Sale
