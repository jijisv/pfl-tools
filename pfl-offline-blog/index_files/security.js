function isSecurity(chkFlag){
	if (chkFlag == "true") return true;
	if (chkFlag == "false") return false;
	return false;
}

function changeH1Class(){
	document.getElementById("blockMessage").className = "security";
}

function writeHeader(){
	if(isSecurity(securityFlag)){
		document.write("Security risk blocked for your protection");
		changeH1Class();
	}
	else{
		document.write("Content blocked by your organization");
	}
}

function writeReason(){
	if(isSecurity(securityFlag)){
		document.write("Sites in this category may pose a security threat to network resources or private information, and are blocked by your organization.");
	}
}

function writeWarning(){
	if(isSecurity(securityFlag)){
		document.write('<span class="warning">Not Recommended</span>');
	}
}

function writeWarning1(){
	if(isSecurity(securityFlag)){
		document.write('This action is not recommended.')
	}
}

function openPopup() {
	parent.document.getElementById('light').innerHTML = document.getElementById('light').innerHTML;
	parent.document.getElementById('light').style.display='block';
	parent.document.getElementById('fade').style.display='block';
	return false;
}


function closePopup() {
	document.getElementById('light').style.display='none';
	document.getElementById('fade').style.display='none';	
	return false;
}

function encode() {
	var _user = document.getElementById("ws-credentials-user");
	var _pass = document.getElementById("ws-credentials-pass");
	var _hddn = document.getElementById("ws-credentials");	
	_hddn.value = "Basic-" + Base64.encode(_user.value + ":" + _pass.value);
	_user.value = '';
	_pass.value = '';
	return true;
}

