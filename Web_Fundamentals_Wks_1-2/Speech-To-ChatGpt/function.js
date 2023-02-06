var input_text = "";
// Initialize webkitSpeechRecognition
let speechRecognition = new webkitSpeechRecognition();
// Initialize SpeechSynthesisUtterance


function speech_to_text() {
    if ("webkitSpeechRecognition" in window) {
    
        // String for the Final Transcript
        let final_transcript = "";
    
        // Set the properties for the Speech Recognition object
        speechRecognition.continuous = true;
        speechRecognition.interimResults = true;
        // speechRecognition.lang = document.querySelector("#select_dialect").value;
    
        // Callback Function for the onStart Event
        // speechRecognition.onstart = () => {
        //     // Show the Status Element
        //     document.querySelector("#status").style.display = "block";
        // };
        // speechRecognition.onerror = () => {
        //     // Hide the Status Element
        //     document.querySelector("#status").style.display = "none";
        // };
        // speechRecognition.onend = () => {
        //     // Hide the Status Element
        //     document.querySelector("#status").style.display = "none";
        // };
    
        speechRecognition.onresult = (event) => {
            // Create the interim transcript string locally because we don't want it to persist like final transcript
            let interim_transcript = "";
    
            // Loop through the results from the speech recognition object.
            for (let i = event.resultIndex; i < event.results.length; ++i) {
            // If the result item is Final, add it to Final Transcript, Else add it to Interim transcript
                if (event.results[i].isFinal) {
                    final_transcript += event.results[i][0].transcript;
                } else {
                    interim_transcript += event.results[i][0].transcript;
                }
            }
    
            // Set the Final transcript and Interim transcript.
            document.querySelector("#final").innerHTML = final_transcript;
            document.querySelector("#interim").innerHTML = interim_transcript;
        };
    
        // Set the onClick property of the start button
        document.querySelector("#start").onclick = () => {
            final_transcript = "";
            // Start the Speech Recognition
            speechRecognition.start();
        };
        // Set the onClick property of the stop button
        document.querySelector("#stop").onclick = () => {
            // Stop the Speech Recognition
            speechRecognition.stop();
            input_text = final_transcript;
            console.log(final_transcript);
        };
        window.speechSynthesis.cancel();

        // populateVoiceList();

        // if (typeof speechSynthesis !== 'undefined' && speechSynthesis.onvoiceschanged !== undefined) {
        //     speechSynthesis.onvoiceschanged = populateVoiceList;
        // }

    } else {
        console.log("Speech Recognition Not Available");
    }
};

// function populateVoiceList() {
//     if (typeof speechSynthesis === 'undefined') {
//         return;
//     }
//     const voices = speechSynthesis.getVoices();
//     for (let i = 0; i < voices.length; i++) {
//         const option = document.createElement('option');
//         option.textContent = `${voices[i].name} (${voices[i].lang})`;
//         if (voices[i].default) {
//             option.textContent += ' — DEFAULT';
//         }
//         option.setAttribute('data-lang', voices[i].lang);
//         option.setAttribute('data-name', voices[i].name);
//         document.getElementById("voices").appendChild(option);
//     }
// }

async function getChatGPT() {

    // OPENAI_SECRET_KEY='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'

    // // OPENAI_API_KEY = `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`

    // const got = require('got');

    // // This is just an example, but could be something you keep track of
    // // in your application to provide OpenAI as prompt text.
    // const chatLog = 'Human: Hello, who are you?\nAI: I am doing great. How can I help you today?\n';

    // // The new question asked by the user.
    // const question = 'Could you tell me what your favorite German thrash metal album is?';

    // (async () => {
    //     const url = 'https://api.openai.com/v1/engines/davinci/completions';
    //     const prompt = `${chatLog}Human: ${question}`;
    //     const params = {
    //         'prompt': prompt,
    //         'max_tokens': 150,
    //         'temperature': 0.9,
    //         'frequency_penalty': 0,
    //         'presence_penalty': 0.6,
    //         'stop': '\nHuman'
    //     };
    //     const headers = {
    //         'Authorization': `Bearer ${process.env.OPENAI_SECRET_KEY}`,
    //     };

    //     try {
    //         const response = await got.post(url, { json: params, headers: headers }).json();
    //         output = `${prompt}${response.choices[0].text}`;
    //         console.log(output);
    //     } catch (err) {
    //         console.log(err);
    //     }
    // })();

};

function text_to_speech() {

    if ('speechSynthesis' in window) {
        // Speech Synthesis supported 🎉

        var msg = new SpeechSynthesisUtterance();

        var voices = window.speechSynthesis.getVoices();

        // input_text = "TeLL me where is Fancy bred, Or in the heart or in the head? How begot, how nourished? Reply, reply. It is engender'd in the eyes, With gazing fed; and Fancy dies." +
        //             "In the cradle where it lies. Let us all ring Fancy's knell: I'll begin it,--Ding, dong, bell. All. Ding, dong, bell."

        msg.voice = voices[1]; 
        msg.volume = 1; // From 0 to 1
        msg.rate = .51; // From 0.1 to 10
        msg.pitch = 0.5; // From 0 to 2
        msg.text = input_text;
        msg.lang = 'es';
        speechSynthesis.speak(msg);
    }else{
         // Speech Synthesis Not Supported 😣
        alert("Sorry, your browser doesn't support text to speech!");
    }

}
