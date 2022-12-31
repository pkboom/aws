<?php

require __DIR__ . '/vendor/autoload.php';

use Bref\Context\Context;

return function (array $event, Context $context) {
  echo json_encode([
    "info" => "this is going to my function",
  ]);

  return ['message' => sprintf("Hello %s!", $event['name'] ?? 'unknown')];
};

