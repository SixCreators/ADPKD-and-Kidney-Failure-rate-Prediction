    const form = document.querySelector('.form-box.login form'); // Select the form
    const emailField = form.querySelector('.form-box.login .email');
    const emailInput = emailField.querySelector('.form-box.login .email-input');
    const passField = form.querySelector('.form-box.login .password');
    const passInput = passField.querySelector('.form-box.login .password-input');
    const loginbtn = document.querySelector(".login .submit-btn");

    
    var returnValue =true;


    //Log in Email validation
    function checkEmail() {
        const Email_pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; 
        if (emailInput.value === "") {
            emailField.classList.remove("invalidEmail");
            returnValue = false;
            return emailField.classList.add("emptyEmail");
        }
        if (!emailInput.value.match(Email_pattern)) {
            emailField.classList.remove("emptyEmail");
            returnValue = false;
            return emailField.classList.add("invalidEmail");
        }
        
        emailField.classList.remove("invalidEmail");
        emailField.classList.remove("emptyEmail");
        returnValue = true;
    }

    //Log in password validation
    function checkPassword() {
        const Password_pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
        if (passInput.value === "") {
            passField.classList.remove("invalidPassword");
            returnValue = false;
            return passField.classList.add("emptyPassword");
        }
        if (!passInput.value.match(Password_pattern)) {
            passField.classList.remove("emptyPassword");
            returnValue = false;
            return passField.classList.add("invalidPassword");
        }
        
        passField.classList.remove("invalidPassword");
        passField.classList.remove("emptyPassword");
        returnValue = true;
    }


    // calling function on Form Submit

    loginbtn.onclick =  function loginValidation() {
            checkEmail();
            checkPassword();
            return returnValue;
        }

    const form2 = document.querySelector('.register form'); // Select the form 2
    const emailField2 = form2.querySelector('.register .email');
    const emailInput2 = emailField2.querySelector('.register .email-input');
    const passField2 = form2.querySelector('.register .password');
    const passInput2 = passField2.querySelector('.register .password-input');
    const userNameField2 = form2.querySelector(".register .user-name");
    const userNameInput2 = userNameField2.querySelector(".register .user-name-input");
    const registerbtn = document.querySelector(".register .submit-btn");
    const agreeCheckedbox = document.querySelector(".register .agreeChecked");

    var returnValue2 = true;

    //register user Name validation
    function checkUsername2() {
        const Username_pattern2 = /^[a-zA-Z][a-zA-Z0-9_]{5,20}$/; 
        if (userNameInput2.value === "") {
            userNameField2.classList.remove("invalidUsername2");
            returnValue2 = false;
            return userNameField2.classList.add("emptyUsername2");
        }
        if (!userNameInput2.value.match(Username_pattern2)) {
            userNameField2.classList.remove("emptyUsername2");
            returnValue2 = false;
            return userNameField2.classList.add("invalidUsername2");
        }
        
        userNameField2.classList.remove("invalidUsername2");
        userNameField2.classList.remove("emptyUsername2");
        returnValue2 = true;
    }

    //register Email validation
    function checkEmail2() {
        const Email_pattern2 = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; 
        if (emailInput2.value === "") {
            emailField2.classList.remove("invalidEmail2");
            returnValue2 = false;
            return emailField2.classList.add("emptyEmail2");
        }
        if (!emailInput2.value.match(Email_pattern2)) {
            emailField2.classList.remove("emptyEmail2");
            returnValue2 = false;
            return emailField2.classList.add("invalidEmail2");
        }
        
        emailField2.classList.remove("invalidEmail2");
        emailField2.classList.remove("emptyEmail2");
        returnValue2 = true;
    }

    //register password validation
    function checkPassword2() {
        const Password_pattern2 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
        if (passInput2.value === "") {
            passField2.classList.remove("invalidPassword2");
            returnValue2 = false;
            return passField2.classList.add("emptyPassword2");
        }
        if (!passInput2.value.match(Password_pattern2)) {
            passField2.classList.remove("emptyPassword2");
            returnValue2 = false;
            return passField2.classList.add("invalidPassword2");
        }
        
        passField2.classList.remove("invalidPassword2");
        passField2.classList.remove("emptyPassword2");
        returnValue2 = true;
    }


    // agree checked validation
    function agreeCheckedBox() {
        if (agreeCheckedbox.checked) {
            return returnValue2 = true;
        } else {
            return returnValue2 = false;
        }
    }


    // calling function on Form Submit
    registerbtn.onclick = function registerValidation() {
        checkUsername2();
        checkEmail2();
        checkPassword2();
        agreeCheckedBox();
        return returnValue2;
    }

//Login & Register design

const container = document.querySelector('.container');
const registerBtn = document.querySelector('.register-btn');
const loginBtn = document.querySelector('.login-btn');


registerBtn.addEventListener('click', () => {
    container.classList.add('active');
});

loginBtn.addEventListener('click', () => {
    container.classList.remove('active');
});


// input box login envelop icon color change
const input = document.querySelector('.form-box.login .input-area.email input');
const email_icon = document.querySelector('.form-box.login .input-area.email .email-icon');


input.addEventListener("keyup", () =>{
    let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if(input.value === "") {
        email_icon.classList.replace("bx-check-circle", "bx-envelope");
        return email_icon.style.color = "#bfbfbf"
    }   
    if(input.value.match(pattern)){
        email_icon.classList.replace("bx-envelope" , "bx-check-circle");
        return email_icon.style.color = "#4bb543"
    }
    email_icon.classList.replace("bx-check-circle", "bx-envelope");
    return email_icon.style.color = "#de0611"
});


// input box login lock icon color change
const input2 = document.querySelector('.form-box.login .input-area.password input');
const lock_icon =  document.querySelector('.form-box.login .input-area.password .lock-icon');


input2.addEventListener("keyup", () =>{
    let pattern2 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
    if(input2.value === "") {
        lock_icon.classList.replace("bx-check-circle", "bx-lock");
        return lock_icon.style.color = "#bfbfbf"
    }   
    if(input2.value.match(pattern2)){
        lock_icon.classList.replace("bx-lock" , "bx-check-circle");
        return lock_icon.style.color = "#4bb543"
    }
    lock_icon.classList.replace("bx-check-circle", "bx-lock");
    return lock_icon.style.color = "#de0611"
});


// input box register user icon color change
const input3 = document.querySelector('.form-box.register .input-area.user-name input');
const user_icon = document.querySelector('.user-icon');


input3.addEventListener("keyup", () =>{
    let pattern3 = /^[a-zA-Z][a-zA-Z0-9_]{5,12}$/;
    if(input3.value === "") {
        user_icon.classList.replace("bx-check-circle", "bx-user");
        return user_icon.style.color = "#bfbfbf"
    }   
    if(input3.value.match(pattern3)){
        user_icon.classList.replace("bx-user" , "bx-check-circle");
        return user_icon.style.color = "#4bb543"
    }
    user_icon.classList.replace("bx-check-circle", "bx-user");
    return user_icon.style.color = "#de0611"
});


// input box register lock icon color change
const input4 = document.querySelector('.form-box.register .input-area.password input');
const lock_icon2 =  document.querySelector('.form-box.register .input-area.password .lock-icon');


input4.addEventListener("keyup", () =>{
    let pattern4 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
    if(input4.value === "") {
        lock_icon2.classList.replace("bx-check-circle", "bx-lock");
        return lock_icon2.style.color = "#bfbfbf"
    }   
    if(input4.value.match(pattern4)){
        lock_icon2.classList.replace("bx-lock" , "bx-check-circle");
        return lock_icon2.style.color = "#4bb543"
    }
    lock_icon2.classList.replace("bx-check-circle", "bx-lock");
    return lock_icon2.style.color = "#de0611"
});


// input box register envelop icon color change
const input5 = document.querySelector('.form-box.register .input-area.email input');
const email_icon2 = document.querySelector('.form-box.register .input-area.email .email-icon');


input5.addEventListener("keyup", () =>{
    let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if(input5.value === "") {
        email_icon2.classList.replace("bx-check-circle", "bx-envelope");
        return email_icon2.style.color = "#bfbfbf"
    }   
    if(input5.value.match(pattern)){
        email_icon2.classList.replace("bx-envelope" , "bx-check-circle");
        return email_icon2.style.color = "#4bb543"
    }
    email_icon2.classList.replace("bx-check-circle", "bx-envelope");
    return email_icon2.style.color = "#de0611"
});



//logi show passsword check box 
let input_password = document.querySelector(".login .password-input");
let checkedBox = document.querySelector(".login .showPassword");

checkedBox.onclick = () => {
    if (checkedBox.checked) {
        input_password.type = 'text';
    } else {
        input_password.type = 'password';
    }
}


//register show passsword check box 
const input_password2 = document.querySelector(".register .password-input");
const checkedBox2 = document.querySelector(".register .showPassword");

checkedBox2.onclick = () => {
    if (checkedBox2.checked) {
        input_password2.type = 'text';
    } else {
        input_password2.type = 'password';
    }
}