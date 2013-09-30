$(document).ready(function () {
	$('#openInfo').click(function () {
		blanket_size();
        open('popUpDivInfo');
		open('blanket');
    });
	$('#openDesigner').click(function () {
		blanket_size();
        open('popUpDivDesigner');
		open('blanket');
    });
	$('#joinUsButton').click(function () {
		blanket_size();
		close('popUpDivDesigner');
        open('popUpDivDesignerForm');
		open('blanket');
    });
	$('#openFeatures').click(function () {
		blanket_size();
        open('popUpDivFeatures');
		open('blanket');
    });
	$('.openSignUpOptions').click(function () {
		blanket_size();
        open('popUpSignUpOptions');
		open('blanket');
		close('popUpSignUpWithEmail');
		close('popUpLogIn');
		close('popUpDivFeatures');
    });
	$('#openSignUpWithEmail').click(function () {
		blanket_size();
        open('popUpSignUpWithEmail');
		open('blanket');
		close('popUpSignUpOptions');
    });
	$('.openLogIn').click(function () {
		blanket_size();
        open('popUpLogIn');
		open('blanket');
		close('popUpSignUpOptions');
		close('popUpSignUpWithEmail');
    });
	$('#blanket').click(function () {
        close('popUpDivInfo');
		close('popUpDivDesigner');
		close('popUpDivDesignerForm');
		close('popUpDivFeatures');
		close('popUpSignUpOptions');
		close('popUpSignUpWithEmail');
		close('popUpLogIn');
		close('blanket');
    });
	$('.closeAll').click(function () {
        close('popUpDivInfo');
		close('popUpDivDesigner');
		close('popUpDivDesignerForm');
		close('popUpDivFeatures');
		close('popUpSignUpOptions');
		close('popUpSignUpWithEmail');
		close('popUpLogIn');
		close('blanket');
    });
	
	$(".noAction").click(function(event){
    event.stopPropagation();
  });
});

function open(div_id) {
    var el = document.getElementById(div_id);
	el.style.display = 'block';
}
function close(div_id) {
    var el = document.getElementById(div_id);
	el.style.display = 'none';
}

function blanket_size() {
    if (typeof window.innerWidth != 'undefined') {
        viewportheight = window.innerHeight;
    } else {
        viewportheight = document.documentElement.clientHeight;
    }
    if ((viewportheight > document.body.parentNode.scrollHeight) && (viewportheight > document.body.parentNode.clientHeight)) {
        blanket_height = viewportheight;
    } else {
        if (document.body.parentNode.clientHeight > document.body.parentNode.scrollHeight) {
            blanket_height = document.body.parentNode.clientHeight;
        } else {
            blanket_height = document.body.parentNode.scrollHeight;
        }
    }
    var blanket = document.getElementById('blanket');
    blanket.style.height = blanket_height + 'px';
}

function changeContent(message){
	document.getElementById('shown_text').innerHTML=message;
}
// slider for features
var num = 1
var text = new Array();
text[1] = "Text for feature One"
text[2]= "Text for feature Two"
text[3]= "Text for feature Three"
text[4]= "Text for feature Four"

function slideshowUp()
{
	num = num + 1
	if (num == 5){
		num = 1;}
	document.getElementById('featureShow').innerHTML = text[num];
}

function slideshowBack()
{
	num = num - 1
	if (num == 0)
	{num = 4}
	document.getElementById('featureShow').innerHTML = text[num];
}
// end slider for features
