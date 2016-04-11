var player, tl, tweets;
// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '378',
    width: '672',
    videoId: 'gTziWaeMYgM?rel=0',
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
  // tl = new TimelineLite();
  // tweets = document.querySelectorAll('.tweet-content');
  // console.log("Buffered and ready to play!");
}

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
function onPlayerStateChange(event) {
  var ps = player.getPlayerState();
  console.log(player.getCurrentTime(),player.getPlayerState());
  // if(ps === 1){
  //   tl.to(tweets, 3, {opacity:0});
  // }
}
