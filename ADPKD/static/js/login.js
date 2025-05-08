// user id user icon color change
const userInput = document.querySelector(".userId input");
const userIcon = document.querySelector(".userId .user-icon");

userInput.addEventListener("keyup", () =>{
    let pattern = /^[a-zA-Z][a-zA-Z0-9_]{5,12}$/;
    if(userInput.value === "") {
        userIcon.classList.replace("bx-check-circle", "bx-user");
        return userIcon.style.color = "#bfbfbf";
    }   
    if(userInput.value.match(pattern)){
        userIcon.classList.replace("bx-user" , "bx-check-circle");
        return userIcon.style.color = "#4bb543";
    }
    userIcon.classList.replace("bx-check-circle", "bx-user");
    return userIcon.style.color = "#de0611";
});

//show passsword vision icon  
const passwordInput = document.querySelector(".password input");
const eyeIcon = document.querySelector(".password .visible");
var num = 1;

eyeIcon.onclick = () => {
    if (num === 1) {
        passwordInput.type = 'text';
        eyeIcon.style.color = 'black';
        num--;
    } else {
        passwordInput.type = 'password';
        eyeIcon.style.color = '#bfbfbf';
        num++;
    }
}

// password lock icon color change
const lockIcon =  document.querySelector('.password .lock-icon');

passwordInput.addEventListener("keyup", () =>{
    let pattern2 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
    if(passwordInput.value === "") {
        lockIcon.classList.replace("bx-check-circle", "bx-lock");
        return lockIcon.style.color = "#bfbfbf";
    }   
    if(passwordInput.value.match(pattern2)){
        lockIcon.classList.replace("bx-lock" , "bx-check-circle");
        return lockIcon.style.color = "#4bb543";
    }
    lockIcon.classList.replace("bx-check-circle", "bx-lock");
    return lockIcon.style.color = "#de0611";
});









const form = document.querySelector('.login form'); // Select the form
const userIdField = form.querySelector('.login .userId');
const userIdInput = userIdField.querySelector('.login .userId input');
const passField = form.querySelector('.login .password');
const passInput = passField.querySelector('.login .password input');
const loginbtn = document.querySelector(".login .submit-btn");


var returnValue =true;


//Log in user id validation
function checkUserId() {
    const UserIdPattern = /^[a-zA-Z][a-zA-Z0-9_]{5,12}$/;; 
    if (userIdInput.value === "") {
        userIdInput.style.borderBottom = "2px solid #ff0000";
        userIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    if (!userIdInput.value.match(UserIdPattern)) {
        userIdInput.style.borderBottom = "2px solid #ff0000";
        userIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    userIdInput.style.borderBottom = "2px solid #bfbfbf";
    return returnValue = true;
}

//Log in password validation
function checkPassword() {
    const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
    if (passInput.value === "") {
        passInput.style.borderBottom = "2px solid #ff0000";
        lockIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    if (!passInput.value.match(passwordPattern)) {
        passInput.style.borderBottom = "2px solid #ff0000";
        lockIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    passInput.style.borderBottom = "2px solid #bfbfbf";
    return returnValue = true;
}


// calling function on Form Submit

loginbtn.onclick =  function loginValidation() {
        checkUserId();
        checkPassword();
        return returnValue;
    }