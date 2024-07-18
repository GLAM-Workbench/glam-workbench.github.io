let clear = document.getElementById('clear-all');
clear.addEventListener('click', function() {
    document.getElementById("datasette-url").innerHTML = "";
    document.getElementById("github-url").value = "";
    document.getElementById("about-url").value = "";
    document.getElementById("fts-cols").value = "";
    document.getElementById("drop-cols").value = "";
});

let button = document.getElementById('create-url');
button.addEventListener('click', function() {
    let gh_url = document.getElementById("github-url").value;
    let fts_cols = document.getElementById("fts-cols").value;
    let drop_cols = document.getElementById("drop-cols").value;
    let about_url = document.getElementById("about-url").value;
    let url_div = document.getElementById("datasette-url")
    url_div.innerHTML = "";
    if (gh_url) {
        let url = "https://glam-workbench.net/datasette-lite/?csv=" + encodeURIComponent(gh_url) + "&install=datasette-homepage-table";
        if (fts_cols) {
            url += "&fts=" + encodeURIComponent(fts_cols);
        }
        if (drop_cols) {
            url += "&drop=" + encodeURIComponent(drop_cols);
        }
        if (about_url) {
            url += "&about=" + encodeURIComponent(about_url);
        }
        let link = document.createElement("a");
        link.textContent = url;
        link.href = url;
        link.target = "_blank";
        url_div.innerHTML = "Click or copy this url: "
        url_div.appendChild(link);
    };

});