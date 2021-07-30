$(function() {
    // Displays menu when button is clicked on
    $(".nav-link").click(function() {
        // 500 ms animation speed
        $(".dropdown").slideToggle(500);
    });
});