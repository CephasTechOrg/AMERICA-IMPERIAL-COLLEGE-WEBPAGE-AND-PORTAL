// gather form fields across steps and all file inputs
async function collectAndSend() {
  const fields = [
    "firstName", "lastName", "email", "phone", "essay"
  ];
  const formData = new FormData();

  // map HTML ids to form names expected by backend
  formData.append("first_name", document.getElementById("firstName").value);
  formData.append("last_name", document.getElementById("lastName").value);
  formData.append("email", document.getElementById("email").value);
  formData.append("phone", document.getElementById("phone").value);
  formData.append("essay", document.getElementById("essay").value);

  // append files, check existence
  const fileInputs = ["transcript","certificates","idDocument","recommendation","otherDocuments"];
  fileInputs.forEach(id => {
    const el = document.getElementById(id);
    if (el && el.files && el.files.length) {
      for (let i = 0; i < el.files.length; i++) {
        formData.append("files", el.files[i], el.files[i].name);
      }
    }
  });

  // send request
  const res = await fetch("http://localhost:8000/applications/", {
    method: "POST",
    body: formData
  });

  const result = await res.json();
  if (result.status === "success") {
    // show confirmation section
    document.getElementById("confirmation").classList.add("active");
    // optionally hide form
    // show application id to student
    console.log("application id", result.application_id);
  } else {
    alert("Submission failed");
  }
}

document.getElementById("submit-application").addEventListener("click", function(e){
  e.preventDefault();
  // validate checkboxes
  const agree = document.getElementById("agreeTerms").checked && document.getElementById("agreePolicy").checked;
  if (!agree) {
    alert("Please agree to the terms and policy");
    return;
  }
  collectAndSend();
});
