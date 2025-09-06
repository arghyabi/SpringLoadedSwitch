<?php
require 'backend.php';

$appVersion   = getAppVersion();
$currentCount = getCurrentCountValue();
$totalCount   = getTotalCountValue();
$motorStatus  = getMotorStatus();
$switchType   = getSwitchType();
$motorButtonText = $motorStatus == 1 ? "Turn Off" : "Turn On";
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
  <header>
    <h1>Spring Loaded Switch Simulator <?php echo $appVersion; ?></h1>
  </header>
  <main>
    <div class="controls">
      <label for="totalCount">Set Total Count:</label>
      <input type="number" id="totalCount" min="1"/>
      <button id="setCountBtn" class="totalCountBtn" onclick = "updateTotalCountValue()">Set Total Count</button>
    </div>
    <div class="switch-container">
      <h2 id="countDisplay">Count: <?php echo $currentCount; ?> / <?php echo $totalCount; ?></h2>
    </div>
    <div class="controls">
      <label for="switchType">Selected Switch Type:
      <span id="switchTypeStatus"><?php echo $switchType; ?></span></label>
      <select id="switchType" class="switchType">
      <option value="Type-A">Type-A (Single MicroSwitch)</option>
      <option value="Type-B">Type-B (Double MicroSwitch)</option>
      <option value="Type-C">Type-C (Double MicroSwitch)</option>
      <option value="Type-D">Type-D (Single MicroSwitch)</option>
      <option value="Type-E">Type-E (Double MicroSwitch)</option>
      </select>
      <button id="setSwitchTypeBtn" onclick="updateSwitchType()">Update Type</button>
    </div>
    <div class="controls">
      <label for="motorToggle">Motor Status:
      <span id="motorStatus"><?php echo $motorStatus == 1 ? 'ON' : 'OFF'; ?></span></label>
      <button id="motorToggle" class="<?php echo $motorStatus == 1 ? 'motor-on' : 'motor-off'; ?>" onclick="toggleMotor()"><?php echo $motorButtonText; ?></button>
    </div>
  </main>
</body>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="script.js"></script>
</html>
