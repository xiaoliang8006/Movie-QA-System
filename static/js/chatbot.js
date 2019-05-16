var ChatBot = {};

//The server path will be used when sending the chat message to the server.
//todo replace with your server path if needed
ChatBot.SERVER_PATH = window.location.href.slice(0,-1);   //"http://localhost:7010";
ChatBot.userName = "Me";

//This function is called in the end of this file

ChatBot.start = function () {
    $(document).ready(function () {
        ChatBot.bindUserActions();
        ChatBot.write("你好，有什么需要帮助的吗？", "Robot");
        });
};

ChatBot.bindUserActions = function () {
    //Both the "Enter" key and clicking the "Send" button will send the user's message
    $('.chat-input').keypress(function (event) {
        if (event.keyCode == 13) {
            ChatBot.sendMessage();
        }
    });
    $(".chat-send").unbind("click").bind("click", function (e) {
        ChatBot.sendMessage();
    });

};

var chatInput="空";
//The core function of the app, sends the user's line to the server and handling the response
ChatBot.sendMessage = function () {
    var sendBtn = $(".chat-send");
    //Do not allow sending a new message while another is being processed
    if (!sendBtn.is(".loading")) {
        chatInput = $(".chat-input");
        //Only if the user entered a value
        if (chatInput.val()) {
            console.log("$$$",chatInput.val());
            sendBtn.addClass("loading");
            //写入聊天记录
            ChatBot.write(chatInput.val(), ChatBot.userName);
            ChatBot.Ajax();
            chatInput.val("")
            sendBtn.removeClass("loading");
        }
    }
};

ChatBot.Ajax = function(){
  $.ajax({
      //部署到服务器时要改成服务器地址http://服务器IP:5000/search
      url: "http://127.0.0.1:5000/search",
      data: {q: chatInput.val()},
      type: "GET",
      dataType: "json",
      success: function(data) {
          console.log(data);
          ChatBot.write(data["answer"], "Robot");
      },
      failed:function() {
          console.log("请求失败");
      }
  })
};

//写入聊天记录函数
ChatBot.write = function (message, sender, emoji) {
    //console.log(message);
    var chatScreen = $(".chat-screen");
    sender = $("<span />").addClass("sender").addClass(sender).text(sender + ":");
    var msgContent = $("<span />").addClass("msg").text(message);
    var newLine = $("<div />").addClass("msg-row");
    newLine.append(sender).append(msgContent);
    chatScreen.append(newLine);
};


ChatBot.start();
