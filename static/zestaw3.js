serializedGraph = null;

function processResponse(response) {
    let data = JSON.parse(response)
    let exceptionContanier = document.getElementById("exceptionContainer");

    exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem. </div>`;
    
    let img = data.graphImage;
    document.getElementById("graphImage").src = "data:image/png;base64," + img;

    document.getElementById("distMatrix").textContent = data.distMatrix;

    document.getElementById("centerAndMinmax").value = "Centrum: " + data.center + ", Minmax: " + data.minmax;

    document.getElementById("mstImage").src = "data:image/png;base64," + data.mstImage;

    serializedGraph = data.serializedGraph;
}


function randomWeighted() {
    $.ajax({
        type: "GET",
        url: "/zestaw3/process",
        success: function (response) {
            processResponse(response)
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("exceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });

}


function processDijkstra() {
    let vertexIdx = document.getElementById("vertexIdx").value;

    $.ajax({
        type: "POST",
        url: "/zestaw3/dijkstra",
        data: {
            vertexIdx: vertexIdx,
            serializedGraph: serializedGraph
        },
        success: function (response) {
            data = JSON.parse(response);
            paths = data.paths;
            
            pathString = "";
            paths.forEach(path => {
                pathString += path + "\n";
            });
            
            dijkstraResult = document.getElementById("dijkstraResult");
            dijkstraResult.textContent = pathString;

            document.getElementById("dijkstraExceptionContainer").innerHTML = "";
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("dijkstraExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}