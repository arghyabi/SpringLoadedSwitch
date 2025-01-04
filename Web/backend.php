<?php
use Symfony\Component\Yaml\Yaml;
require 'vendor/autoload.php';


$yamlConfigFilePath = '../config.yaml';
$RtConfigFilePath   = '../rtDb.json';


// get yaml config data
function getConfigData()
{
    global $yamlConfigFilePath;
    $config = Yaml::parseFile($yamlConfigFilePath);
    return $config;
}


// get Run Time Config
function getRtConfig()
{
    global $RtConfigFilePath;
    $jsonContent = file_get_contents($RtConfigFilePath);
    $data = json_decode($jsonContent, true);
    return $data;
}


// Set Run Time Config
function setRtConfig($newData)
{
    global $RtConfigFilePath;
    $jsonData = json_encode($newData, JSON_PRETTY_PRINT);
    file_put_contents($RtConfigFilePath, $jsonData);
}


// get application version
function getAppVersion()
{
    $config  = getConfigData();
    $version = isset($config['appVersion']) ? $config['appVersion'] : '0.0.0.0000';
    return $version;
}


// get current count value
function getCurrentCountValue()
{
    $rtConfig = getRtConfig();
    $currentCount = isset($rtConfig['cycleCount']) ? $rtConfig['cycleCount'] : 0;
    return $currentCount;
}


// get total count value
function getTotalCountValue()
{
    $rtConfig = getRtConfig();
    $maxCount = isset($rtConfig['maxCount']) ? $rtConfig['maxCount'] : 0;

    // if the max value is not found in the RT database then try to get from global config
    if($maxCount == 0)
    {
        $config  = getConfigData();
        $maxCount = isset($config['maxCount']) ? $config['maxCount'] : 0;
    }

    return $maxCount;
}


// update the max count value
function updateMaxCountValue($count)
{
    $rtConfig = getRtConfig();
    $rtConfig["maxCount"] = $count;
    $rtConfig["updateNeeded"] = 1;
    setRtConfig($rtConfig);
}


// update the current count value
function updateCurrentCountValue($count)
{
    $rtConfig = getRtConfig();
    $rtConfig["cycleCount"] = $count;
    $rtConfig["updateNeeded"] = 1;
    setRtConfig($rtConfig);
}
?>
