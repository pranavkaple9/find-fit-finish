var time_limit=30*60*1000;
if(sessionStorage.getItem('status')=='1'){
time_limit=Number.parseInt(sessionStorage.getItem('time'),10);
}
var now=Date.parse(new Date());
var deadline=new Date(now+time_limit);

function time_remaining(endtime){
	var t = Date.parse(endtime) - Date.parse(new Date());
	var seconds = Math.floor( (t/1000) % 60 );
	var minutes = Math.floor( (t/1000/60) % 60 );
	var hours = Math.floor( (t/(1000*60*60)) % 24 );
	var days = Math.floor( t/(1000*60*60*24) );
	return {'total':t, 'days':days, 'hours':hours, 'minutes':minutes, 'seconds':seconds};
}
function run_clock(id,endtime){
	var clock = document.getElementById(id);
	function update_clock(){
		var t = time_remaining(endtime);
        if (t.minutes<10 && t.seconds<10){
		    clock.innerHTML = '0'+t.minutes+':'+'0'+t.seconds;
        }
        else if(t.minutes<10 && t.seconds>=10){
            clock.innerHTML = '0'+t.minutes+':'+t.seconds;
        }
        else if(t.minutes>=10 && t.seconds<10){
            clock.innerHTML = t.minutes+':'+'0'+t.seconds;
        }
        else{
            clock.innerHTML = t.minutes+':'+t.seconds;
        }
            
            
		value=t.minutes*60+t.seconds
		value=value*1000
		sessionStorage.setItem('time',value);
		sessionStorage.setItem('status',1);
		if(t.total<=0){ clearInterval(timeinterval); }
		if(t.minutes==0 && t.seconds==0)
		{
			
			var id=document.getElementById("hidden").value;
			document.getElementById("hidden").value=document.getElementById("cell2Input").value;
			var id1=document.getElementById("hidden").value;
            document.getElementById("hidden2").value="Finish Test";
			document.forms["form1"].submit();
            
		}
	}
	update_clock(); // run function once at first to avoid delay
	var timeinterval = setInterval(update_clock,1000);
}
run_clock('timer',deadline);
