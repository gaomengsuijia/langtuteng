
//注册
function res() {
    var username = $('#username').val();
    var password = $('#password').val();
    var password2 = $('#password').val();
    var nickname = $('#nickname').val();
    var phone = $('#phone').val();
    var emailVal = $('#email').val();
    if (username != '' & password !='' & password2 !='' &nickname != ''){
        //判断username
        var regusername = /^[a-zA-Z]{5,10}$/;
        if (!regusername.test(username)){
            var errorMsg = "账号为5-10位字母";
            $('#error').text(errorMsg);
        }

        //驗證密碼


        //验证nickname
        var regName = /[~#^$@%&!*()<>:;'"{}【】  ]/;
        if(nickname == "" || nickname.length < 6 || !regName.test(nickname)){
            var errorMsg = " 姓名非空，长度6位以上，不包含特殊字符！";
            //class='msg onError' 中间的空格是层叠样式的格式
            $parent.append("<span class='msg onError'>" + errorMsg + "</span>");
        }
        else{
            var okMsg=" 输入正确";
            $parent.find(".high").remove();
            $parent.append("<span class='msg onSuccess'>" + okMsg + "</span>");
        }


        //验证邮箱
        var regEmail = /.+@.+\.[a-zA-Z]{2,4}$/;
        if(emailVal== "" || (emailVal != "" && !regEmail.test(emailVal))){
            var errorMsg = " 请输入正确的E-Mail住址！";
            $parent.append("<span class='msg onError'>" + errorMsg + "</span>");
        }
        else{
            var okMsg=" 输入正确";
            $parent.find(".high").remove();
            $parent.append("<span class='msg onSuccess'>" + okMsg + "</span>");
        }
        return $('#registform').submit();
    }else {
        //必填项
        var errorMsg = "必填项不能为空";
        $('#error').text(errorMsg);
    }

}