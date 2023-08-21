'use strict';
const otherUserID = document.getElementById('other-user-id').textContent.trim();
const currentUserUsername = document
	.getElementById('current-username')
	.textContent.trim()
	.replace(/\"/g, '');

const webSocket = new WebSocket(
	`${document.body.dataset.scheme === 'http' ? 'ws' : 'wss'}://${document.body.dataset.host
	}/ws/chat/${otherUserID}/`
);

console.log(
	`${document.body.dataset.scheme === 'http' ? 'ws' : 'wss'}://${document.body.dataset.host
	}/ws/chat/${otherUserID}/`
);

webSocket.addEventListener('open', (event) => {
	//   document.getElementById(
	//     'message-wrapper'
	//   ).innerHTML += `<div class="alert alert-success alert-dismissible fade show" role="alert">
	//                Conversation has started.
	//               <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
	//             </div>`;
});

webSocket.addEventListener('message', (event) => {
	const data = JSON.parse(event.data);
	console.log(data);
	const chatBody = document.getElementById('chat-body');
	let newMessage = '';

	if (data.senderUsername === currentUserUsername) {
		newMessage = `
		<li class="odd chat-item">
			<div class="chat-content">
				<div class="box bg-light-success">
					<h5 class="font-medium">Me</h5>
					<p class="font-light mb-0">
					<pre>${data.message}</pre>
					</p>
					<div class="chat-time">Just now</div>
				</div>
			</div>
			<div class="chat-img"><img src="/static/assets/images/users/1.jpg" alt="user"></div>
		</li>`;
	} else {
		newMessage = `
		<li class="chat-item">
		<div class="chat-img"><img src="/static/assets/images/users/2.jpg" alt="user"></div>
			<div class="chat-content">
				<div class="box bg-light-success">
					<h5 class="font-medium">${data.senderUsername}</h5>
					<p class="font-light mb-0">
					<pre>${data.message}</pre>
					</p>
					<div class="chat-time">Just now</div>
				</div>
			</div>
		</li>`;
	}
	chatBody.innerHTML += newMessage;
	console.log(`SenderUser: ${data.senderUsername}`);
	console.log(`currentUserUsername: ${currentUserUsername}`);
	console.log(data.senderUsername === currentUserUsername);
});

webSocket.addEventListener('error', (event) => {
	document.getElementById(
		'message-wrapper'
	).innerHTML += `<div class="alert alert-danger alert-dismissible fade show" role="alert">
          An error occurred.
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>`;
});

webSocket.addEventListener('close', (event) => {
	document.getElementById(
		'message-wrapper'
	).innerHTML += `<div class="alert alert-warning alert-dismissible fade show" role="alert">
      Chat ended.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>`;
});

document
	.getElementById('send-message-btn')
	.addEventListener('click', (event) => {
		event.preventDefault();
		console.log('Here');
		const messageInput = document.getElementById('message-body');
		if (messageInput.value.length > 1) {
			webSocket.send(
				JSON.stringify({
					message: messageInput.value,
					senderUsername: currentUserUsername,
				})
			);
			messageInput.value = '';
		}
	});

	function scrollToBottom() {
		const objDiv = document.querySelector('#message-wrapper');
		objDiv.scrollTop = objDiv.scrollHeight;
	}
    console.log("1");
	scrollToBottom();
    console.log("2");
window.addEventListener('DOMContentLoaded', () => {
	setTimeout(function () {
		document.querySelectorAll('.alert').forEach((element) => {
			element.querySelectorAll('.btn-close').forEach((el) => {
				el.click();
			});
		});
	}, 2000);
});