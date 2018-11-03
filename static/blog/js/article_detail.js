//点赞

function post_like(ar_id){
     $.ajax({

                type: "post",
                url: "/thumb",
                data: {
                    "article_id": ar_id
                },
                success: function (data) {
                    if (data['code']=="20001"){
                        layer.msg("点赞成功");
                        $('.thumb_total').text(data['total_thumb']);

                    }else if (data['code']=="20002"){
                        layer.msg("请勿重复点赞")
                    }else if (data['code']=="20004"){
                        window.location.replace("/account/login")
                    }

                },
                error: function () {
                    layer.msg("点赞失败");
                }

    })
}

//清除所有的空格
function Trim(str,is_global)
  {
   var result;
   result = str.replace(/(^\s+)|(\s+$)/g,"");
   if(is_global.toLowerCase()=="g")
   {
    result = result.replace(/\s/g,"");
    }
   return result;
}

//检查字段
function check_comment(comment) {
    var comm = Trim(comment,'g');
    if (comm == ""){
        layer.msg("请输入内容");
        return false
    }else if (comm.length>200) {
        layer.msg("不能超过200个字符");
        return false
    }else {
        return true
    }
}

//动态添加评论
function append_comment(comment_html) {
    //清空testarea
    $("#reply_body").val("");
    $("#reply1").append(comment_html);
}

//提交评论
function post_comment() {
    var comment = $("#reply_body").val();
    var article_id = $("input[name='articleid']").val();
    var token = $("input[name='csrfmiddlewaretoken']").val();
    if (check_comment(comment)){
        $.ajax({

                type: "post",
                url: "/comment",
                data: {
                    "replybody":comment,
                    "articleid": article_id,
                    "csrfmiddlewaretoken":token
                },
                success: function (data) {
                    if (data['code']=="20001"){
                        layer.msg("评论成功");
                        append_comment(data['comment_html']);

                    }else if (data['code']=="20002"){
                        layer.msg("请勿重复点赞")
                    }else if(data['code']=="20004"){
                        window.location.replace("/account/login");
                    }

                },
                error: function () {
                    layer.msg("评论失败");
                }

        })
    }

}
