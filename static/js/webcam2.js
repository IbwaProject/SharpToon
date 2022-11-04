var myVideoStream = document.getElementById('myVideo')     // make it a global variable
  var myStoredInterval = 0
  
function getVideo(){
  navigator.getMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
  navigator.getMedia({video: true, audio: false},
                     
    function(stream) {
      myVideoStream.srcObject = stream   
      myVideoStream.play();
  }, 
                     
   function(error) {
     alert('webcam not working');
  });
  
  document.getElementById("takepicture").style.display="inline";
}
  
function takeSnapshot(div) {
   var myCanvasElement = document.getElementById('myCanvas');
   var myCTX = myCanvasElement.getContext('2d');
   myCTX.drawImage(myVideoStream, 0, 0, myCanvasElement.width, myCanvasElement.height);

   var a = document.createElement("a");
   a.href = myCanvasElement.toDataURL();
   var fileName = "imageTemp1.jpg";
  //  var filepath = "{{url_for('static', filename = 'images/input/imageTemp1.jpg')}}";
  //  a.setAttribute('href', filepath);
   a.setAttribute("download", fileName);
   document.body.appendChild(a);
   a.click();
   document.body.removeChild(a);
}
  
function takeAuto() {
    takeSnapshot() // get snapshot right away then wait and repeat
    clearInterval(myStoredInterval)
    myStoredInterval = setInterval(function(){                                                                                         
       takeSnapshot()
   }, document.getElementById('myInterval').value);        
}