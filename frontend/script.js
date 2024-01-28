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
  const le_mesaj = async () => {await downloadImage(url)};
  gptPrint(async () => {await downloadImage(url)});
})

FILE = "/Users/alejandro/Downloads/INC_MSG.txt"

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

//import {readFile} from 'fs'

async function downloadImage(url) {
  var name = generateUniqueCode(8) + ".jpg"
  var a = document.createElement('a');
  a.href = url;
  a.download = name;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);

  const serverUrl = new URL("http://127.0.0.1:9000/request") // CHANGE TO request
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
  serverUrl.headers = {'Access-Control-Allow-Origin': 'http://localhost:9000'}
  let response = await fetch( serverUrl, {mode:'cors'})

  console.log("RESPONSEEE:::")
  console.log(response)
  console.log(response.body)
  var msg = await response.json()
  console.log(msg)
  // msg = readFile(FILE,(err, inputD) => {
  //   if (err) throw err;
  //      console.log(inputD.toString());
  // })
  return msg;
}


const chat_box = document.querySelector(".chatbox_body");
const sendBtn = document.querySelector(".chatbox_footer i")

const apiUrl = 'http://localhost:9000/roast';

function getroast(apiUrl, dataArray) {
    return fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        return JSON.parse(data).roast;
        // Do something with the data
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });
}

  function getcompliment(apiUrl, dataArray) {
    return fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        return JSON.parse(data).compliment;
        // Do something with the data
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });
}

function gptPrint(mesaj) {
    
        setTimeout(() => {
            if(document.querySelector(".gptpend") == undefined) {
            document.querySelector(".chatbox_body ul").insertAdjacentHTML("beforeend", `
            <div class="typing pending gptpend">
                <span></span>
                <span></span>
                <span></span>
            </div>
            `);
            scrollToBottom();
            setTimeout(() => {
                document.querySelector(".gptpend").remove()
                printGpt(mesaj);
            }, 1500);}
        }, 1000);
    }


const printChat = () => {
    let description = document.querySelector(".chatbox_footer input").value;

    let li = `
        <li class='message user'>${description}</li>
    `;

    document.querySelector(".chatbox_body ul").insertAdjacentHTML("beforeend", li);

    document.querySelector(".chatbox_footer input").value = '';
    scrollToBottom();
}

const printGpt = (choice) => {
    console.log(choice)
    let description = choice;

    let li = `
        <li class='message gpt'>${description}</li>
    `;

    document.querySelector(".chatbox_body ul").insertAdjacentHTML("beforeend", li);

    scrollToBottom();
}

sendBtn.addEventListener("click", () => {
    if(document.querySelector(".chatbox_footer input").value != '') {
        printChat();
        document.querySelector(".pendinguser").remove();
        gptPrint();
    }
});
document.body.addEventListener('keydown', e => {
    if(e.key == 'Enter' && document.querySelector(".chatbox_footer input").value != '') {
        printChat();
        document.querySelector(".pendinguser").remove();
        gptPrint();
    }
});

function scrollToBottom() {
    document.querySelector(".chatbox_body").scrollTop = document.querySelector(".chatbox_body").scrollHeight;
}



document.querySelector(".compliment").addEventListener("click", () => {
    document.querySelector(".chatbox_body ul").insertAdjacentHTML("beforeend", `<li class='message user'>Compliment me please!</li>`);
    document.querySelector(".options").remove();
    // gptPrint(gpt_msg);
    
    scrollToBottom();
})
document.querySelector(".insult").addEventListener("click", () => {
    document.querySelector(".chatbox_body ul").insertAdjacentHTML("beforeend", `<li class='message user'>Insult me please!</li>`);
    document.querySelector(".options").remove();
    // gptPrint(gpt_msg);

    scrollToBottom();
})



let mode = "light mode";

document.querySelector("#color-mode").addEventListener("click", () => {
    const le_btn = document.querySelector("#color-mode");

    if(mode == "dark mode") {
        le_btn.classList.remove("fa-moon");
        le_btn.classList.add("fa-sun");

        document.querySelector(".area").style.background = "#a9abc4";
        document.querySelector(".chatbox_body").style.background = "#EEE";
        document.querySelector(".chatbox_footer input").style.background = "#FFF";
        document.querySelector(".chatbox_footer").style.background = "#FFF";
        document.querySelector(".chatbox_footer input").style.color = "#000";
        document.querySelector(".chatbox_footer").style.color = "#000";

        document.documentElement.style.setProperty('--green', '#8eb686');
        document.documentElement.style.setProperty('--text_color', '#000');
        document.documentElement.style.setProperty('--purple', '#7d559b');
        document.documentElement.style.setProperty('--button_color', '#000');
        document.documentElement.style.setProperty('--button_bg', 'rgba(255, 255, 255, 0.2)');

        mode = "light mode";
    } else {
        le_btn.classList.remove("fa-sun");
        le_btn.classList.add("fa-moon");

        document.querySelector(".area").style.background = "#242642";
        document.querySelector(".chatbox_body").style.background = "#2D2E43";
        document.querySelector(".chatbox_footer input").style.background = "#343651";
        document.querySelector(".chatbox_footer").style.background = "#343651";
        document.querySelector(".chatbox_footer input").style.color = "#FFF";
        document.querySelector(".chatbox_footer").style.color = "#FFF";

        document.documentElement.style.setProperty('--green', '#5c7b56');
        document.documentElement.style.setProperty('--text_color', '#FFF');
        document.documentElement.style.setProperty('--purple', '#745190');
        document.documentElement.style.setProperty('--button_color', '#FFF');
        document.documentElement.style.setProperty('--button_bg', 'rgba(255, 255, 255, 0.1)');

        mode = "dark mode";
    }
})


document.querySelector(".chatbox_footer input").addEventListener("input", () => {
    if(document.querySelector(".pendinguser") == undefined) {
        document.querySelector(".chatbox_body ul").insertAdjacentHTML("beforeend", `
        <div class="typing pending pendinguser">
            <span></span>
            <span></span>
            <span></span>
        </div>
        `)
        scrollToBottom();
    }
});
