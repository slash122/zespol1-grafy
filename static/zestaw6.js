function processPageRankResponse(response) {
    let data = JSON.parse(response);
    let exceptionContanier = document.getElementById("exceptionContainer");
    
    exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem. </div>`;

    document.getElementById("pageRankCustom").textContent = data.prCustom
    document.getElementById("pageRankRandomWalk").textContent = data.prRW

    document.getElementById("graphImage").src = "data:image/png;base64," + data.img;
}


function submitCodedGraph() {
    let graphCode = document.getElementById("graphCode").value;
        
    $.ajax({
        type: "POST",
        url: "/zestaw6/pagerank",
        data: {
            graphCode: graphCode
        },
        success: function (response) {
            processPageRankResponse(response);
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("codeExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}


function processShortestPathResponse(response) {
    let data = JSON.parse(response);

    document.getElementById("graphHamilton").src = "data:image/png;base64," + data.img1;
    document.getElementById("graphSimulatedAnnealing").src = "data:image/png;base64," + data.img2;
    
    document.getElementById("hamiltonLength").textContent = data.dist1;
    document.getElementById("annealingLength").textContent = data.dist2;
}

function submitShortestPath() {
    $.ajax({
        type: "GET",
        url: "/zestaw6/shortest",
        success: function (response) {
            processShortestPathResponse(response);
        },
        error: function (response) {
            console.log(JSON.parse(response.responseText).exceptionMsg);
        }
    })
}