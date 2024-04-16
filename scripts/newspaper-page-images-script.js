
async function getPageID(article_id) {
    url = "https://api.trove.nla.gov.au/v3/newspaper/" + article_id + "?encoding=json&reclevel=full";
    const response = await fetch(url);
    const data = await response.json();
    const trovePageUrl = data.trovePageUrl;
    const pageID = trovePageUrl.match(/page(\d+)/)[1];
    return pageID;
}

let btn = document.getElementById('download-image');
btn.addEventListener('click', async function() {
    output = document.getElementById("images");
    output.innerHTML = "";
    document.getElementById("status").style.display = 'block';
    let identifier = document.getElementById("page-id").value;
    let pageID;
    if (identifier.startsWith("http")) {
        identifier = identifier.match(/(?:article|page)\/?(\d+)/)[1];
        if (identifier.indexOf("article") >= 0) {
            pageID = await getPageID(identifier);
        } else {
            pageID = identifier;
        }
    } else {
        pageID = identifier;
    }
    url = "https://trove.nla.gov.au/ndp/imageservice/nla.news-page" + pageID + "/level4";
    console.log(url);
    let link = document.createElement("a");
    link.textContent = "nla.news-page" + pageID;
    link.href = url;
    link.target = "_blank";
    let image_list = document.createElement("ul");
    let list_item = document.createElement("li");
    list_item.appendChild(link);
    image_list.appendChild(list_item);
    output.appendChild(image_list);
});
document.getElementById("status").style.display = 'none';
