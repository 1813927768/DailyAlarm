const origin =
  "http://" + (location.host || "${1:localhost}").split(":")[0] + ":8081";

function str2bool(str) {
  if (typeof str == "string") {
    return str !== "false";
  }
  console.log("not a string");
  return str;
}

function getState() {
  axios.get(origin + "/config.json").then((res) => {
    // document.querySelector("#switch").checked
    Object.keys(res.data).forEach((item) => {
      const key = item.split("_")[0];
      if (item.indexOf("_") > 0) {
        document.querySelector(`#${key}-alert`).checked = str2bool(
          res.data[item]
        );
      } else {
        document.querySelector(`#switch`).checked = str2bool(res.data[item]);
      }
    });
  });
}

function setSwitchState() {
  const params = new URLSearchParams();

  const switch_state = document.querySelector("#switch").checked;
  if (switch_state === false) {
    // disable alert settings
    document.querySelector("#wechat-alert").disabled = true;
    document.querySelector("#mail-alert").disabled = true;
  } else {
    document.querySelector("#wechat-alert").disabled = false;
    document.querySelector("#mail-alert").disabled = false;
  }

  params.append("switch", switch_state);
  axios.post(origin, params).then((res) => console.log(res));
}

function setAlertState(name) {
  const params = new URLSearchParams();
  const state = document.querySelector(`#${name}-alert`).checked;
  params.append(`${name}_alert`, state);
  axios.post(origin, params).then((res) => console.log(res));
}
