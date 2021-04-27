var xmlHttp;

function interact(inText, lemmatizer, classifier) {

	if (inText.length==0) { 
  		document.getElementById("txtHint").innerHTML="";
  		return;
  	}
	xmlHttp=GetXmlHttpObject()
	if (xmlHttp==null) {
  		// alert ("Browser does not support HTTP Request");
  		return;
  	} 
	var url="http://localhost:5000/resp";
	url=url+"?q="+inText;
	url=url+"&lem="+lemmatizer;
	url=url+"&class="+classifier;
	url=url+"&sid="+Math.random();
	// alert(url);
	xmlHttp.onreadystatechange=stateChanged; 
	xmlHttp.open("POST",url,true);
	xmlHttp.send(null);

} 

function stateChanged() { 
	if (xmlHttp.readyState==4 || xmlHttp.readyState=="complete") { 
 		document.getElementById("exampleFormControlTextarea2").innerHTML=xmlHttp.responseText 
 	} 
}
	
function GetXmlHttpObject() {
	var xmlHttp=null;
	try {
 	// Firefox, Opera 8.0+, Safari
 		xmlHttp=new XMLHttpRequest();
 	} catch (e) {
 		// Internet Explorer
 		try {
  			xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
  		} catch (e) {
  			xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
  		}
 	}
	return xmlHttp;
}