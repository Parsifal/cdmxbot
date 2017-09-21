//Require
var twit = require('twit');
var config = require('./config.js');
var fs = require('fs');

//Principal para usar la API de Twitter
var Twitter = new twit(config);

//Function para twittear
var tweetParams = function(params) {
  Twitter.post('statuses/update',
    params, function(err, data, response) {
    console.log(data)
  })
}

var stream = Twitter.stream('statuses/filter', { track: ['@cdmxbot #buscoa'] });
stream.on('tweet', tweetEvent);

function tweetEvent(tweet) {

    // User
    var name = tweet.user.screen_name;
    // Texto
    var txt = tweet.text;
    var regexp = new RegExp('#([^\\s]*)','g'); //Quitando las hashtags
    txt = txt.replace(regexp, '');
    txt = txt.replace('@cdmxbot', ''); //Quitando la mención al bot

    var tweetID  = tweet.id_str;

    //Buscaremos #sismo junto a lo que haya escrito el usuario, sólo desde el 19 de septiembre
    var thequery = '#sismo AND ' + txt + ' since:2017-09-19';

    //Busca lo recibido
    //Luego por cada tweet encontrado, se responde al usuario
    Twitter.get('search/tweets', { q: thequery, count: 3, result_type:'recent' }, function(err, data, response) {

        var total = data.statuses.length;

        Array.from(data.statuses).forEach(function(item, index){
          //Armando el objeto para twittear la respuesta
          var reply = '@' + name + ' Encontré esto (' + (index+1) + '/' + total + '): https://twitter.com/statuses/' + item.id_str ;

          var params             = {
                                    status: reply,
                                    in_reply_to_status_id: tweetID
                                   };
        //Twitteando la respuesta
        tweetParams(params);

        });
    })

};
