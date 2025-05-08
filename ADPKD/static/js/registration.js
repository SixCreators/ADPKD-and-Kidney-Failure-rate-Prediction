// user id user icon color change
const userInput = document.querySelector(".userId input");
const userIcon = document.querySelector(".userId .user-icon");

userInput.addEventListener("keyup", () =>{
    let pattern = /^[a-zA-Z][a-zA-Z0-9_]{5,12}$/;
    if(userInput.value === "") {
        userIcon.classList.replace("bx-check-circle", "bx-user");
        return userIcon.style.color = "#bfbfbf"
    }   
    if(userInput.value.match(pattern)){
        userIcon.classList.replace("bx-user" , "bx-check-circle");
        return userIcon.style.color = "#4bb543"
    }
    userIcon.classList.replace("bx-check-circle", "bx-user");
    return userIcon.style.color = "#de0611"
});

// First name text icon color change
const firstNameInput = document.querySelector(".firstName input");
const firstNameIcon = document.querySelector(".firstName .FName-icon");

firstNameInput.addEventListener("keyup", () =>{
    let pattern2 = /^[a-zA-Z][a-zA-Z]{1,25}$/;
    if(firstNameInput.value === "") {
        firstNameIcon.classList.replace("bx-check-circle", "bx-text");
        return firstNameIcon.style.color = "#bfbfbf"
    }   
    if(firstNameInput.value.match(pattern2)){
        firstNameIcon.classList.replace("bx-text" , "bx-check-circle");
        return firstNameIcon.style.color = "#4bb543"
    }
    firstNameIcon.classList.replace("bx-check-circle", "bx-text");
    return firstNameIcon.style.color = "#de0611"
});


//  Last name text icon color change
const lastNameInput = document.querySelector(".lastName input");
const lastNameIcon = document.querySelector(".lastName .LName-icon");

lastNameInput.addEventListener("keyup", () =>{
    let pattern2 = /^[a-zA-Z][a-zA-Z]{1,25}$/;
    if(lastNameInput.value === "") {
        lastNameIcon.classList.replace("bx-check-circle", "bx-text");
        return lastNameIcon.style.color = "#bfbfbf"
    }   
    if(lastNameInput.value.match(pattern2)){
        lastNameIcon.classList.replace("bx-text" , "bx-check-circle");
        return lastNameIcon.style.color = "#4bb543"
    }
    lastNameIcon.classList.replace("bx-check-circle", "bx-text");
    return lastNameIcon.style.color = "#de0611"
});


// Email envelop icon color change
const emailInput = document.querySelector('.email input');
const emailIcon = document.querySelector('.email .email-icon');

emailInput.addEventListener("keyup", () =>{
    let pattern3 = /^[a-z0-9._~-]+@[a-z]+\.[a-z]{2,3}$/;
    if(emailInput.value === "") {
        emailIcon.classList.replace("bx-check-circle", "bx-envelope");
        return emailIcon.style.color = "#bfbfbf"
    }   
    if(emailInput.value.match(pattern3)){
        emailIcon.classList.replace("bx-envelope" , "bx-check-circle");
        return emailIcon.style.color = "#4bb543"
    }
    emailIcon.classList.replace("bx-check-circle", "bx-envelope");
    return emailIcon.style.color = "#de0611"
});


// Phone number phone icon color change
const phoneNoInput = document.querySelector('.phoneNo input');
const phoneNoIcon = document.querySelector('.phoneNo .phone-icon');
const country =  document.querySelector('.country select');

phoneNoInput.addEventListener("keyup", () =>{
    let pattern4 = /^[0-9]{10}$/;
    if(phoneNoInput.value === "") {
        phoneNoIcon.classList.replace("bx-check-circle", "bx-phone");
        return phoneNoIcon.style.color = "#bfbfbf"
    }   
    if(phoneNoInput.value.match(pattern4) && country.value === "India"){
        phoneNoIcon.classList.replace("bx-phone" , "bx-check-circle");
        return phoneNoIcon.style.color = "#4bb543"
    }
    phoneNoIcon.classList.replace("bx-check-circle", "bx-phone");
    return phoneNoIcon.style.color = "#de0611"
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
    let pattern5 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
    if(passwordInput.value === "") {
        lockIcon.classList.replace("bx-check-circle", "bx-lock");
        return lockIcon.style.color = "#bfbfbf"
    }   
    if(passwordInput.value.match(pattern5)){
        lockIcon.classList.replace("bx-lock" , "bx-check-circle");
        return lockIcon.style.color = "#4bb543"
    }
    lockIcon.classList.replace("bx-check-circle", "bx-lock");
    return lockIcon.style.color = "#de0611"
});


//show confirm passsword check box 
const confirmPasswordInput = document.querySelector(".confirmPassword input");
const eyeIcon2 = document.querySelector(".confirmPassword .visible");
var num2 = 1;

eyeIcon2.onclick = () => {
    
    if (num2 === 1) {
        confirmPasswordInput.type = 'text';
        eyeIcon2.style.color = 'black';
        num2--;
    } else {
        confirmPasswordInput.type = 'password';
        eyeIcon2.style.color = '#bfbfbf';
        num2++;
    }
}

// confirm password lock icon color change
const lockIcon2 =  document.querySelector('.confirmPassword .lock-icon');

confirmPasswordInput.addEventListener("keyup", () =>{
    let pattern5 = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
    if(confirmPasswordInput.value === "") {
        lockIcon2.classList.replace("bx-check-circle", "bx-lock");
        return lockIcon2.style.color = "#bfbfbf"
    }   
    if(confirmPasswordInput.value.match(pattern5) && confirmPasswordInput.value == passwordInput.value){
        lockIcon2.classList.replace("bx-lock" , "bx-check-circle");
        return lockIcon2.style.color = "#4bb543"
    }
    lockIcon2.classList.replace("bx-check-circle", "bx-lock");
    return lockIcon2.style.color = "#de0611"
});




const form = document.querySelector('.register form'); // Select the form
const userIdInput = document.querySelector('.register .userId input');
const firstNameInput2 = document.querySelector('.register .firstName input');
const lastNameInput2 = document.querySelector('.register .lastName input');
const emailInput2 = document.querySelector('.register .email input');
const phoneNoInput2 = document.querySelector('.register .phoneNo input');
const passInput = document.querySelector('.register .password input');
const conPassInput = document.querySelector('.register .confirmPassword input');
const agreeCheckedbox1Field = form.querySelector('.register .checkBox.TC');
const agreeCheckedbox1 = agreeCheckedbox1Field.querySelector('.register .checkBox.TC input');
const agreeCheckedbox2Field = form.querySelector('.register .checkBox.PP');
const agreeCheckedbox2 = agreeCheckedbox2Field.querySelector('.register .checkBox.PP input');
const registerbtn = document.querySelector(".register .submitBtn");

var returnValue =true;

//Register in user id validation
const UserIdPattern = /^[a-zA-Z][a-zA-Z0-9_]{5,12}$/; 
function checkUserId() {
    
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

//Register in first name validation
const FNamePattern = /^[a-zA-Z][a-zA-Z]{1,25}$/; 
function checkFirstName() {
    
    if (firstNameInput2.value === "") {
        firstNameInput2.style.borderBottom = "2px solid #ff0000";
        firstNameIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    if (!firstNameInput2.value.match(FNamePattern)) {
        firstNameInput2.style.borderBottom = "2px solid #ff0000";
        firstNameIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    firstNameInput2.style.borderBottom = "2px solid #bfbfbf";
    return returnValue = true;
}

//Register in last name validation
const LNamePattern = /^[a-zA-Z][a-zA-Z]{1,25}$/;
function checkLastName() {
     
    if (lastNameInput2.value === "") {
        lastNameInput2.style.borderBottom = "2px solid #ff0000";
        lastNameIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    if (!lastNameInput2.value.match(LNamePattern)) {
        lastNameInput2.style.borderBottom = "2px solid #ff0000";
        lastNameIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    lastNameInput2.style.borderBottom = "2px solid #bfbfbf";
    return returnValue = true;
}

//Register in email validation
const emailPattern =  /^[a-z0-9._~-]+@[a-z]+\.[a-z]{2,3}$/;
function checkEmail() {
    
    if (emailInput2.value === "") {
        emailInput2.style.borderBottom = "2px solid #ff0000";
        emailIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    if (!emailInput2.value.match(emailPattern)) {
        emailInput2.style.borderBottom = "2px solid #ff0000";
        emailIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    emailInput2.style.borderBottom = "2px solid #bfbfbf";
    return returnValue = true;
}

//Register in phone no validation
const phoneNoPattern = /^[0-9]{10}$/; 
function checkPhoneNo() {
    
    if (phoneNoInput2.value === "") {
        phoneNoInput2.style.borderBottom = "2px solid #ff0000";
        phoneNoIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    if (!phoneNoInput2.value.match(phoneNoPattern)) {
        phoneNoInput2.style.borderBottom = "2px solid #ff0000";
        phoneNoIcon.style.color = "#ff0000";
        return returnValue = false;
    }
    phoneNoInput2.style.borderBottom = "2px solid #bfbfbf";
    return returnValue = true;
}

//Register in password validation
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

//Register in confirm password validation

function checkConfirmPassword() {
    const confirmPasswordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@.#$!%*?&])[A-Za-z\d@.#$!%*?&]{8,16}$/;
    if (conPassInput.value === "") {
        conPassInput.style.borderBottom = "2px solid #ff0000";
        lockIcon2.style.color = "#ff0000";
        return returnValue = false;
    }
    if (!conPassInput.value.match(confirmPasswordPattern)) {
        conPassInput.style.borderBottom = "2px solid #ff0000";
        lockIcon2.style.color = "#ff0000";
        return returnValue = false;
    }
    if (conPassInput.value != passInput.value) {
        conPassInput.style.borderBottom = "2px solid #ff0000";
        lockIcon2.style.color = "#ff0000";
        return returnValue = false;
    }
    conPassInput.style.borderBottom = "2px solid #bfbfbf";
    return returnValue = true;
    
}

// agree checked validation
function agreeCheckedBox1() {
    if (agreeCheckedbox1.checked) {
        agreeCheckedbox1Field.style.color = "#000";
        return returnValue = true;
    } else {
        agreeCheckedbox1Field.style.color = "red";
        return returnValue = false;
    }
}

// agree checked validation
function agreeCheckedBox2() {
    if (agreeCheckedbox2.checked && agreeCheckedbox1.checked && conPassInput.value === passInput.value && 
        phoneNoInput2.value.match(phoneNoPattern) && emailInput2.value.match(emailPattern) && lastNameInput2.value.match(LNamePattern) &&
        firstNameInput2.value.match(FNamePattern) && userIdInput.value.match(UserIdPattern)) {
        agreeCheckedbox2Field.style.color = "#000";
        return returnValue = true;
    } else {
        agreeCheckedbox2Field.style.color = "red";
        return returnValue = false;
    }
}

// calling function on Form Submit
registerbtn.onclick = function registerValidation() {
    checkUserId();
    checkFirstName();
    checkLastName();
    checkEmail();
    checkPhoneNo();
    checkPassword();
    checkConfirmPassword();
    agreeCheckedBox1();
    agreeCheckedBox2();
    
    return returnValue;
}







