window.onload = function() {
  // チャットボックスを取得
  const chatBox = document.getElementById('chat-box');
  
  // チャットボックスのスクロールを一番下に設定
  chatBox.scrollTop = chatBox.scrollHeight;

  // Ctrl + Enterでフォームを送信
  const form = document.getElementById('chat-form');
  const textarea = document.getElementById('user-input');

  textarea.addEventListener('keydown', function(event) {
      // Ctrl + Enterが押された場合
      if (event.ctrlKey && event.key === 'Enter') {
          event.preventDefault();  // デフォルトの動作（改行など）を防止
          form.submit();  // フォームを送信
      }
  });

  // LINEぽいUIにする
  document.getElementById("chat-form").addEventListener("submit", function (e) {
    var userInput = document.getElementById("user-input");
    var chatBox = document.getElementById('chat-box');
    const text = userInput.value;
    // 仮表示 div 作成
    var newDiv = document.createElement('div');
    newDiv.className = 'user-message';
    newDiv.innerHTML = text.replace(/\n/g, "<br>");
    // div を追加し下にスクロール
    chatBox.appendChild(newDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
  });
}
