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

FILE = "/Users/alejandro/Downloads/INC_MSG.txt"

import { readFile } from 'fs';

function handleFileSelect(event) {
  const fileInput = event.target;
  const file = fileInput.files[0];

  if (file) {
    const reader = new FileReader();

    reader.onload = function (e) {
      const content = e.target.result;
      displayFileContent(content);
    };

    reader.readAsText(file);
  }
}

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
  // fetch(serverUrl, {mode:'no-cors',
  // headers : { 
  //   'Content-Type': 'application/json',
  //   'Accept': 'application/json'
  //  }})
  //   .then(response => response.json())
  //   .then(data => {
  //     console.log(data)
  //   })
  let response = await fetch( serverUrl, {mode:'no-cors'})

  console.log("RESPONSEEE:::")
  console.log(response)
  msg = readFile(FILE,(err, inputD) => {
    if (err) throw err;
       console.log(inputD.toString());
  })
  console.log(msg)
  return name;
}

// async function fetchMessage(name) {
//     const response = await fetch(`/request`);

//     const json = await response.json();
//     console.log('Message:', json.message);
//     return json.message;

// }


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
