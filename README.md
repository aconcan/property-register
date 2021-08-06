# property-register
Pulls data from Ireland's [property register](https://www.propertypriceregister.ie/website/npsra/pprweb.nsf/PPR?OpenForm) to track sales of residential dwellings in specified areas. Parses response with BeautifulSoup, then compares this with the database for new sales since the program was last run. 
Any updates then sent via text using the Twilio API.

<img width="747" alt="Screen Shot 2021-08-06 at 2 12 52 PM" src="https://user-images.githubusercontent.com/55048231/128515535-be2dcbbe-96d6-4bd9-828d-535e0205300e.png">

