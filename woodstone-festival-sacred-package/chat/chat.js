const messagesDiv = document.getElementById('messages');
const input = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
  const text = input.value.trim();
  if (!text) return;
  
  const userMsg = document.createElement('div');
  userMsg.className = 'message user';
  userMsg.textContent = `You: ${text}`;
  messagesDiv.appendChild(userMsg);
  
  const aiMsg = document.createElement('div');
  aiMsg.className = 'message ai';
  aiMsg.textContent = `AI Pulse: Your presence is acknowledged 🌿`;
  messagesDiv.appendChild(aiMsg);

  input.value = '';
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
});