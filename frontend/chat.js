const chat_box = document.querySelector(".chatbox_body");
const sendBtn = document.querySelector(".chatbox_footer i")


var gpt_msg = [""];

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
    let description = choice[Math.floor(Math.random() * choice.length)];

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
        // gptPrint(gpt_msg);
    }
});
document.body.addEventListener('keydown', e => {
    if(e.key == 'Enter' && document.querySelector(".chatbox_footer input").value != '') {
        printChat();
        document.querySelector(".pendinguser").remove();
        // gptPrint(gpt_msg);
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
