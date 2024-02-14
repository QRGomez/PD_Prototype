async function uploadAudio() {
    const fileInput = document.getElementById('audioInput');
    await uploadFile(fileInput, 'https://c283-136-158-1-127.ngrok-free.app/transcribe/audio', 'audioResult');
}

async function uploadVideo() {
    const fileInput = document.getElementById('videoInput');
    await uploadFile(fileInput, 'https://c283-136-158-1-127.ngrok-free.app/transcribe/video', 'videoResult');
}

async function uploadImage() {
    const fileInput = document.getElementById('imageInput');
    await uploadFile(fileInput, 'https://c283-136-158-1-127.ngrok-free.app/transcribe/image', 'imageResult');
}


async function uploadFile(fileInput, endpoint, resultDivId) {
    const file = fileInput.files[0];

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                body: formData,
                headers:new Headers({
                    "ngrok-skip-browser-warning": "69420",
                  })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);

            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'transcription.doc');
            document.body.appendChild(link);
            link.click();
            link.parentNode.removeChild(link);

        } catch (error) {
            console.error('Error uploading file:', error);
        }
    } else {
        console.error(`Please select a file`);
    }
}
