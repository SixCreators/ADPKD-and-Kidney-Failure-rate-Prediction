const error_icon1 = document.querySelector('.serumCreatinine i');
const error_icon2 = document.querySelector('.age i');
const error_icon3 = document.querySelector('.genders i');
const error_icon4 = document.querySelector('.races i');
const input1 = document.querySelector('.serumCreatinine input');
const input2 = document.querySelector('.age input');
const Gender = document.querySelector('.genders .gender');
const Race = document.querySelector('.races .race');
const submitBtn = document.querySelector ('.btn-submit')


var returnValue =true;

submitBtn.onclick =  function Validation() {
    checked();
    return returnValue;
}


function  checked(){
    // box 1
    if (input1.value === '' || input1.value === '0') {
        error_icon1.style.display = 'block';
        returnValue =false;
    } else {
        returnValue =true;
        error_icon1.style.display = 'none';
    }
    // box 2
    if(input2.value === '' || input2.value === '0') {
        error_icon2.style.display = 'block';
        returnValue =false;
    } else {
        error_icon2.style.display = 'none';
        returnValue =true;
    }

    // choose here 1
    if (Gender.value === '0') {
        error_icon3.style.display = 'block';
        returnValue =false;
    } else {
        error_icon3.style.display = 'none';
        returnValue =true;
    }
    // choose here 2
    if (Race.value === '0') {
        error_icon4.style.display = 'block';
        returnValue =false;
    } else {
        error_icon4.style.display = 'none';
        returnValue =true;
    }

}

