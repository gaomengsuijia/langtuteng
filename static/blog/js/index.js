
//书籍搜索

function searchbook(){
    var keys = $.trim($("#keys").val());
    if (keys == '') {

        return false
    } else {
        return $("#booksearchform").submit();
    }
}


