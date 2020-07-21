
$(function () {
    var ue = UE.getEditor('editor',{
        'serverUrl':'/ueditor/upload',
        toolbars:[
            ['fullscreen', 'source', 'undo', 'redo'],
            ['bold', 'italic', 'underline', 'fontborder', 'strikethrough', 'superscript', 'subscript', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall', 'cleardoc']
        ]
    });
    window.ue = ue;
})

$(function () {
    $("#comment-btn").click(function (event) {
        event.preventDefault();

        var content = window.ue.getContent()
        var post_id = $("#post-content").attr("data-id");
        lgajax.post({
            'url': '/acomment/',
            'data':{
                'content': content,
                'post_id': post_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    window.location.reload();
                }else{
                    lgalert.alertInfo(data['message']);
                }
            }
        });
//        }
    });
});