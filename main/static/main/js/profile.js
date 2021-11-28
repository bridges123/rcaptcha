$(function () {
    let capKeyCode = 'KeyN'
    $('.stat-table').css('margin', '-130px 0px 0px 86px')

//    if (document.getElementById('capKey').value === "") {
//		document.getElementById('capKey').value = capKeyCode
//	}

    $('.switch-btn').click(function (e, changeState) {
        if (changeState === undefined) {
            $(this).toggleClass('switch-on');
        }
        if ($(this).hasClass('switch-on')) {
            $(this).trigger('on.switch');
        } else {
            $(this).trigger('off.switch');
        }
    })

    $('.switch-btn').on('on.switch', function(){
        delay = 100
        minusRange = 210
        $('.del').val('1')
    })

    $('.switch-btn').on('off.switch', function(){
        delay = 15
        minusRange = 95
        $('.del').val('0')
    })

    $('body').keydown(function(data) {
        let key = data.key;
        let keyCode = data.originalEvent.code;
        if (document.getElementById('capKey').focused) {
                capKeyCode = data.originalEvent.code
                document.getElementById('capKey').value = capKeyCode
                return false
        }
    })

});