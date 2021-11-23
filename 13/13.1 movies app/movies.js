$("#addMovieButton").on("click", function(e){
    const movieTitle = $("#title").val();
    const movieRating = $("#rating").val();
    $('#movies-container').append(`<div>${movieTitle}, ${movieRating}/5 Stars <button class='removeMe'>Remove</button></div>`);
})

$("#movies-container").on("click", function(e) {
    if(e.target.classList.contains("removeMe")){
        $(e.target).parent().remove();
    }
})