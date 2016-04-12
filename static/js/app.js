var player, tweets, timeouts = [];

console.log("json data: ",jsondata);
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

function stopClock(){
  for (var i = 0; i < timeouts.length; i++) {
    clearTimeout(timeouts[i]);
  }
  //quick reset of the timer array you just cleared
  timeouts = [];
  }

function onPlayerStateChange(event) {
  var ps = player.getPlayerState()
  pct = player.getCurrentTime();
  if(ps === 1){
    startClock();
  }else if(ps === 2){
    stopClock();
  }
}

function scheduleAnimations(){
  var ct = player.getCurrentTime();
  for(var anim in jsondata){
    if(ct < jsondata[anim].time)
      animate(jsondata[anim],ct);
  }
  // var anim = jsondata.filter(function(el){
  //     return el.time <= time + margin && el.time >= time - margin;
  //   })[0];
}

function animate(li_data,currentTime){
  timeouts.push(setTimeout(function(){
    var formatAbout = function(name,date){
      return '<a href="https://twitter.com/' + name + '" target="_blank">@' + name + '</a> &bull; '+ date;
    }

    var formatTweet = function(tweet,lyrics,reLyrics){
      return tweet.replace(reLyrics,'<span class="color">' +lyrics+'</span>');
    }

    //console.log(li_data);

    var li = tweets[li_data.li];
    var about = li.getElementsByClassName('about-tweet')[0],
    text = li.getElementsByClassName('tweet-text')[0];

    var newabout = formatAbout(li_data.tweet.handle,li_data.tweet.timestamp);
    var lyric = li_data.lyrics.replace(/"/g,'');
    newtext = formatTweet(li_data.tweet.text,lyric, new RegExp(lyric,'gi'));

    var tl = new TimelineLite();

    tl.set(about, {innerHTML: newabout, opacity: 0, rotationX: 90, rotationY: 0, transformOrigin:"0% 0% -50%"});
    tl.set(text, {innerHTML: newtext, opacity:0, rotationX: 90, rotationY: 0, transformOrigin:"0% 0% -50%"});
    tl.to(about, 2, {innerHTML: newabout, opacity:1, rotationX: 0, rotationY: 0, transformOrigin:"0% 0% 0%",ease:Power4.easeOut});
    tl.to(text, 2, {innerHTML: newtext, opacity:1, rotationX: 0, rotationY: 0, transformOrigin:"0% 0% 0%",ease:Power1.easeOut}, "-=2");

  }, 1000 * (li_data.time - currentTime)));
}
