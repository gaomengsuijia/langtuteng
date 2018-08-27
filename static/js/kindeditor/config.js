
KindEditor.ready(function (k) {
    window.editor = k.create('textarea[name=body]',{  //这个id选择器是你要添加富文本编辑器的元素的id，按F12查找
        resizeType:1,
        allowPreviewEmoticons : false,
        allowImageRemote : false,
        uploadJson : '/admin/upload/kindeditor',  //这是上传图片处理的url
        width:'800px',
        height:'400px',

    });
})