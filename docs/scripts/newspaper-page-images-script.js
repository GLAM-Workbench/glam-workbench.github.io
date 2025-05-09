
async function getPageID(articleID) {
    url = "https://i6jpz6edq4.execute-api.ap-southeast-2.amazonaws.com/default/get-newspaper-page-id?article_id=" + articleID;
    const response = await fetch(url, { method: "GET"});
    const data = await response.json();
    //const trovePageUrl = data.trovePageUrl;
    //const pageID = trovePageUrl.match(/page(\d+)/)[1];
    const pageID = data.page_id;
    console.log(pageID);
    return pageID;
}

let btn = document.getElementById('download-image');
btn.addEventListener('click', async function() {
    output = document.getElementById("images");
    output.innerHTML = "";
    document.getElementById("status").style.display = 'block';
    let identifier = document.getElementById("page-id").value;
    let level = document.getElementById("level").value;
    let pageID;
    if (identifier.startsWith("http")) {
        if (identifier.indexOf("article") >= 0) {
            document.getElementById("status").style.display = 'none';
            //output.innerHTML = "You need to supply a page url not an article url";
            articleID = identifier.match(/article\/?(\d+)/)[1];
            pageID = await getPageID(articleID);
        } else {
            pageID = identifier.match(/page\/?(\d+)/)[1];
        }
    } else {
        pageID = identifier;
    }
    if (pageID) {
        url = "https://trove.nla.gov.au/ndp/imageservice/nla.news-page" + pageID + "/level" + level;
        document.getElementById("status").style.display = 'none';
        console.log(url);
        let link = document.createElement("a");
        link.textContent = "nla.news-page" + pageID;
        link.download = "nla.news-page" + pageID + ".jpg";
        link.href = url;
        link.target = "_blank";
        let image_list = document.createElement("ul");
        let list_item = document.createElement("li");
        list_item.appendChild(link);
        image_list.appendChild(list_item);
        output.appendChild(image_list);
        let img = document.createElement("img");
        img.src = url;
        output.appendChild(img);
    }
});

let clear = document.getElementById('clear-image-results');
clear.addEventListener('click', async function() {
    document.getElementById("images").innerHTML = "";
    document.getElementById("page-id").value = "";
});
document.getElementById("status").style.display = 'none';
