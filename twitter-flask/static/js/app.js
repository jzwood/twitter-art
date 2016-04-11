var player, tweets;
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

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
  tweets = document.querySelectorAll('.tweet-content');
  console.log("Buffered and ready to play!");
}

function startClock(){
  setTimeout(function(){ scheduleAnimations(); }, 2000);
}

function onPlayerStateChange(event) {
  var ps = player.getPlayerState()
  pct = player.getCurrentTime();
  if(ps === 1 && pct < 2){
    startClock();
  }
}

function scheduleAnimations(){
  for(var anim in jsondata){
    //console.log(jsondata[anim]);
    animate(jsondata[anim]);
  }
  // var anim = jsondata.filter(function(el){
  //     return el.time <= time + margin && el.time >= time - margin;
  //   })[0];
}

function animate(li_data){
  setTimeout(function(){
    var formatAbout = function(name,date){
      return '<a href="https://twitter.com/' + name + '" target="_blank">@' + name + '</a> &bull; '+ date;
    }

    var formatTweet = function(tweet,lyrics){
      return tweet.replace(lyrics,'<span style="color:#F5D824">' +lyrics+'</span>');
    }

    //console.log(li_data);

    var li = tweets[li_data.li];
    var about = li.getElementsByClassName('about-tweet')[0],
    text = li.getElementsByClassName('tweet-text')[0];

    var newabout = formatAbout(li_data.tweet.handle,li_data.tweet.timestamp),
    newtext = li_data.tweet.text;//formatTweet(li_data.tweet.text,li_data.lyrics.replace(/"/g,''));
    console.log(newabout,newtext)

    var tl = new TimelineLite();
    
    tl.set(about, {innerHTML: newabout, opacity: 0, rotationX: 90, rotationY: 0, transformOrigin:"0% 0% -50%"});
    tl.set(text, {innerHTML: newtext, opacity:0, rotationX: 90, rotationY: 0, transformOrigin:"0% 0% -50%"});
    tl.to(about, 2, {innerHTML: newabout, opacity:1, rotationX: 0, rotationY: 0, transformOrigin:"0% 0% 0%",ease:Power4.easeOut});
    tl.to(text, 2, {innerHTML: newtext, opacity:1, rotationX: 0, rotationY: 0, transformOrigin:"0% 0% 0%",ease:Power1.easeOut}, "-=2");
  }, 1000 * (li_data.time - player.getCurrentTime()));
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
