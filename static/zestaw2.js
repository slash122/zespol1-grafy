function processGraphicSeq() {
    let graphSequence = document.getElementById("graphicSequenceInput").value;

    $.ajax({
        type: "POST",
        url: "/zestaw2/graphicseq",
        data: {
            graphSequence: graphSequence,
        },
        success: function (response) {
            let data = JSON.parse(response)
            let exceptionContanier = document.getElementById("sequenceExceptionContainer");

            exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Ciąg graficzny. 
            Wykres grafu jest na dole.</div>`;
            let img = data.graphImage;

            document.getElementById("graphImage").src = "data:image/png;base64," + img;
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("sequenceExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}