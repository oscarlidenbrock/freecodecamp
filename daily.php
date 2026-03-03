<?php

/* get date in YYYY-MM-DD format */
if (isset($argv[1])) {
    $arg = $argv[1];
} else {
    $arg = date('Y-m-d');
}

/* get json data */
$url = "https://api.freecodecamp.org/daily-coding-challenge/date/".$arg;

try {
    if ($html = getHTMl($url)) {
        $json = json_decode($html, true);
    }
} catch (Exception $e) {
    die('JSON decode error: '.$e->getMessage().'\n');
}

/* set tpl variables */
$description = strip_tags($json['description']);
$description = "# ".str_replace("\n", "\n# ", $description);

$function = $json['python']['challengeFiles'][0]['contents'];
$testFunction = "";

if (preg_match('/def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(/', $function, $matches)) {
    $functionName = $matches[1];
}

if (preg_match('/\((.*?)\)/', $function, $matches)) {
    $functionVariables = explode(',', $matches[1]);

    foreach ($functionVariables as &$functionVariable) {
        $functionVariable = trim($functionVariable);
    }
}

if ($functionName && $functionVariables) {
    $testFunction = $functionName."(";

    foreach ($functionVariables as $key => $functionVariable) {
        $testFunction .= "test['parameters'][$key]";
        if ($key < count($functionVariables) - 1) $testFunction .= ", ";
    }

    $testFunction .= ")";
}

$testCode = $json['python']['tests'][0]['text'];
$resultFormat = "¿?";

if (preg_match('/should return <code>(.*?)<\/code>/', $testCode, $match)) {
    $returnValue = trim($match[1]);

    if ($returnValue === 'True' || $returnValue === 'False') {
        $resultFormat = 'bool';
    } elseif ($returnValue === 'None') {
        $resultFormat = 'NoneType';
    } elseif (preg_match('/^\[.*\]$/s', $returnValue)) {
        $resultFormat = 'list';
    } elseif (preg_match('/^\{.*\}$/s', $returnValue)) {
        $resultFormat = 'dict';
    } elseif (preg_match('/^\(.*\)$/s', $returnValue)) {
        $resultFormat = 'tuple';
    } elseif (preg_match('/^[0-9]+$/', $returnValue)) {
        $resultFormat = 'int';
    } elseif (preg_match('/^[0-9]*\.[0-9]+$/', $returnValue)) {
        $resultFormat = 'float';
    } elseif (preg_match('/^["\'].*["\']$/', $returnValue)) {
        $resultFormat = 'str';
    } else {
        $resultFormat = 'unknown';
    }
}

$unitTest = "";

foreach ($json['python']['tests'] as $test) {
    $testString = $test['testString'];

    if (preg_match('/(\w+)\((.+)\),\s*(.+)\)/', $testString, $matches)) {
        $functionArgs = $matches[2];  // argumentos de la función
        $expected = $matches[3];      // valor esperado

        $segments = explode('(', $functionArgs);
        $params = end($segments);

        $segments = explode(')', $expected);
        $resultValue = $segments[0];

        $result[] = [
            'parameters' => $params,
            'result' => $resultValue
        ];

        $unitTest = [];

        foreach ($result as $test) {
            $unitTest[] = '{"parameters": ['.$test['parameters'].'], "result": '.$test['result'].'},';
        }

        $unitTest = "        ".implode("\n        ", $unitTest);
    }
}

$tplValues = [
    '{{ date }}' => $arg,
    '{{ title }}' => $json['title'],
    '{{ challenge_url }}' => 'https://www.freecodecamp.org/learn/daily-coding-challenge/'.$arg,
    '{{ description }}' => $description,
    '{{ function }}' => $function,
    '{{ parameters_format }}' => 'list',
    '{{ result_format }}' => $resultFormat,
    '{{ unittest }}' => $unitTest,
    '{{ test_function  }}' => $testFunction
];

/* replace template variables */
$tpl = file_get_contents(__DIR__ . '/daily.tpl');
$tpl = str_replace(array_keys($tplValues), array_values($tplValues), $tpl);

/* save result */
$date = new DateTime($arg);
$path = __DIR__ . '/challenges/'.$date->format("Y-m").'/';
if (!is_dir($path)) mkdir($path, 0755, true);

$fileName = $date->format("d").'_'.str_replace(' ', '-', strtolower($json['title'])).'.py';
file_put_contents($path.$fileName, $tpl);

function getHTML(string $url): string|false
{
    $ch = curl_init($url);

    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_MAXREDIRS => 5,
        CURLOPT_CONNECTTIMEOUT => 10,
        CURLOPT_TIMEOUT => 30,
        CURLOPT_SSL_VERIFYPEER => true,
        CURLOPT_USERAGENT => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
        CURLOPT_ENCODING => '',
        CURLOPT_HTTPHEADER => [
            'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language: es-ES,es;q=0.9,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding: gzip, deflate, br',
            'Connection: keep-alive',
            'Upgrade-Insecure-Requests: 1',
        ]
    ]);

    $response = curl_exec($ch);

    if (curl_errno($ch)) {
        curl_close($ch);
        return false;
    }

    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($httpCode >= 200 && $httpCode < 300) {
        return $response;
    }

    return false;
}