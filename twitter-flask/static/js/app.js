var player, tl, tweets, clock;
console.log("json data here: ",jsondata);
// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '378',
    width: '672',
    videoId: 'Hh-1Lag3BV8',
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
  //we want to repress fullscreen
  document.getElementById('player').removeAttribute("allowfullscreen");
}

// player.addEventListener()

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
  tl = new TimelineLite();
  tweets = document.querySelectorAll('.tweet-content');
  // tweets = document.querySelectorAll('.tweet-content');
  startClockListener();
  console.log("Buffered and ready to play!");
}

function startClockListener(){
  clock = setInterval(function(){ exeAnimation(0.25) }, 500);
}

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
function onPlayerStateChange(event) {
  var ps = player.getPlayerState()
  pct = player.getCurrentTime();
}

function exeAnimation(margin){
  var time = player.getCurrentTime();

  var anim = jsondata.filter(function(el){
      return el.time <= time + margin && el.time >= time - margin;
    })[0];

  var formatAbout = function(name,date){
    return '<a href="https://twitter.com/' + name + '" target="_blank">@' + name + '</a> &bull; '+ date;
  }

  var formatTweet = function(tweet,lyrics){
    return tweet.replace(lyrics,'<span style="color:#F5D824">' +lyrics+'</span>');
  }

  if(anim){
    console.log(anim, time);
    var li = tweets[anim.li];
    var about = li.getElementsByClassName('about-tweet'),
    text = li.getElementsByClassName('tweet-text');

    tl.set(about, {opacity:0, innerHTML:formatAbout(anim.tweet.handle,anim.tweet.timestamp), rotationX: 90, rotationY: 0, transformOrigin:"0% 0% -50%"});
    tl.set(text, {opacity:0, innerHTML:formatTweet(anim.tweet.text,anim.lyrics.replace(/"/g,'')), rotationX: 90, rotationY: 0, transformOrigin:"0% 0% -50%"});
    tl.to(about, 2, {opacity:1, rotationX: 0, rotationY: 0, transformOrigin:"0% 0% 0%",ease:Power4.easeOut});
    tl.to(text, 2, {opacity:1, rotationX: 0, rotationY: 0, transformOrigin:"0% 0% 0%",ease:Power1.easeOut}, "-=2");
  }
}

// var tweets = document.getElementById('tweet-list');
// //tweets = document.getElementById('tweet-list');
// var tweetAbout = document.querySelectorAll('.about-tweet');
//

//
// window.addEventListener("keydown", handle, true);
//
// function handle(){
//   // var height = tweetOne[0].getBoundingClientRect().height * 1.5;
//   // tl.set(tweets, {y:height});
//   var newText = "Did you know that there are over 175,000 #youngcarers (5-18yrs) in the UK? Join us on @itvthismorning today where we'll be meeting some!";
//
//   tl.to(tweetAbout, 2, {opacity:1, rotationX: 0, rotationY: 0, transformOrigin:"0% 0% 0%",ease:Power4.easeOut});
//   tl.to(tweetOne, 1.5, {opacity:1, rotationX: 0, rotationY: 0, transformOrigin:"0% 0% 0%",ease:Power1.easeOut}, "-=2");
//
//   tl.to(tweetOne, 10, {opacity:1});
//
//   tl.to(tweetAbout, 2, {opacity:0, rotationX: -90, ease:Power4.easeOut});
//   tl.to(tweetOne, 2, {opacity:0, rotationX: -90, ease:Power4.easeOut}, "-=2");
//
//   tl.set(tweetOne, {opacity:0, innerText:newText, rotationX: 90, transformOrigin:"0% 0% -50%"});
//   tl.set(tweetAbout, {opacity:0, rotationX: 180, transformOrigin:"0% 0% -50%"});
// }
