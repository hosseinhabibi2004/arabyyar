var checkitem;
var elementParent;
var itemId;

function checkitems(element) {
    if (elementParent != null) {
        elementParent.removeChild(checkitem);
    }
    elementParent = element;
    checkitem = document.createElement("img");
    checkitem.src = "";
    checkitem.className += 'colors_items_checked';
    element.appendChild(checkitem);
    itemId = element.id;
    showdata();
}

var sounds;

function soundplayer() {
    switch (itemId) {
        case 'colors_pink':
            sounds = new Audio("");
            break;
        case 'colors_purple':
            sounds = new Audio("");
            break;
        case 'colors_red':
            sounds = new Audio("");
            break;
        case 'colors_cyan':
            sounds = new Audio("");
            break;
        case 'colors_blue':
            sounds = new Audio("");
            break;
        case 'colors_green':
            sounds = new Audio("");
            break;
        case 'colors_orange':
            sounds = new Audio("");
            break;
        case 'colors_yellow':
            sounds = new Audio("");
            break;
        case 'colors_white':
            sounds = new Audio("");
            break;
        case 'colors_gray':
            sounds = new Audio("");
            break;
        case 'colors_brown':
            sounds = new Audio("");
            break;
        case 'colors_black':
            sounds = new Audio("");
            break;
    }
    sounds.play();
}

function showdata() {
    var showdatatext = document.getElementById('result_content_label_text_color');
    switch (itemId) {
        case 'colors_pink':
            showdatatext.innerHTML = 'وردی';
            break;
        case 'colors_purple':
            showdatatext.innerHTML = 'بنفسجی';
            break;
        case 'colors_red':
            showdatatext.innerHTML = 'احمر';
            break;
        case 'colors_cyan':
            showdatatext.innerHTML = 'سماوی';
            break;
        case 'colors_blue':
            showdatatext.innerHTML = 'ازرق';
            break;
        case 'colors_green':
            showdatatext.innerHTML = 'اخضر';
            break;
        case 'colors_orange':
            showdatatext.innerHTML = 'برتقالی';
            break;
        case 'colors_yellow':
            showdatatext.innerHTML = 'اصفر';
            break;
        case 'colors_white':
            showdatatext.innerHTML = 'ابیض';
            break;
        case 'colors_gray':
            showdatatext.innerHTML = 'رمادی';
            break;
        case 'colors_brown':
            showdatatext.innerHTML = 'بنی';
            break;
        case 'colors_black':
            showdatatext.innerHTML = 'اسود';
            break;
    }
}