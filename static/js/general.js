$(document).ready( function() {
	let userID = '';
	let sock = {};
	try{
		sock = new WebSocket(`ws://${window.location.host}/wsgeneral`)
	} catch {
		sock = new WebSocket(`wss://${window.location.host}/wsgeneral`)
	}

	function getOwnMessage(msg, time) {
		return `<div class="message-list-item">
    	<div class="row">
    		<div class="col-sm-6"></div>
	    	<div class="col-sm-5 text-right own-message-box">
	    		${msg}
	    	</div>
	    	<div class="col-sm-1 text-center">
	    		${time}
	    	</div>
	    </div>
    </div>`;
	}

	function getFriendsMessage(friendid, msg, time) {
		return `<div class="message-list-item">
    	<div class="row">
	    	<div class="col-sm-1 text-center">
	    		${friendid}, ${time}
	    	</div>
	    	<div class="col-sm-5 text-left message-box">
	    		${msg}
	    	</div>
	    	<div class="col-sm-6"></div>
	    </div>
    </div>`;
	}

	function getGeneralMessage(msg) {
		return `<div class="row message-list-item"><div class="col-sm-2"></div><div class="col-sm-8 text-center">${msg}</div><div class="col-sm-2"></div></div>`;
	}

	function displayUserID(uid) {
		userID = uid;
		const showID = $(' #show-id ');
		showID.html(`Your randomly generated id: <span id='uid'>${uid}</span>`);
	}

	function showMessage(message) {
		const msgBox = $(' #message-list ');
		let msgHTML = ''

		const date = new Date();
		const hours = date.getHours();
		const minutes = date.getMinutes();
		const timeString = `${hours}:${minutes}`;		

		/*No need for, I think
		const day = date.getDate();
		const month = date.getMonth(); //January is 0
		const dateString = `${month}/${day}`; */

		try{
			const msgObj = JSON.parse(message)
			if (!!msgObj.user && msgObj.msg) {
				const id = msgObj.user;
				const msg = msgObj.msg;

				if (id === userID) {
					msgHTML = getOwnMessage(msg, timeString)
				} else {
					msgHTML = getFriendsMessage(id, msg, timeString);
				};
			} else if (!!msgObj.myID) {
				//SOME DIRTY CODE HERE
				console.log(userID);
				displayUserID(msgObj.myID);
				console.log(userID);
				return;
			} else {
				msgHTML = getGeneralMessage(message);
			}
		} catch {
			msgHTML = getGeneralMessage(message);
		}

		msgBox.append(msgHTML);
		msgBox.scrollTop( msgBox.height() );
	}

	//on Enter-key or Send-button click
	function sendMessage() {
		const msgBox = $(' #message ');
		const msg = msgBox.val();
		if (userID === '') {
			alert('You did not receive ID due to system error');
		} else if (!msg) {
			return;
		}else {
			sock.send(msg);
			msgBox.val('').focus();
		}
	}

    sock.onopen = function(){
        showMessage('Connection to server started');
    };


    $(' #submit ').on('click', function() {
        sendMessage();
    });

    $('#message').keyup(function(e){
        if(e.keyCode == 13){
            sendMessage();
        }
    });

    sock.onmessage = function(event) {
        showMessage(event.data);
    };

    sock.onclose = function(event){
        if(event.wasClean){
            sock.send('Clean connection end');
        }else{
            sock.send('Connection broken');
        }
    };

    sock.onerror = function(error){
        sock.send(error);
    };

    $(' #group-general ').on('click', function() {
    	window.location.href='/';
    })

    $(' #group-interns ').on('click', function() {
    	window.location.href='/interns';
    })

    $(' #message ').focus();
});