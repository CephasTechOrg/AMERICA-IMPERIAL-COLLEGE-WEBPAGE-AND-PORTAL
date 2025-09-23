async function loadApplications() {
  const res = await fetch("http://localhost:8000/applications_list/");
  const apps = await res.json();
  const tbody = document.getElementById("appsBody");
  tbody.innerHTML = "";
  apps.forEach(a => {
    const files = a.uploaded_files ? a.uploaded_files.join(", ") : "";
    const row = `
      <tr>
        <td>${a.id}</td>
        <td>${a.first_name} ${a.last_name}</td>
        <td>${a.email}</td>
        <td>${a.phone}</td>
        <td>${a.status}</td>
        <td>${files}</td>
      </tr>
    `;
    tbody.insertAdjacentHTML("beforeend", row);
  });
}

window.onload = loadApplications;
