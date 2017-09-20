var twit = require('twit');
var config = require('./config.js');
var fs = require('fs');

var Twitter = new twit(config);


var tweet = function() {

  var number = Math.random() * (1000 - 1) + 1;

  Twitter.post('statuses/update',
    { status: 'H ' + number }, function(err, data, response) {
    console.log(data)
  })
}

tweet();
// retweet in every 50 minutes
//setInterval(tweet, 1800000);

//
// post a tweet with media
//
