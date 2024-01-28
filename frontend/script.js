        // Set constraints for the video stream
        var constraints = { video: { facingMode: "user" }, audio: false };
        // Define constants
        const cameraView = document.querySelector("#camera--view"),
            cameraOutput = document.querySelector("#camera--output"),
            cameraSensor = document.querySelector("#camera--sensor"),
            cameraTrigger = document.querySelector("#camera--trigger")
        // Access the device camera and stream to cameraView
        function cameraStart() {
            navigator.mediaDevices
                .getUserMedia(constraints)
                .then(function(stream) {
                track = stream.getTracks()[0];
                cameraView.srcObject = stream;
            })
            .catch(function(error) {
                console.error("Oops. Something is broken.", error);
            });
        }
        // Take a picture when cameraTrigger is tapped
        var url;
        cameraTrigger.onclick = function() {
            cameraSensor.width = cameraView.videoWidth;
            cameraSensor.height = cameraView.videoHeight;
            cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
            // cameraOutput.src = cameraSensor.toDataURL("image/png");
            // cameraOutput.classList.add("taken");
            console.log(cameraSensor.toDataURL("image/png"));
            url = cameraSensor.toDataURL("image/png");
        };
        // Start the video stream when the window loads
        window.addEventListener("load", cameraStart, false);




const btn = document.getElementById('camera--trigger');


btn.addEventListener('click', (event) => {
  event.preventDefault();
  console.log('ABC')
  downloadImage(url);
})


function downloadImage(url) {
  fetch(url, {
    mode : 'no-cors',
  })
    .then(response => response.blob())
    .then(blob => {
    let blobUrl = window.URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.download = url.replace(/^.*[\\\/]/, '');
    a.href = blobUrl;
    document.body.appendChild(a);
    a.click();
    a.remove();
  })
}
