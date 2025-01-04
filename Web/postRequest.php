<?php
require 'backend.php';
header('Content-Type: application/json');

$indexFilePath = '';

// get all count values
if(isset($_POST["getCountValues"]))
{
    $currentVal = getCurrentCountValue();
    $maxVal     = getTotalCountValue();

    $response = [
        'currentVal' => $currentVal,
        'maxVal'     => $maxVal,
    ];

    echo json_encode($response);
}

// update total count
if(isset($_POST["updateTotalCount"]))
{
    $newCurrentVal = $_POST['newTotalCount'];
    $currentVal = getCurrentCountValue();

    if($newCurrentVal < $currentVal)
    {
        $msg = "New Total value is less then current count; Reset the Current value.";
        $status = FALSE;
    }
    else
    {
        updateMaxCountValue($newCurrentVal);
        $msg = "Update Successful.";
        $status = TRUE;
    }

    $response = [
        'msg'    => $msg,
        'status' => $status,
    ];

    echo json_encode($response);
}


// update current count
if(isset($_POST["updateCurrentCount"]))
{
    $newCurrentVal = $_POST['newCurrentCount'];
    $maxVal = getTotalCountValue();

    if($newCurrentVal > $maxVal)
    {
        $msg = "New Current value is greater then Total count; Reset the Total value.";
        $status = FALSE;
    }
    else
    {
        updateCurrentCountValue($newCurrentVal);
        $msg = "Update Successful.";
        $status = TRUE;
    }

    $response = [
        'msg'    => $msg,
        'status' => $status,
    ];

    echo json_encode($response);
}

?>