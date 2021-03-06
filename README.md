# The Neighborhood Map
This app is to demonstrate the ability to use a js framework (`knockout.js`) & Google Maps API.
The application allows one to view places to visit in Nairobi.

## Code
CSS - Two files make up the CSS files that are local. Bootstrap CSS is CDN based and not local, just easier to update as it is currently using **Bootstrap 4 Alpha**. CSS files that are included are:
- `bootstrap-vertical-menu.css` (CSS for the Nav Sidebar)
- `mapStyles.css` (Overwrites Bootstrap CSS for custom styling of app)

JS - There are quite a few here and I will try explain as best as possible without becoming too convoluted.
- `knockout-3.4.2.js` (Knockout framework)
- `app.js` (Main application file)
- `styles.js` (Contains the styles for the custom Google Maps look)
- `markers.js` (Contains place that are used to populate the map)

HTML - `Index.html` is where all the magic happens and all the data is binded.

## Features
A Google Maps implemenation that shows places (in my opinion) to visit in Nairobi.

## APIs Used

**Google Maps API** is used here to show the map and generate the markers etc.

**Foursquare API** is used here to get JSON data of a given place. The application uses the **Places API** to provide location-based searches into this app.The inforamtion of the place is shown when one clicks on the red marker and the infoWindow appears with the locatin details.

## Installation
Clone or download this repo and simply open the index.html file and enjoy!
You can make modifications to the locations and add your own in the `js/markers.js` file.

## Live Example
You can find a live running site of the application by clicking [here](https://bit.ly/2B1Euqe).

## How to Contribute

Contributions are welcomes. If you find any typos, errors, or additional resources. First, fork this repository. Please follow the contribution guidlines.

* You can Fork Icon the project.
* Or clone the repository to make changes.
```
$ git clone {REPOSITORY_CLONE_URL}
$ cd to the directory
```
* You can also Pull Request Icon by:

Making a pull request. Once you've pushed changes to your local repository, you can issue a pull request by clicking on the pull request icon.

### License

The contents of this repository are covered under the **MIT License**.
