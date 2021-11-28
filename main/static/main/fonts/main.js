$(function () {
    let strIdList
    let timer
    let msg = []
    let result
    let ourCap = []
    let mindex
    let mistakes = 0
    let delay = 30
    $('body').keydown(function(data) {
        const key = data.key;
        if ((key === 'Backspace') || (key === 'Escape')) {
            $('.img').hide()
            mistakes = 0
            ourCap = []
        }else {
            const keyId = data.keyCode;
            const hidden = $('.img').is(':hidden')
            if (hidden) {
                if (key === 'n') {
                    $('#code').text('')
                    $('#code').css('left', '47.5%')
                    mistakes = 0
                    ourCap = []
                    let id = Math.floor(Math.random() * 90000 + 10000);
                    let strId = code(id)
                    strIdList = id.toString().split('')
                    $('#image').attr("src", 'img/captches/' + strId + '.jpeg')
                    $('.img').show()
                    timer = new Date().getTime()
                    
                }
            } else if ((keyId >= 48) && (keyId <= 57)) {
                setTimeout(() => {
                    let len = 0
                    $('#code').text((index, text) => {
                        len = text.length
                        return text
                    })
                    if (len <= 4) {
                        if (key === strIdList[len]) {
                            $('#code').text((index, text) => {
                                text = text + key
                                return text
                            })
                            ourCap.push(key)
                            if (len === 1) {
                                $('#code').css('left', '45.5%')
                            } else if (len === 2) {
                                $('#code').css('left', '43.5%')
                            } else if (len === 3) {
                                $('#code').css('left', '41.4%')
                            } else if (len === 4) {
                                $('#code').css('left', '39.3%')
                                result = new Date().getTime()
                                result = (result - timer - 5000) / 1000
                                // setTimeout(() => {
                                //     $('.img').hide()
                                // }, 30)
                                $('.img').hide()
                                if (mistakes === 1) {
                                    ourCap[mindex] = ''
                                }
                                const cap = strIdList.join('')
                                msg.push("[" + new Date().toLocaleTimeString() + "] Верно | Капча ("
                                     + ourCap.join('') + "/" + cap + ") введена за " + result)
                            }
                        } else {
                            mistakes += 1
                            if (mistakes === 1) {
                                mindex = ourCap.length
                                ourCap.push(key)
                                if ($('#notf').is(':hidden')) {
                                    setTimeout(() => {
                                        $('#notf').show()
                                    }, 100)
                                    setTimeout(() => {
                                        $('#notf').hide()
                                    },2500)
                                }
                            }else if (mistakes === 2) {
                                result = new Date().getTime()
                                result = (result - timer - 5000) / 1000
                                // setTimeout(() => {
                                //     $('.img').hide()
                                // }, 35)
                                $('.img').hide()
                                const cap = strIdList.join('')
                                ourCap.push(key)
                                msg.push("[" + new Date().toLocaleTimeString() + "] Неверно | Капча ("
                                    + ourCap.join('') + "/" + cap + ") введена за " + result)
                                mistakes = 0
                            }
                        }
                    }
                }, delay)
            }
        }
    });
    setInterval(function()
    {
        let res = ""
        let cnt = 0
        let n = ""

        for (let txt of msg)
        {
            cnt = cnt + 1
            res = res + "<br>" + txt
        }
        if (cnt < 9) {
            cnt = 9 - cnt
            for (let i = 0; i < cnt; i++)
            {
                n = n + "<br>"
            }
        } else if (cnt > 9) {
            msg.shift()
            res = ""
            cnt = 0
            for (let txt of msg)
            {
                cnt = cnt + 1
                res = res + "<br>" + txt
            }
        }

        res = n + res

        let s = document.getElementById('text')
        s.innerHTML = res

        let tt = document.getElementById('text')
        tt.scrollTop = tt.scrollHeight
    }, 100);
});


function div(val, by){
    return (val - val % by) / by;
}


function code(prev) {
    let res = ''
    while (prev > 0) {
        res += (prev % 4).toString()
        prev = div(prev, 4)
    }
    let a = res.split('')
    let r = a.reverse()
    const re = r.join('')
    return re
}


// function decode(prev) {
//     prev = Number(prev)
//     let cnt = 0
//     let res = 0
//     while (prev > 0) {
//         res += (prev % 10) * (4 ** cnt)
//         cnt += 1
//         prev = div(prev, 10)
//     }
//     return res
// }