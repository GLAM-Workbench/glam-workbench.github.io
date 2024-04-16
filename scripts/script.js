document$.subscribe(function() {
    console.log("Initialize third-party libraries here")

    const delay = ms => new Promise((resolve) => setTimeout(resolve, ms));

    async function getStatus(task_id, masked, retry) {
      retries = 0
      while (true) { // Loop
        const response = await fetch("https://696eq39n0e.execute-api.ap-southeast-2.amazonaws.com/default/trove-newspaper-images-check?article_id=" + task_id + "&masked=" + masked + "&retry=" + retry, {
          method: "GET",
        });
        if (response.status != 202) {
          const data = await response.json();
          console.log("DATA FROM SUCCESS BLOCK", data);
          return data;
        }
        if (retries > 10) {
            return [];
        }
        console.log("polling")
        retries++;
        await delay(5000);
      }
    }

    let btn = document.getElementById('download-image');
    console.log(btn)
    btn.addEventListener('click', async function() {
        output = document.getElementById("images");
        output.innerHTML = "";

        let article_id = document.getElementById("article-id").value;
        if (article_id.startsWith("http")) {
            article_id = article_id.match(/article\/?(\d+)/)[1];
        }
        let masked_chkbox = document.getElementById("mask-image")
        let masked = "False";
        if (masked_chkbox.checked) {
            masked = "True";
        }
        console.log(masked);
        let retry = "False";
        let retry_chkbox = document.getElementById("mask-image")
        if (retry_chkbox.checked) {
            retry = "True";
        }
        console.log(article_id);
        const data = await getStatus(article_id, masked, retry);
        console.log(data);
        
        for (url of data) {
            let para = document.createElement("p");
            let link = document.createElement("a");
            link.textContent = "Download image";
            link.href = url;
            link.download = "";
            let image = document.createElement("img");
            image.src = url;
            para.appendChild(link);
            images.appendChild(para);
            images.appendChild(image);
        }
    })
})
