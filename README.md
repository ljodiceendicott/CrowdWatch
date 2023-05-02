# PeopleWatch

## Abstract

Not knowing how busy a location will be, is something that can have a large effect on your experience while being at that place. With CrowdWatch, it will eliminate this issue by giving customers the ability to view how many people are at the location without having to go there and see it for yourself. This is done by having the people at the location updating the values which are then updated on a website that customers are then able to go on and see. The website also contains historical information that will allow customers to learn when the location has its peak times and schedule accordingly. It also has use on the business side. They can use the information to improve their staffing by moving staffing to cover the times that are considered their peak times. By doing this they are able to improve their service. Along with the website, there is also a hardware element that is found at the main entry points of these places. This hardware component will also be used to populate a spreadsheet that allow the businesses to view their data and construct the analytics that are needed for them.

## This Project fulfills my Senior thesis for Endicott College.

it encorporates:

- Arduino
- Python
- HTML/CSS & Javascript
- Spreadsheet Files

To Run this project (Website) use the command:
Command has to be ran from _Senior Thesis\Website\PeopleWatchSite_

_node index.js_

Before running the project for non-testing usage you will have to run the python command:
_python getStarted.py_
This command will be used to create the data storage for the project. this includes: - MongoDB Database file -- log of the actions from the website - Spreadsheet file -- (for business usage for analytics) - description.json -- used in the creation of the layout includes the constants for each location

These are the main directories of the project

- Arduino
  Holds the Arduino file for the device
- Python
  Holds the code that is used but also the code that was used for research and development which is found in the _Development and testing_ directory
- Website
  Holds web code including HTML/CSS/Javascript as well as information for firebase
- User Files
  Files found in this directory, are the ones that pertain to a singular business which is then used throughout the project

## Introduction

CrowdWatch is software that allows for customers to be informed about the amount of customers that attend a business. This allows the customers to be able to make an informed decision on if they would be willing to go to a location based on the amount of people that are currently there. This software would also allow the business’ themselves to view analytics about themselves. With these analytics, they are able to adjust staffing to help improve their ability to serve their customers. It will include a two part system. The first part will be a hardware component that is used to adjust the number of people as they enter or leave the area in use. The second part would be the software component which allows the public to view the information about the businesses and their locations’ count of people.
Looking at the hardware component, it could be found in settings that are found indoors or have a person present in the main entrance would be able to use a counting device, that would contain buttons to allow for increasing and decreasing the number of people as well as the ability to cycle through the areas that people are entering or leaving. This would be a stationary device found at a location like a front desk or the front of a bus or train where a driver is situated. This is because in order for a person to enter or leave they would have to pass through these points.
With the software side, there is going to be a website that is open to the public. This will display the number of people that are found in these locations. Along with the number, there will also be a color coordinated to the number of people based on the maximum number of people found. This is something that will be made to be updated real time. There is also a portion of the software that will send information to a spreadsheet for the business’ use. The spreadsheet will be used by the businesses to help improve its own infrastructure and overall customer service.

## Related Works

As this is a problem that can be found in most public businesses, it is very surprising that most industries do not all have a solution implemented to help inform their customers of how many people are in their business. In doing research for this project, there have been comparable implementations were found at Endicott, used in businesses, as well as companies that have been created to solve this problem. With these implementations, there are things that worked well and there are things that need to be improved. The things that need to be improved are the things that were addressed in the creation of CrowdWatch.
At Endicott, there have been a few things that I have used for inspiration. One of the more recent things that I found was at Callahan Dining Hall during the period when there was weekly testing for the Covid-19 on the Endicott College Campus. In order to help reduce the spread of the virus, there was a limit for the amount of people allowed in the hall at one point in time. There was a television screen outside of the hall that would update the count as people would enter and exit. This was able to inform the people outside of the dining hall of the current number. Unfortunately the only place this information was able to be seen was outside of the dining hall, which made it not very useful unless you were right outside. This was a factor that was considered when constructing CrowdWatch. This factor for CrowdWatch was to have the ability to access from anywhere.
Another thing from Endicott that I found that as related works is the Thesis projects of Chantel Barret, called IWorkout, and Kristian Catalan, called Campus Crowd. Both of these projects had elements that were interesting components that related to CrowdWatch. With Chantel’s, the analytics and execution would be similar to CrowdWatch. IWorkout was designed to be used in a gym setting and was an IOS application. The use of Arduino components and a Raspberry PI are elements that I feel inspired parts of the implementation of the hardware used in CrowdWatch. With IWorkout’s implementation is limiting to only use with IOS products which does not allow for the information to be accessed from the browser or any other non-IOS devices. There are similar critiques with Kristians implementation of Campus Crowd. It was constructed with android studios, limiting the use of the service to android devices. With CrowdWatch, it should be able to be visited on any device. One thing that worked really well was the analytics that were found in the application. With Campus Crowd, there were different levels of information that the user would be able to view. The main portion that inspired parts of CrowdWatch was the statistics page and the building view. These both inform the user about the current count of people as well as historical analysis. These are two of the main features found in Crowd Watch. Also with campus crowd, the way that the count was being generated was based off of wifi signals and by tracking the user. With CrowdWatch there will not be any tracking of users, making it less intrusive while still keeping a proper count (Barret and Endicott College 2017, Catalan and Endicott College 2017).
Within some companies, they contain their own implementation of keeping track of the count of people in locations. One of these companies is GymIt. GymIt is a gym found in the boston area. They have an app that assists its members in tracking their fitness goals as well as planning out different activities that, as a member, you can use along with the other things that you would want to keep track of for the improvement of health. Along with this, they give the ability for the customers to see the amount of people that are found at the gym. This count of people is adjusted by having people scan their membership card to get in. By doing so, the count on the application and website are adjusted. It is the same for when people leave. The issue is that this number is not always accurate. This is due to the people at the front desk not having the people scan out from the gym. With their implementation of this, there is also no analytics for the different sections found in the gym or any historical analysis for when the best times are to go to the gym (“GymIt Brookline”, n.d.).  
A company that has been able to implement an expected busy feature that will be similar to the historical analysis page is Google Maps. Within Google Maps, there is a feature when looking at a business that it shows the expected times that it would be busy for the particular day. This is a feature that would be beneficial to have in the historical analysis for CrowdWatch. The way that the information for when the locations are busy found on Google Maps is for the business as a whole. For CrowdWatch, This would make more sense to have it by sub-locations. This is because there will be several different locations found at one main location being the business (“Popular times, wait times, and visit duration - Google Business Profile Help”, n.d.).
Unlike Google Maps or Gymit, there are companies that their business is making these counting devices and accompanying software. A service that includes both the software and the hardware is a company called Axper. Their products are used in retail environments and public spaces. There is analytics but they are available for internal use only. They also do not show any tools to help make this information available for the public, which is one of the main functions of CrowdWatch. Giving the public the ability to view this analytical information (“Retail”, n.d.).
Another product that is similar to CrowdWatch is the Pearl Smart People Counter. This is a device that can be found on amazon for five hundred dollars. This device works similarly to the devices found from the company Axper. The difference is that with the Pearl Smart Device, you are the one that is doing it all on your own. In order to have these devices work, you have to manually put them up in the door ways. The instructions given seemed very confusing as it did not explain how it would be done to setup an entire network of these devices. With researching this device, it allows the understanding of what someone would realistically be willing to pay for a device with software that does something very similar to CrowdWatch (“Pearl Smart People Counter: Wireless Door Sensor/Visitor Counter”, n.d.).

## References for project

Barret, Chantel, and Endicott College. 2017. “Chantel Barret's IWorkout,” Chantel Barret's Senior Thesis. https://www.dropbox.com/sh/f5qibg5z11u37ue/AACB2KRmgS7IRU5QTwhzfrAha?dl=0&preview=barrettchantal_1169_687053_thesis+poster+v1-2.pptx.
Catalan, Kristian, and Endicott College. 2017. “Kristian Catalan's Campus Crowd Poster.” Endicott College. https://www.dropbox.com/sh/f5qibg5z11u37ue/AACB2KRmgS7IRU5QTwhzfrAha?dl=0&preview=catalankristian_late_2533_72109_poster3.pdf.
“GymIt Brookline.” n.d. GymIt. Accessed February 15, 2023. https://gymit.com/brookline/.
“Pearl Smart People Counter: Wireless Door Sensor/Visitor Counter - Directional in & Out Detection - Standard AA Batteries - Built-in WiFi - Time-Sensitive Reports - iOS & Android App (Black).” n.d. Amazon.com. Accessed February 15, 2023. https://www.amazon.com/Generation-People-Counter-Infrared-Sensor/dp/B07QSFBJ1J/ref=sr_1_4?keywords=Traffic+Counter&qid=1672682036&sr=8-4&ufe=app_do%3Aamzn1.fos.c3015c4a-46bb-44b9-81a4-dc28e6d374b3.
“Popular times, wait times, and visit duration - Google Business Profile Help.” n.d. Google Support. Accessed February 15, 2023. https://support.google.com/business/answer/6263531?hl=en.
“Retail.” n.d. Axper. Accessed February 15, 2023. https://axper.com/en/people-counting/retail/

## Full thesis Document found at link below

[CrowdWatch Full Thesis Document](https://docs.google.com/document/d/e/2PACX-1vRTV-NPqKuE_ZPC1UbwoRSEr2qawrUnvC-V6Zrq60OuKGlauEKXZC211aPnS4S6dEEOjoETfdSVDvTg/pub)
