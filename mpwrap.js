var http = require('http');

var endpoint = "http://www.mountainproject.com/data/get-routes-for-lat-lon?lat=%LAT%.72&lon=%LON%&maxDistance=%DIST%&key=%KEY%"

//https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js


//var script ;
//script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js';
//script.type = 'text/javascript';

var getCrag = exports.getCrag = function(lat, lon, dist) {
    var replacements =  {
        "%LAT%": "33.72",
        "%LON%": "-84.6",
        "%DIST%": "20",
        "%KEY%" : ''

        // "%LAT%": lat,
        // "%LON%": lon,
        // "%DIST%": dist
    };
    endpoint = endpoint.replace(/%\w+%/g, function(all) {
        return replacements[all] || all;
    });

    console.log(endpoint);

    // var data = $.getJSON(endpoint, function(data) {
    //     console.log(data);
    // });
}

getCrag();
