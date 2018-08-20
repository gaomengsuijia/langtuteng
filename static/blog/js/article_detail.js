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
