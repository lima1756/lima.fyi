// Captcha configuration
var mtcaptchaConfig = {
    "sitekey": "MTPublic-3UmToMY2F",
    "widgetSize": "mini",
    "theme": "blackmoon"
};
(function () {
    var mt_service = document.createElement('script'); mt_service.async = true; mt_service.src = 'https://service.mtcaptcha.com/mtcv1/client/mtcaptcha.min.js'; (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(mt_service);
    var mt_service2 = document.createElement('script'); mt_service2.async = true; mt_service2.src = 'https://service2.mtcaptcha.com/mtcv1/client/mtcaptcha2.min.js'; (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(mt_service2);
})();

// Sending email from contact form
const form = document.getElementById("contact_form");
const url = 'https://olbdxzj1ub.execute-api.us-west-1.amazonaws.com/default/limafyi-mail-dev-send';
const messageResponse = document.getElementById('form-result');
const submit = document.getElementById('btn-send-form');

function post(url, body, callback) {
    var req = new XMLHttpRequest();
    req.open("POST", url, true);
    req.setRequestHeader("Content-Type", "application/json");
    req.addEventListener("load", function () {
        if (req.status === 200) {
            callback(null, JSON.parse(req.responseText));
        } else {
            callback(req);
        }
    });
    req.send(JSON.stringify(body));
}

function success() {
    messageResponse.innerHTML = '<b> Your message was sent, thanks! </b>';
    messageResponse.classList.add('info');
}

function error(err) {
    const response = JSON.parse(err.response).result;
    messageResponse.innerHTML = '<b>' + response + '</b>';
    messageResponse.classList.add('danger');
}

form.addEventListener('submit', function (e) {
    e.preventDefault();
    submit.innerHTML = '<i class="fas fa-spinner fa-pulse"></i>';
    submit.disabled = true;

    const payload = {
        name: form.name.value,
        email: form.email.value,
        content: form.message.value,
        solution: form["frc-captcha-solution"].value
    };
    post(url, payload, function (err, res) {
        form.name.value = '';
        form.email.value = '';
        form.message.value = '';
        friendlyChallenge.autoWidget.reset();
        messageResponse.classList.remove('info');
        messageResponse.classList.remove('danger');
        submit.innerHTML = 'Send!';
        submit.disabled = false;
        submit.blur();
        if (err) { return error(err); }
        success();
    })
})