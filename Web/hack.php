<?php
require 'backend.php';

$appVersion   = getAppVersion();
$currentCount = getCurrentCountValue();
$totalCount   = getTotalCountValue();
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="resources/site_icon.png" type="image/png">
  <title>Spring Loaded Switch - <?php echo $appVersion; ?></title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="hackHeader">
    <h1>Spring Loaded Switch Simulator <?php echo $appVersion; ?></h1>
  </header>
  <main>
    <div class="controls">
      <label for="totalCount">Set Total Count:</label>
      <input type="number" id="totalCount" min="1"/>
      <button id="setCountBtn" class="totalCountBtn" onclick = "updateTotalCountValue()">Set Total Count</button>
    </div>
    <div class="controls">
      <label for="currentCount">Set Current Count:</label>
      <input type="number" id="currentCount" min="0" />
      <button id="setCurrentBtn" class="currentCountBtn" onclick = "updateCurrentCountValue()">Set Current Count</button>
    </div>
    <div class="switch-container">
      <h2 id="countDisplay">Count: <?php echo $currentCount; ?> / <?php echo $totalCount; ?></h2>
    </div>
    <br/>
    <a href="/"><h1>Home</h1></a>
  </main>
</body>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="script.js"></script>
</html>
