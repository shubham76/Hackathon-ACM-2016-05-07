function validateForm(){
	var retval=true;
	var fname = register_form.fname.value;
	var ck_name = /^[A-Za-z]{2,20}$/;
	if (fname=="") {
		document.getElementById('fnr').innerHTML = "Firstname field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(fname))
    	{
		document.getElementById('fnr').innerHTML = "Firstname should contain only alphabets";
		retval=false;
    	}	
	var lname = register_form.lname.value;
	if (lname=="") {
		document.getElementById('lnr').innerHTML = "Lastname field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_name.test(lname))
    	{
		document.getElementById('lnr').innerHTML = "Lastname should contain only alphabets";
		retval=false;
    	}
	var email = register_form.email.value;
	var ck_email= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if (email=="") {
		document.getElementById('emr').innerHTML = "Email field should not be empty"; 
        	retval=false;
    	}
    	else if(!ck_email.test(email))
    	{
		document.getElementById('emr').innerHTML = "Lastname should contain only alphabets";
		retval=false;
    	}
	var mob1 = register_form.telephone1.value;
	var mob2 = register_form.telephone2.value;
	var ck_mob = /^[0-9]{10,10}$/
	if (mob1=="") {
		document.getElementById('mbr1').innerHTML = "Mobile number required"; 
        	retval=false;
    	}
    	else if(!ck_mob.test(mob1))
    	{
		document.getElementById('mbr1').innerHTML = "10 digit number required";
		retval=false;
    	}
	if(mob2!="" && !ck_mob.test(mob2))
    	{
		document.getElementById('mbr2').innerHTML = "10 digit number required";
		retval=false;
    	}
	var roll_no = register_form.roll_no.value;
	var ck_rn1= /^[B][T][0-9]{2}[A-Z]{3}[0-9]{3}$/
	var ck_rn2= /^[b][t][0-9]{2}[a-z]{3}[0-9]{3}$/
	if (roll_no=="") {
		document.getElementById('rnr').innerHTML = "Roll Number required"; 
        	retval=false;
    	}
    	else if( !(ck_rn1.test(roll_no)) && !(ck_rn2.test(roll_no)))
    	{
		document.getElementById('rnr').innerHTML = "Roll Number not valid";
		retval=false;
    	}
	var clg_id = register_form.clg_id.value;
	var ck_cid= /^[0-9]{5}$/
	if (clg_id=="") {
		document.getElementById('cidr').innerHTML = "college id number required"; 
        	retval=false;
    	}
    	else if( !ck_cid.test(clg_id))
    	{
		document.getElementById('cidr').innerHTML = "college id not valid";
		retval=false;
    	}
	var branch = register_form.branch.value;
	if (branch=="sb") {
		document.getElementById('br').innerHTML = "select a branch"; 
        	retval=false;
    	}
	var pass1 = register_form.password1.value;
	var pass2 = register_form.password2.value;
	if(pass1.length < 8)
	{
		document.getElementById('passr1').innerHTML = "minimum 8 characters required";
		retval=false;
	}
	if(pass1 != pass2)
	{
		document.getElementById('passr2').innerHTML = "passwords don't match";
		retval=false;
	}
	return retval;	
}
