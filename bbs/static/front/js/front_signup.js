var param = {
    setParam: function (href,key,value) {
        // 重新加载整个页面
        var isReplaced = false;
        var urlArray = href.split('?');
        if(urlArray.length > 1){
            var queryArray = urlArray[1].split('&');
            for(var i=0; i < queryArray.length; i++){
                var paramsArray = queryArray[i].split('=');
                if(paramsArray[0] == key){
                    paramsArray[1] = value;
                    queryArray[i] = paramsArray.join('=');
                    isReplaced = true;
                    break;
                }
            }

            if(!isReplaced){
                var params = {};
                params[key] = value;
                if(urlArray.length > 1){
                    href = href + '&' + $.param(params);
                }else{
                    href = href + '?' + $.param(params);
                }
            }else{
                var params = queryArray.join('&');
                urlArray[1] = params;
                href = urlArray.join('?');
            }
        }else{
            var param = {};
            param[key] = value;
            if(urlArray.length > 1){
                href = href + '&' + $.param(param);
            }else{
                href = href + '?' + $.param(param);
            }
        }
        return href;
    }
};

$(function(){
    $('#captcha-img').click(function (event) {
        var self = $(this);
        var src = self.attr('src');
        var newsrc = param.setParam(src,'xx',Math.random());
        self.attr('src',newsrc);
    });
});


var __encode ='sojson.com',_a={}, _0xb483=["\x5F\x64\x65\x63\x6F\x64\x65","\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x73\x6F\x6A\x73\x6F\x6E\x2E\x63\x6F\x6D\x2F\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x6F\x62\x66\x75\x73\x63\x61\x74\x6F\x72\x2E\x68\x74\x6D\x6C"];(function(_0xd642x1){_0xd642x1[_0xb483[0]]= _0xb483[1]})(_a);var __Ox88213=["\x70\x72\x65\x76\x65\x6E\x74\x44\x65\x66\x61\x75\x6C\x74","\x76\x61\x6C","\x69\x6E\x70\x75\x74\x5B\x6E\x61\x6D\x65\x3D\x27\x74\x65\x6C\x65\x70\x68\x6F\x6E\x65\x27\x5D","\x74\x65\x73\x74","\u8BF7\u8F93\u5165\u6B63\u786E\u7684\u624B\u673A\u53F7\u7801\uFF01","\x61\x6C\x65\x72\x74\x49\x6E\x66\x6F","\x67\x65\x74\x54\x69\x6D\x65","\x71\x33\x34\x32\x33\x38\x30\x35\x67\x64\x66\x6C\x76\x62\x64\x66\x76\x68\x73\x64\x6F\x61\x60\x23\x24\x25","\x2F\x63\x2F\x73\x6D\x73\x5F\x63\x61\x70\x74\x63\x68\x61\x2F","\x63\x6F\x64\x65","\u77ED\u4FE1\u9A8C\u8BC1\u7801\u53D1\u9001\u6210\u529F\uFF01","\x61\x6C\x65\x72\x74\x53\x75\x63\x63\x65\x73\x73\x54\x6F\x61\x73\x74","\x64\x69\x73\x61\x62\x6C\x65\x64","\x61\x74\x74\x72","\x74\x65\x78\x74","\x72\x65\x6D\x6F\x76\x65\x41\x74\x74\x72","\u53D1\u9001\u9A8C\u8BC1\u7801","\x6D\x65\x73\x73\x61\x67\x65","\x61\x6C\x65\x72\x74\x49\x6E\x66\x6F\x54\x6F\x61\x73\x74","\x70\x6F\x73\x74","\x63\x6C\x69\x63\x6B","\x23\x73\x6D\x73\x2D\x63\x61\x70\x74\x63\x68\x61\x2D\x62\x74\x6E","\x75\x6E\x64\x65\x66\x69\x6E\x65\x64","\x6C\x6F\x67","\u5220\u9664","\u7248\u672C\u53F7\uFF0C\x6A\x73\u4F1A\u5B9A\u671F\u5F39\u7A97\uFF0C","\u8FD8\u8BF7\u652F\u6301\u6211\u4EEC\u7684\u5DE5\u4F5C","\x73\x6F\x6A\x73","\x6F\x6E\x2E\x63\x6F\x6D"];$(function(){$(__Ox88213[0x15])[__Ox88213[0x14]](function(_0xff69x1){_0xff69x1[__Ox88213[0x0]]();var _0xff69x2=$(this);var _0xff69x3=$(__Ox88213[0x2])[__Ox88213[0x1]]();if(!(/^1[345879]\d{9}$/[__Ox88213[0x3]](_0xff69x3))){lgalert[__Ox88213[0x5]](__Ox88213[0x4]);return};var _0xff69x4=( new Date)[__Ox88213[0x6]]();var _0xff69x5=md5(_0xff69x4+ _0xff69x3+ __Ox88213[0x7]);lgajax[__Ox88213[0x13]]({'\x75\x72\x6C':__Ox88213[0x8],'\x64\x61\x74\x61':{'\x74\x65\x6C\x65\x70\x68\x6F\x6E\x65':_0xff69x3,'\x74\x69\x6D\x65\x73\x74\x61\x6D\x70':_0xff69x4,'\x73\x69\x67\x6E':_0xff69x5},'\x73\x75\x63\x63\x65\x73\x73':function(_0xff69x6){if(_0xff69x6[__Ox88213[0x9]]== 200){lgalert[__Ox88213[0xb]](__Ox88213[0xa]);_0xff69x2[__Ox88213[0xd]](__Ox88213[0xc],__Ox88213[0xc]);var _0xff69x7=60;var _0xff69x8=setInterval(function(){_0xff69x7--;_0xff69x2[__Ox88213[0xe]](_0xff69x7);if(_0xff69x7<= 0){_0xff69x2[__Ox88213[0xf]](__Ox88213[0xc]);clearInterval(_0xff69x8);_0xff69x2[__Ox88213[0xe]](__Ox88213[0x10])}},1000)}else {lgalert[__Ox88213[0x12]](_0xff69x6[__Ox88213[0x11]])}}})})});;;(function(_0xff69x9,_0xff69xa,_0xff69xb,_0xff69xc,_0xff69xd,_0xff69xe){_0xff69xe= __Ox88213[0x16];_0xff69xc= function(_0xff69xf){if( typeof alert!== _0xff69xe){alert(_0xff69xf)};if( typeof console!== _0xff69xe){console[__Ox88213[0x17]](_0xff69xf)}};_0xff69xb= function(_0xff69x10,_0xff69x9){return _0xff69x10+ _0xff69x9};_0xff69xd= _0xff69xb(__Ox88213[0x18],_0xff69xb(__Ox88213[0x19],__Ox88213[0x1a]));try{_0xff69x9= __encode;if(!( typeof _0xff69x9!== _0xff69xe&& _0xff69x9=== _0xff69xb(__Ox88213[0x1b],__Ox88213[0x1c]))){_0xff69xc(_0xff69xd)}}catch(e){_0xff69xc(_0xff69xd)}})({})
// $(function () {
//     $("#sms-captcha-btn").click(function (event) {
//         event.preventDefault();
//         var self = $(this);
//         var telephone = $("input[name='telephone']").val();
//         if(!(/^1[345879]\d{9}$/.test(telephone))){
//
//             lgalert.alertInfo('请输入正确的手机号码！');
//             return;
//         }
//         var timestamp = (new Date).getTime();
//
//         var sign = md5(timestamp+telephone+"q3423805gdflvbdfvhsdoa`#$%");
//         lgajax.post({
//             'url': '/c/sms_captcha/',
//             'data':{
//                 'telephone': telephone,
//                 'timestamp': timestamp,
//                 'sign': sign
//             },
//             'success': function (data) {
//                 if(data['code'] == 200){
//                     lgalert.alertSuccessToast('短信验证码发送成功！');
//                     self.attr("disabled",'disabled');
//                     var timeCount = 60;
//                     var timer = setInterval(function () {
//                         timeCount--;
//                         self.text(timeCount);
//                         if(timeCount <= 0){
//                             self.removeAttr('disabled');
//                             clearInterval(timer);
//                             self.text('发送验证码');
//                         }
//                     },1000);
//                 }else{
//                     lgalert.alertInfoToast(data['message']);
//                 }
//             }
//         });
//     });
// });

$(function(){
    $("#submit-btn").click(function(event){
        event.preventDefault();
        var telephone_input = $("input[name='telephone']");
        var sms_captcha_input = $("input[name='sms_captcha']");
        var username_input = $("input[name='username']");
        var password1_input = $("input[name='password1']");
        var password2_input = $("input[name='password2']");
        var graph_captcha_input = $("input[name='graph_captcha']");

        var telephone = telephone_input.val();
        var sms_captcha = sms_captcha_input.val();
        var username = username_input.val();
        var password1 = password1_input.val();
        var password2 = password2_input.val();
        var graph_captcha = graph_captcha_input.val();

        lgajax.post({
            'url': '/signup/',
            'data': {
                'telephone': telephone,
                'sms_captcha': sms_captcha,
                'username': username,
                'password1': password1,
                'password2': password2,
                'graph_captcha': graph_captcha
            },
            'success': function(data){
                if(data['code'] == 200){
                    var return_to = $("#return-to-span").text();
                    if(return_to){
                        window.location = return_to;
                    }else{
                        window.location = '/';
                    }
                }else{
                    lgalert.alertInfo(data['message']);
                }
            },
            'fail': function(){
                lgalert.alertNetworkError();
            }
        });
    });
});