function copyToClipboard(text){
    var dummy = document.createElement("input");
    document.body.appendChild(dummy);
	dummy.setAttribute('value', text);
    dummy.select();
    document.execCommand("copy");
	document.body.removeChild(dummy);}

copyToClipboard (document.getElementById("type-text").innerText.replace(/(\r\n\t|\n|\r\t)/gm,"") || document.getElementById("type-text").TextContent.replace(/(\r\n\t|\n|\r\t)/gm,""))

//window.open("https://mem.meditab.com/v4/index.php?file=med_typing_tests")
//window.alert("JS Executed")

/* alert ("page loaded")

if(document.readyState === "complete") {
  alert("Already loaded!")
  function copyToClipboard(text){
    var dummy = document.createElement("input");
    document.body.appendChild(dummy);
	dummy.setAttribute('value', text);
    dummy.select();
    document.execCommand("copy");
	document.body.removeChild(dummy);}
	
	
}
else {
	alert ("Page not loaded")
	document.getElementById("type-text").addEventListener("DOMContentLoaded", function copyToClipboard(text){
    var dummy = document.createElement("input");
    document.body.appendChild(dummy);
	dummy.setAttribute('value', text);
    dummy.select();
    document.execCommand("copy");
	document.body.removeChild(dummy);}, false)
} */
/* alert ("Page not loaded")
	document.getElementById("type-text").addEventListener("DOMContentLoaded", function copyToClipboard(text){
    var dummy = document.createElement("input");
    document.body.appendChild(dummy);
	dummy.setAttribute('value', text);
    dummy.select();
    document.execCommand("copy");
	document.body.removeChild(dummy);}
	
copyToClipboard (document.getElementById("type-text").innerText.replace(/(\r\n\t|\n|\r\t)/gm,"") || document.getElementById("type-text").TextContent.replace(/(\r\n\t|\n|\r\t)/gm,""))
alert ("content copied")

window.alert("JS Executed") */
