function clearForm() {
  console.log("Clear Form Button Clicked");
}

function predict() {
  console.log("Predict Button Clicked");

  const ba = document.getElementById("bikeAge").value;
  const ct = document.getElementById("city").value;
  const on = document.getElementById("owner").value;
  const pw = document.getElementById("power").value;
  const bn = document.getElementById("brand").value;
  const op = document.getElementById("originalPrice").value;
  const km = document.getElementById("kms_driven").value;

  console.log("Bike Age : " + ba);
  console.log("City : " + ct);
  console.log("OwnerShip : " + on);
  console.log("Power : " + pw);
  console.log("Brand : " + bn);
  console.log("Original Price : " + op);
  console.log("KMs Driven : " + km);

  const data = {
    Bike_Age: ba,
    city: ct,
    owner: on,
    power: pw,
    brand: bn,
    "Original Price": op,
    kms_driven: km,
  };

  console.log("Data : ", data);

  document.getElementById("bikeAge").value = "";
  document.getElementById("city").value = "";
  document.getElementById("owner").value = "";
  document.getElementById("power").value = "";
  document.getElementById("brand").value = "";
  document.getElementById("originalPrice").value = "";
  document.getElementById("kms_driven").value = "";
}
