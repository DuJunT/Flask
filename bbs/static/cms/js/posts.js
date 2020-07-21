

$(function () {
    $(".highlight-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var post_id = tr.attr("data-id");
        var highlight = parseInt(tr.attr("data-highlight"));
        // alert(highlight)
        var url = "";
        if(highlight){
            url = "/cms/chpost/";
        }else{
            url = "/cms/hpost/";
        }
        lgajax.post({
            'url': url,
            'data': {
                'post_id': post_id
            },
            'success': function (data) {
                if(data['code'] == 200){
                    lgalert.alertSuccessToast('操作成功！');
                    setTimeout(function () {
                        window.location.reload();
                    },500);
                }else{
                    zlalert.alertInfo(data['message']);
                }
            }
        });
    });
});


$(function () {
    $(".btn-xs").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var post_id = tr.attr("data-id");
        lgalert.alertConfirm({
            "msg":"您确定要删除这篇帖子吗？",
            'confirmCallback': function () {
                lgajax.post({
                    'url': '/cms/dpost/',
                    'data':{
                        'post_id': post_id
                    },
                    'success': function (data) {
                        if(data['code'] == 200){
                            window.location.reload();
                        }else{
                            lgalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        });


    });
});