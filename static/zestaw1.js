function processGraphDataResponse(response, exceptionContainerId) {
    let exceptionContanier = document.getElementById(exceptionContainerId);
    exceptionContanier.innerHTML = "";
    
    let data = JSON.parse(response)
    let repr = data.graphRepresentations;
    let img = data.graphImage;

    document.getElementById("graphAdjacencyMatrix").textContent = repr.adjmatrix;
    document.getElementById("graphAdjacencyList").textContent = repr.adjlist;
    document.getElementById("graphIncedencyMatrix").textContent = repr.incmatrix;

    document.getElementById("graphImage").src = "data:image/png;base64," + img;
}


function submitCodedGraph() {
    let graphCodeType = document.getElementById("graphCodeType").value;
    let graphCode = document.getElementById("graphCode").value;
    
    $.ajax({
        type: "POST",
        url: "/zestaw1/process",
        data: {
            graphCodeType: graphCodeType,
            graphCode: graphCode
        },
        success: function (response) {
            processGraphDataResponse(response, "codeExceptionContainer");
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("codeExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}


function submitRandomGraph() {
    let randomType = document.getElementById("graphRandomType").value;
    let param1 = document.getElementById("firstRandomParam").value;
    let param2 = document.getElementById("secondRandomParam").value;

    $.ajax({
        type: "POST",
        url: "/zestaw1/random",
        data: {
            randomType: randomType,
            param1: param1,
            param2: param2
        },
        success: function (response) {
            processGraphDataResponse(response, "randomExceptionContainer");
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("randomExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}