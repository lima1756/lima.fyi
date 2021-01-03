'use strict';

const domain = process.env.DOMAIN;
const captchaApiKey = process.env.CAPTCHA_API_KEY;
const captchaSiteKey = process.env.CAPTHA_SITE_KEY;
const mailto = process.env.EMAIL;
const mailgun = require('mailgun-js')({ apiKey: process.env.MAILGUN_API_KEY, domain: domain });
const axios = require('axios');

class SendingError extends Error {}

function generateResponse(code, payload) {
  return {
    statusCode: code,
    headers: {
      "access-control-allow-methods": "OPTIONS, POST",
      'Access-Control-Allow-Origin': "*",
      'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
      'Access-Control-Allow-Credentials': true,
      "content-type": "application/json"
    },
    body: `{"result": "${payload.message}"}`
  }
}

async function validateBody(body) {
  const input = JSON.parse(body)
  if (!(input.email && input.name && input.content && input.solution)) {
    throw new SendingError('Missing parameters! Make sure you\'ve filled all fields and clicked on the "solve captcha button"')
  }
  try {
    const response = await axios.post(`https://friendlycaptcha.com/api/v1/siteverify`, {
      solution: input.solution,
      secret: captchaApiKey,
      sitekey: captchaSiteKey
    });
    if(response.data.success || response.status != 200) {
      return input
    }
    let error = ''
    switch(response.data.errors[0]){
      case 'solution_invalid': 
        error = "There was a problem with the captcha, please reload the page and try again.";
        break;
      case 'solution_timeout_or_duplicate': 
        error = "The captcha has expired, please try again.";
        break;
    }
    throw new SendingError(error);
  } 
  catch (err) {
    if (err instanceof SendingError) {
      throw err
    }
    console.info("THERE WAS AN ERROR WITH FRIENDLY CAPTCHA, HOPING FOR THE BEST AND SENDING EMAIL");
    console.error(err);
    return input;
  }
}

function sendEmail({email, name, content}) {
  const data = {
    from: `${name} <contact@${domain}>`,
    to: mailto,
    subject: `New message from: ${name} <${email}> through lima.fyi`,
    text: content
  };
  return mailgun.messages().send(data);
}

module.exports.send = async (event) => {
  try {
    if(!event.body){
      //There is a bug with cors, it is ignoring my configuration in API Gateway, so it failed here because the OPTION request didn't have a body, hacky solution for this
      return generateResponse(200, {message:""})  
    }
    const input = await validateBody(event.body)
    const data = await sendEmail(input)
    return generateResponse(200, data)
  } catch (err) {
    console.error(err);
    if (err instanceof SendingError) {
      return generateResponse(400, err)
    } else {
      return generateResponse(500, new Error("There was a problem, please refresh the page and try again in a moment :)"))
    }
  }
}