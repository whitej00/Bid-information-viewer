'use strict';

Util.onReady(function () {
    var hocrProofreader = new HocrProofreader({
        layoutContainer: 'layout-container',
        editorContainer: 'editor-container'
    });

    document.getElementById('toggle-layout-image').addEventListener('click', function () {
        hocrProofreader.toggleLayoutImage();
    });

    document.getElementById('zoom-page-full').addEventListener('click', function () {
        hocrProofreader.setZoom('page-full');
    });

    document.getElementById('zoom-page-width').addEventListener('click', function () {
        hocrProofreader.setZoom('page-width');
    });

    document.getElementById('zoom-original').addEventListener('click', function () {
        hocrProofreader.setZoom('original');
    });

    document.getElementById('button-save').addEventListener('click', function () {
        var hocr = hocrProofreader.getHocr();

        var request = new XMLHttpRequest();
        request.open('POST', 'save.php');
        request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=utf-8');
        request.send('hocr=' + encodeURIComponent(hocr));
    });

    var hocrBaseUrl = 'https://kplc.co.ke/img/full/erJcsN0MybZM_ADDENDUM NO. 1 - TENDER FOR SUPPLY OF DISTRIBUTION TRANSFORMERS.pdf/';
    var hocrUrl = hocrBaseUrl + 'demo.hocr';

    Util.get(hocrUrl, function (err, hocr) {
        if (err) return Util.handleError(err);

        hocrProofreader.setHocr(hocr, hocrBaseUrl);
    });
});
