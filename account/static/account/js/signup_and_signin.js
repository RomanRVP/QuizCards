
const registration_btn = document.getElementById('sign-up')
const login_btn = document.getElementById('sign-in')


login_btn.onclick = () => {
    document.getElementById('form-registration').style.display = 'none';
    document.getElementById('form-login').style.display = 'block';

}

registration_btn.onclick = () => {
    document.getElementById('form-registration').style.display = 'block';
    document.getElementById('form-login').style.display = 'none';

}
