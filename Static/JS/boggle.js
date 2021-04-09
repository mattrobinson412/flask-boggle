$("input").on("submit", async function(e){
    e.preventDefault();
    const guess = $("#guessSubmission").val();
    $.ajax({
        type: "POST",
        url: "/",
        data: {
            word: guess
        },
        dataType: "json",
        success: function (response) {
            console.log(guess);
        }
    });

})