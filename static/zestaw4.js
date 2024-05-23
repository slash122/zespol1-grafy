function processRandomDigraph() {
    let param1 = document.getElementById("randomDigraphParam1").value;
    let param2 = document.getElementById("randomDigraphParam2").value;

    $.ajax({
        type: "POST",
        url: "/zestaw4/randomdigraph",
        data: {
            param1: param1,
            param2: param2,
        },
        success: function (response) {
            let data = JSON.parse(response);
            let exceptionContanier = document.getElementById("randomDigraphExceptionContainer");

            exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem.
            Wykres grafu jest na dole.` 
            document.getElementById("graphImage").src = "data:image/png;base64," + data.graphImage;
            
            console.log(data);

            document.getElementById("kosaraju").value = data.components;
            document.getElementById("bellmanFord").value = data.distances;
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("randomDigraphExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}
