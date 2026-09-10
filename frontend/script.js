const API_URL = "http://127.0.0.1:5000";


// --------------------------------------------------
// Upload PDF
// --------------------------------------------------

async function uploadPDF() {

    const fileInput =
        document.getElementById("fileInput");

    const uploadStatus =
        document.getElementById("uploadStatus");

    const conversation =
        document.getElementById("conversation");


    if (fileInput.files.length === 0) {

        uploadStatus.textContent =
            "Please select a PDF first.";

        return;
    }


    const file = fileInput.files[0];

    uploadStatus.textContent =
        "Processing PDF...";

    conversation.textContent =
        "Please wait...";


    const formData = new FormData();

    formData.append("file", file);


    try {

        const response = await fetch(
            `${API_URL}/api/upload`,
            {
                method: "POST",
                body: formData
            }
        );


        const data = await response.json();


        if (!response.ok) {
            throw new Error(data.message);
        }


        uploadStatus.textContent =
            `${data.filename} uploaded successfully. ` +
            `${data.chunk_count} chunks created.`;


        conversation.textContent =
            "Document is ready. Ask a question.";


    } catch (error) {

        uploadStatus.textContent =
            `Upload failed: ${error.message}`;

        conversation.textContent = "";

    }
}


// --------------------------------------------------
// Ask Question
// --------------------------------------------------

async function askQuestion() {

    const questionInput =
        document.getElementById("questionInput");

    const conversation =
        document.getElementById("conversation");


    const question =
        questionInput.value.trim();


    if (!question) {

        conversation.textContent =
            "Please enter a question.";

        return;
    }


    conversation.textContent =
        "Searching the document...";


    try {

        const response = await fetch(
            `${API_URL}/api/ask`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );


        const data = await response.json();


        if (!response.ok) {
            throw new Error(data.message);
        }


        displayConversation(
            data.chat_history,
            data.sources
        );


        questionInput.value = "";


    } catch (error) {

        conversation.textContent =
            `Error: ${error.message}`;

    }
}


// --------------------------------------------------
// Display Conversation
// --------------------------------------------------

function displayConversation(
    history,
    sources
) {

    const conversation =
        document.getElementById("conversation");


    conversation.innerHTML = "";


    history.forEach(item => {

        const question =
            document.createElement("div");

        question.className =
            "message question";


        const questionTitle =
            document.createElement("strong");

        questionTitle.textContent =
            "You";


        const questionText =
            document.createElement("p");

        questionText.textContent =
            item.question;


        question.appendChild(
            questionTitle
        );

        question.appendChild(
            questionText
        );


        const answer =
            document.createElement("div");

        answer.className =
            "message answer";


        const answerTitle =
            document.createElement("strong");

        answerTitle.textContent =
            "AI";


        const answerText =
            document.createElement("p");

        answerText.textContent =
            item.answer;


        answer.appendChild(
            answerTitle
        );

        answer.appendChild(
            answerText
        );


        conversation.appendChild(
            question
        );

        conversation.appendChild(
            answer
        );

    });


    if (sources && sources.length > 0) {

        const sourceTitle =
            document.createElement("h3");

        sourceTitle.textContent =
            "Sources";

        conversation.appendChild(
            sourceTitle
        );


        sources.forEach(source => {

            const sourceElement =
                document.createElement("div");

            sourceElement.className =
                "source";


            sourceElement.textContent =
                `Chunk ${source.chunk_id} ` +
                `(Similarity: ${source.score})`;


            conversation.appendChild(
                sourceElement
            );

        });

    }
}


// --------------------------------------------------
// Button Events
// --------------------------------------------------

document
    .getElementById("uploadButton")
    .addEventListener(
        "click",
        uploadPDF
    );


document
    .getElementById("askButton")
    .addEventListener(
        "click",
        askQuestion
    );