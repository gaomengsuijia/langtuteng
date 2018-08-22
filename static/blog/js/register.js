
//错误提示
function append_error(info,ty) {
    $('#error').empty();
    $('#error').append("<span class=" + ty + ">" + info + "</span>");
    setTimeout(_delerro(ty),3000)
}
//定时删除提示
function _delerro(ty) {
    return function () {
        var erels = $("." + ty);
        if (erels){
            erels.remove();
        }

    }
}
//检验表单字段

function check_data(username,password,password2,nickname,phone,emailVal) {
    if (username != '' & password !='' & password2 !='' &nickname != ''){
        //判断username
        var regusername = /^[a-zA-Z]{5,10}$/;
        if (!regusername.test(username)){
            append_error("账号为5-10位字母","useerror");
            return false
        }

        //驗證密碼
        var regpassword = /^[0-9a-zA-Z]{6,15}$/;
        if (password != password2){
                append_error("两次密码不相同",'passerror1');
                return false
            }
        if(!regpassword.test(password)){
            append_error("密码为6-15位的字母或数字组合",'passerror');
            return false
        }

        //验证nickname
        var regName = /[^~#^$@%&!*()<>:;'"{}【】  ]/;
        if(nickname == "" || nickname.length>20 || !regName.test(nickname)){
            var errorMsg = " 姓名非空，长度6位以上，不包含特殊字符！";
            append_error("昵称非空，长度20位以下，不包含特殊字符！","useerror");
            return false
        }
        //验证邮箱
        if ($.trim(emailVal)){
            var regEmail = /.+@.+\.[a-zA-Z]{2,4}$/;
            if(emailVal== "" || (emailVal != "" && !regEmail.test(emailVal))){
                append_error("请输入正确的E-Mail地址！",'emailerror');
                return false
            }
        }
        //验证手机号
        if ($.trim(phone)){
            var regphone = /^[1][3,4,5,7,8][0-9]{9}$/;
            if (!regphone.test(phone)){
                append_error("手机号码不正确",'phoneerror');
                return false
            }
        }

        return true
    }else {
        //必填项
        append_error("必填项不能为空","kong");
        return false
    }
}

function go_login() {
    window.location.replace("/account/login");
}

//注册
function res() {
    var username = $('#username').val();
    var password = $('#password').val();
    var password2 = $('#password2').val();
    var nickname = $('#nickname').val();
    var phone = $('#phone').val();
    var emailVal = $('#email').val();
    var token = $('input[name="csrfmiddlewaretoken"]').val();
    if (check_data(username,password,password2,nickname,phone,emailVal)){
        $.ajax({

                type: "post",
                url: "/account/register",
                data: {
                    "username": username,
                    "password": password,
                    "password2": password2,
                    "nickname": nickname,
                    "phone": phone,
                    "email": emailVal,
                    "csrfmiddlewaretoken": token,
                },
                success: function (data) {
                    if (data['code']==20001){
                        layer.msg("恭喜您注册成功,请进行登录");
                        setTimeout(go_login,2000);

                    }else if (data['code']==20002){
                        layer.msg("注册失败，该用户名已被占用")
                    }else if (data['code']==20004){
                        layer.msg("参数不合法");
                    }

                },
                error: function () {
                    layer.msg("注册失败");
                }

    })
        // return $('#registform').submit();
    }


}