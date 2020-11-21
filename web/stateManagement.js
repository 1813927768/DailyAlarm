const origin =
  "http://" + (location.host || "${1:localhost}").split(":")[0] + ":8081";

function getState() {
  console.log("get state from config.py, print here");
  axios.get(origin).then((res) => {});
}

function setSwitchState() {
  const params = new URLSearchParams();

  const switch_state = document.querySelector("#switch").checked;
  if (switch_state == false) {
    // disable alert settings
    document.querySelector("#wechat-alert").disabled = true;
    document.querySelector("#mail-alert").disabled = true;
  } else {
    document.querySelector("#wechat-alert").disabled = false;
    document.querySelector("#mail-alert").disabled = false;
  }

  params.append("switch", switch_state ? "True" : "False");
  axios.post(origin, params).then((res) => console.log(res));
}

function setAlertState(name) {
  const params = new URLSearchParams();
  const state = document.querySelector(`#${name}-alert`).checked;
  params.append(`${name}_alert`, state ? "True" : "False");
  axios.post(origin, params).then((res) => console.log(res));
}
