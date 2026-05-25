// ==========================================
// EMAIL SPAM DETECTOR - PROFESSIONAL UI JS
// ==========================================


// PAGE LOADED
window.addEventListener("load", () => {

    document.body.style.opacity = "1";

});



// ==========================================
// BUTTON LOADING EFFECT
// ==========================================

const button = document.querySelector("button");

if(button){

    button.addEventListener("click", () => {

        button.innerHTML = "Analyzing...";

        button.style.transform = "scale(0.96)";

        button.style.opacity = "0.85";

    });

}



// ==========================================
// TEXTAREA GLOW EFFECT
// ==========================================

const textarea = document.querySelector("textarea");

if(textarea){

    textarea.addEventListener("focus", () => {

        textarea.style.boxShadow =
        "0 0 25px rgba(211,124,255,0.35)";

    });

    textarea.addEventListener("blur", () => {

        textarea.style.boxShadow = "none";

    });

}



// ==========================================
// TYPING EFFECT FOR TITLE
// ==========================================

const title = document.querySelector("h1");

if(title){

    const originalText = title.innerHTML;

    title.innerHTML = "";

    let index = 0;

    function typeEffect(){

        if(index < originalText.length){

            title.innerHTML += originalText.charAt(index);

            index++;

            setTimeout(typeEffect, 25);

        }

    }

    typeEffect();

}



// ==========================================
// RESULT POPUP ANIMATION
// ==========================================

const resultBox = document.querySelector(".result-box");

if(resultBox){

    resultBox.style.opacity = "0";

    resultBox.style.transform = "translateY(20px)";

    setTimeout(() => {

        resultBox.style.transition = "0.5s ease";

        resultBox.style.opacity = "1";

        resultBox.style.transform = "translateY(0px)";

    }, 150);

}



// ==========================================
// AUTO HIDE RESULT
// ==========================================

if(resultBox){

    setTimeout(() => {

        resultBox.style.transition = "0.5s ease";

        resultBox.style.opacity = "0.2";

    }, 12000);

}



// ==========================================
// FLOATING CONTAINER EFFECT
// ==========================================

const container = document.querySelector(".container");

if(container){

    let position = 0;

    setInterval(() => {

        position += 0.02;

        container.style.transform =
        `translateY(${Math.sin(position) * 4}px)`;

    }, 30);

}



// ==========================================
// BACKGROUND SOFT GLOW ANIMATION
// ==========================================

const body = document.querySelector("body");

let glow = 0;

setInterval(() => {

    glow += 1;

    body.style.background = `
    radial-gradient(circle at top,
    rgba(${140 + glow % 20}, 90, 255, 0.12),
    #14091f 35%,
    #1d0f2e 100%)
    `;

}, 120);



// ==========================================
// TEXTAREA AUTO RESIZE
// ==========================================

if(textarea){

    textarea.addEventListener("input", () => {

        textarea.style.height = "auto";

        textarea.style.height =
        textarea.scrollHeight + "px";

    });

}



// ==========================================
// BUTTON HOVER GLOW
// ==========================================

if(button){

    button.addEventListener("mouseenter", () => {

        button.style.boxShadow =
        "0 0 30px rgba(211,124,255,0.5)";

    });

    button.addEventListener("mouseleave", () => {

        button.style.boxShadow =
        "0 0 18px rgba(200,111,255,0.25)";

    });

}



// ==========================================
// CONSOLE MESSAGE
// ==========================================

console.log("Email Spam Detector Loaded Successfully");