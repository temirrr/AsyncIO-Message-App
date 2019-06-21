$(document).ready(function) {
	var userID = '';
	var sock = {};
	try{
		sock = new WebSocket(`ws://${window.location.host}/ws`)
	} catch {
		sock = new WebSocket(`wss://${window.location.host}/ws`)
	}

	function getOwnMessage(msg, time) {
		return `<div class="message-list">
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
		const showID = $(' #show-id ');
		showID.text(`Your randomly generated id is ${uid}`);
		userID = uid;
	}

	function showMessage(message) {
		const msgBox = $(' #message-list ');
		const msgHTML = ''

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
					msgHTML = getFriendsMessage(id, msg, timeString)
				} else {
					msgHTML = getOwnMessage(msg, timeString);
				};
			} else if (!!msgObj.myID) {
				displayUserID(msgObj.myID);
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
}