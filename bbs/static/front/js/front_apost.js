

$(function () {


    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var titleInput = $('input[name="title"]');
        var boardSelect = $("select[name='board_id']");
        var contentText = $("textarea[id='TextContent']");

        var title = titleInput.val();
        var board_id = boardSelect.val();
        var content = contentText.val();

        lgajax.post({
            'url': '/apost/',
            'data': {
                'title': title,
                'content':content,
                'board_id': board_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    lgalert.alertConfirm({
                        'msg': '恭喜！帖子发表成功！',
                        'cancelText': '回到首页',
                        'confirmText': '再发一篇',
                        'cancelCallback': function () {
                            window.location = '/';
                        },
                        'confirmCallback': function () {
                            contentText.val("");
                            titleInput.val("");
                        }
                    });
                }else{
                    lgalert.alertInfo(data['message']);
                }
            }
        });
    });
});