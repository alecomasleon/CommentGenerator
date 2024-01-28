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
            console.log(cameraSensor.toDataURL("image/jpeg"));
            url = cameraSensor.toDataURL("image/jpeg");
        };
        // Start the video stream when the window loads
        window.addEventListener("load", cameraStart, false);




const btn = document.getElementById('camera--trigger');

function generateUniqueCode(length) {
  const uppercaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz';
  let code;

    code = '';
    for (let i = 0; i < length; i++) {
      code += uppercaseLetters.charAt(Math.floor(Math.random() * uppercaseLetters.length));
    }

  return code;
}

btn.addEventListener('click', (event) => {
  event.preventDefault();
  console.log('ABC')
  console.log(downloadImage(url))
})

 async function downloadImage(url) {
  var name = generateUniqueCode(8) + ".jpg"
  var a = document.createElement('a');
  a.href = url;
  a.download = name;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);

  const serverUrl = new URL("http://127.0.0.1:9000/request")
  const params = { 'name': name}
  serverUrl.search = new URLSearchParams(params)
  let response = await fetch( serverUrl, {mode:'no-cors'})

  console.log("RESPONSEEE:::")
  console.log(response)
  return name;
}

async function fetchMessage(name) {
  try {
    const response = await fetch(`/request?name=${name}`);
    if (!response.ok) {
      throw new Error(`Failed to fetch data. Status: ${response.status}`);
    }

    const json = await response.json();
    console.log('Message:', json.message);
    return json.message;
  } catch (error) {
    console.error('Error fetching message:', error.message);
    throw error;
  }
}


//.then(responseData => {
//    // Handle the response from the server if needed
//    console.log('Server response:', responseData);
//   })
//.catch(error => {
//// Handle errors that occur during the fetch
//console.error('Error during fetch:', error);
//});
//  return url;
//}
