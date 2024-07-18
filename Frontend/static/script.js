document.addEventListener('DOMContentLoaded', function () {
    let selectedLanguage = null;  // Variable to store the selected language

    document.getElementById('sendBtn').addEventListener('click', async function () {
        let chatInput = document.getElementById('chatInput');
        let chatDisplay = document.getElementById('chatDisplay');

        if (chatInput.value.trim() !== "") {
            let userMessage = document.createElement('div');
            userMessage.className = 'chat-message user';
            userMessage.innerHTML = "<span class='emoji' style='font-size: 30px;'>🙋🏻‍♀️</span> " + chatInput.value;
            chatDisplay.appendChild(userMessage);

            if (selectedLanguage) {
                let botMessage = document.createElement('div');
                botMessage.className = 'chat-message bot';

                let botResponse = await getBotResponse(chatInput.value, selectedLanguage);
                botMessage.innerHTML = "<span class='emoji' style='font-size: 30px;'>🦜</span> " + botResponse;
                chatDisplay.appendChild(botMessage);

                chatDisplay.scrollTop = chatDisplay.scrollHeight;
            } else {
                let botMessage = document.createElement('div');
                botMessage.className = 'chat-message bot';
                botMessage.innerHTML = "<span class='emoji' style='font-size: 30px;'>🦜</span> " + "Please Select a language";
                chatDisplay.appendChild(botMessage);

                chatDisplay.scrollTop = chatDisplay.scrollHeight;
            }

            chatInput.value = "";
        }
    });

    async function getBotResponse(message, language) {
        try {
            let response = await fetch('/generate-response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message, language: language })
            });
            let data = await response.json();
            return data.bot_response;
        } catch (error) {
            console.error('Error:', error);
            return "Server down";
        }
    }

    // Toggle language dropdown
    document.querySelector('.language').addEventListener('click', function () {
        document.getElementById('languageDropdown').classList.toggle('show');
    });

    // Close the dropdown if the user clicks outside of it
    window.onclick = function (event) {
        if (!event.target.matches('.language')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    };

    // Add event listeners to the language options
    document.querySelectorAll('#languageDropdown a').forEach(function (element) {
        element.addEventListener('click', function () {
            selectedLanguage = this.getAttribute('data-lang');
            alert('Selected Language: ' + selectedLanguage);
            // Close the dropdown after selection
            document.getElementById('languageDropdown').classList.remove('show');
        });
    });
});