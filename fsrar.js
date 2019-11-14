var system = require('system');
var page = require('webpage').create();
var fs = require('fs');

var amc = system.args[1];
var clientKey = system.args[2];
var startTime = Date.now();

var url = 'https://check1.fsrar.ru/MobileApi/'; // URL
var captchaImageFN = 'captcha.png'; // Имя файла с капчей (изображение png)
var resultFN = 'check1_fsrar.html'; // Имя файла для сохранения полученных данных по накладной
var createURL = 'https://api.anti-captcha.com/createTask';
var resultURL = 'https://api.anti-captcha.com/getTaskResult';

page.settings.userAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0';   // От имени какого браузера будем работать
page.settings.resourceTimeout = 60000;                                                                      // Максимальное время ожидания в миллисекундах

page.open(url, function (status) {
    if (status === 'success') {
        checkReadyState();                  // Проверка статуса загрузки документа
    } else {
        console.log(url + " didn't load");
        phantom.exit();
    }
});

page.onConsoleMessage = function (msg) { // Для отладки
    console.log(msg);
};

page.onError = function (msg, trace) {
    result = date2string(Date.now()) + "\tWebpage JS error:" + "\t" + msg;
    console.log('ERROR:' + result);
};

phantom.onError = function (msg) {
    result = date2string(Date.now()) + "\tPhantomJS error:" + "\t" + msg;
    console.log('ERROR:' + result);
};

page.onLoadFinished = function () {
    // console.log('onLoadFinished');
};

page.onResourceReceived = function (response) {
    //console.log(JSON.stringify(response));
};

function onPageReady() {
    console.log('Page loaded - Checking TTN-'+ system.args[1] + ' ' + system.args[2]);
    // console.log(page.content);
    // Заполняем все поля кроме капчи
    page.evaluate(function (valAmc) {
        document.getElementById("tab-title4").click();
        document.getElementById("bk").value = valAmc;
    }, amc);

    // Получаем координаты капчи
    var CaptchaRect = page.evaluate(function () {
        var box = document.getElementById("SampleCaptcha_CaptchaImage").getBoundingClientRect();
        console.log(box.top);
        console.log(box.left);
        console.log(box.width);
        console.log(box.height);
        console.log(pageYOffset);
        console.log(pageXOffset);
        return {
            top: box.top  + pageYOffset,
            //bottom: box.bottom,
            left: box.left + pageXOffset,
            //right: box.right,
            width: box.width ,
            height: box.height
        };
    });

    // Делаем рендеринг капчи
    page.clipRect = {
        top: CaptchaRect.top - 28 ,
        //bottom: CaptchaRect.bottom,
        left: CaptchaRect.left,
        //right: CaptchaRect.right,
        width: CaptchaRect.width,
        height: CaptchaRect.height
    };

    //page.clipRect = {
    //    top: 664.59375,
    //    left: 8,
    //    width: 250,
    //    height: 50
    //};
    page.render(captchaImageFN, {format: 'png'});
    var base64 = page.renderBase64('PNG');
    var data_w = {
        clientKey: clientKey, //ключ для антикапчи
        task: {
            type: "ImageToTextTask",
            body: base64
        }
    };

    page.includeJs('https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', function () {
        console.log("Start solving Captcha");
        var t = page.evaluate(function (data, url) {
            var res = $.ajax({
                async: false,
                type: 'POST',
                url: url,
                dataType: 'json',
                contentType: 'application/json',
                data: JSON.stringify(data),
                complete: function (x) {
                    return x;
                },
                error: function (x) {
                    console.log("Ошибка создания task: " + x);
                    phantom.exit();
                },
            });
            var x = JSON.parse(JSON.stringify(res.responseText));
            var task = JSON.parse(x).taskId;
            return task;
        }, data_w, createURL);
        console.log("Task ID = " + t);

        setTimeout(function (){}, 5000);
        var i = 1;
        var timer = setInterval(function () {
            var captcha = page.evaluate(function (data, url) {
                var res = $.ajax({
                    async: false,
                    type: 'POST',
                    url: url,
                    dataType: 'json',
                    contentType: 'application/json',
                    data: JSON.stringify(data),
                    complete: function (x) {
                        return x;
                    },
                    error: function (x) {
                        console.log("Ошибка получения статуса task: " + x);
                        phantom.exit();
                    },
                });
                var x = JSON.parse(JSON.stringify(res.responseText));
                var task = JSON.parse(x);
                var sol = JSON.parse(JSON.stringify(task.solution));
                console.log("Task status: " + task.status + ". Solution: " + sol.text);
                return sol.text;
            }, {clientKey: clientKey /*ключ для антикапчи*/, taskId: t}, resultURL);
            if (captcha) {
                ++i;
                page.evaluate(function (captcha) {
                    //console.log(captcha);
                    document.querySelector("input[name='CaptchaCode']").value = captcha;
                    document.querySelector("input[id='get1']").click();
                }, captcha);
                startTime = Date.now();
                checkReadyResponse();
                clearInterval(timer);
            } else {
                //console.log("Task is not solved yet");
                ++i;
            }
            if (i >= 15) {
                var wfile = fs.write(resultFN, "Не удалось решить капчу", 'w');
                phantom.exit();
            }
        }, 2000);
    });
}

// Проверка статуса загрузки сайта
function checkReadyState() {
    setTimeout(function () {
        var readyState = page.evaluate(function () {
            return document.readyState;
        });
        //console.log('readyState = ' + readyState);
        if (readyState === "complete") {
            onPageReady();
        } else {
            checkReadyState();
        }
    }, 1000);
}

// Проверка статуса получения ответа
function checkReadyResponse() {
    setTimeout(function () {
        var readyState = page.evaluate(function () {
            return document.readyState;
        });
        //console.log('readyState = ' + readyState);
        if (readyState === "complete") {
            if (page.evaluate(function () {
                return document.getElementById("content").innerHTML;
            }) === "") {
                if (Date.now() - startTime > 60000) {
                    console.log("Content didn't load");
                    phantom.exit();
                }
                console.log('No content yet');
                checkReadyResponse();
            } else {
                //page.clipRect = {};
                //page.render("00.png");
                var res = page.evaluate(function () {
                    return document.getElementById("content").outerHTML;
                });
                var wfile = fs.write(resultFN, res, 'w');
                phantom.exit();
            }
        } else {
            checkReadyResponse();
        }
    }, 1000);
}
