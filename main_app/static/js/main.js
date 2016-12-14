$(document).ready(function(){

    $('#login-click-btn').click(function(){
        $('.page-filter').css("display", "block");
        $('.login-form-bg').css("display", "block");
    });

    $('#close-btn, #login-form-btn, .page-filter').click(function(){
        $('.page-filter').css("display", "none");
        $('.login-form-bg').css("display", "none");
    });

    $('.minimize').click(function(){
        $('.minimize').css('display', 'none');
        $('.maximize').css('display', 'block');
        $('#minimize-body').css('display', 'none');
        $('.guide-jumbotron').addClass('minimized');
        $('.guide-panel').addClass('minimized-panel');
    });

    $('.maximize, .minimized-panel').click(function() {    
        $('.minimize').css('display', 'block');
        $('.maximize').css('display', 'none');    
        $('#minimize-body').css("display", "block");
        $('.guide-jumbotron').removeClass('minimized');
        $('.guide-panel').removeClass('minimized-panel');
    });

    $('.plus, .new-project').click(function(){
        $('.page-filter').css("display", "block");
        $('.new-project-form-bg').css("display", "block");
    });

    $('.form-heading>h2,span, .page-filter, #close-btn').click(function(){
        $('.page-filter').css("display", "none");
        $('.new-project-form-bg').css("display", "none");
    });

    $('.note, .new-note').click(function(){
        $('.page-filter').css("display", "block");
        $('.new-note-form-bg').css("display", "block");
    });    

    $('#close-btn, .page-filter').click(function(){
        $('.page-filter').css("display", "none");
        $('.new-note-form-bg').css("display", "none");
    });

    $('#delete-note, #delete-project').click(function(){
        $('.page-filter').css("display", "block");
        $('.delete-project-form-bg').css("display", "block");
    });    

    $('#close-btn, #nvm, .page-filter').click(function(){
        $('.page-filter').css("display", "none");
        $('.delete-project-form-bg').css("display", "none");
    });

    $('#add-comment').click(function(){
        $('.comment-form').css("display", "block");        
    });

    $('#update-note').click(function(){
        $('.update-note-form').css("display", "block");        
    });

    $('#introduction-trash').click(function(){
        $('.to-remove').remove();
    });


    $(":file").filestyle({input: false});

});

