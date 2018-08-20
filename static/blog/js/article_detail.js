//点赞

function post_like(ar_id){
     $.ajax({

                type: "post",
                url: "/blog/thumb",
                data: {
                    "article_id": ar_id
                },
                success: function (data) {
                    if (data['code']=="20001"){
                        layer.msg("点赞成功");
                        $('.thumb_total').text(data['total_thumb']);

                    }else if (data['code']=="20002"){
                        layer.msg("请勿重复点赞")
                    }

                },
                error: function () {
                    layer.msg("点赞失败");
                }

    })
}


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

function check_comment(comment) {
    var comm = Trim(comment,'g');
    if (comm == ""){
        layer.msg("请输入内容");
        return false
    }else {
        return true
    }
}

//动态添加评论
function append_comment() {
    //清空testarea
    $("#reply_body").val("");
}

//提交评论
function post_comment() {
    var comment = $("#reply_body").val();
    var article_id = $("input[name='articleid']").val();
    var token = $("input[name='csrfmiddlewaretoken']").val();
    if (check_comment(comment)){
        $.ajax({

                type: "post",
                url: "/blog/comment",
                data: {
                    "replybody":comment,
                    "articleid": article_id,
                    "csrfmiddlewaretoken":token
                },
                success: function (data) {
                    if (data['code']=="20001"){
                        layer.msg("评论成功");
                        append_comment();

                    }else if (data['code']=="20002"){
                        layer.msg("请勿重复点赞")
                    }

                },
                error: function () {
                    layer.msg("评论失败");
                }

        })
    }

}
